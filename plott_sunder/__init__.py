from otree.api import *
import random


doc = """
Experimento simplificado de Plott & Sunder (1988) sobre agregación de información.
Los jugadores reciben señales privadas sobre el valor de un activo y hacen predicciones.
"""


class C(BaseConstants):
    NAME_IN_URL = 'plott_sunder'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 5

    # Valores posibles del activo según el estado
    VALORES_POSIBLES = [0, 240, 480]
    ESTADOS = ['X', 'Y', 'Z']  # X=0, Y=240, Z=480

    # Premio por mejor predicción
    PREMIO = cu(1000)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    """Asigna el estado verdadero y las señales privadas a cada grupo.
    Funciona con grupos de 1, 2 o 3 jugadores automáticamente."""
    for group in subsession.get_groups():
        # Seleccionar aleatoriamente el estado verdadero
        estado_idx = random.randint(0, 2)
        group.estado_verdadero = C.ESTADOS[estado_idx]
        group.valor_verdadero = C.VALORES_POSIBLES[estado_idx]

        players = group.get_players()
        num_players = len(players)

        # Asignar señales según el tamaño del grupo
        if num_players == 1:
            # Un solo jugador: asignar señal aleatoria
            estado_descartado = random.choice(C.ESTADOS)
            players[0].señal_privada = f"NOT {estado_descartado}"

        elif num_players == 2:
            # Dos jugadores: cada uno descarta un estado diferente (aleatorio)
            estados_disponibles = C.ESTADOS.copy()
            random.shuffle(estados_disponibles)
            for i, player in enumerate(players):
                player.señal_privada = f"NOT {estados_disponibles[i]}"

        else:
            # Tres o más jugadores: distribuir las 3 señales cíclicamente
            estados_a_descartar = []
            for i in range(num_players):
                estado_descartado = C.ESTADOS[i % 3]
                estados_a_descartar.append(estado_descartado)

            # Mezclar aleatoriamente las señales
            random.shuffle(estados_a_descartar)

            # Asignar señales a jugadores
            for player, estado_descartado in zip(players, estados_a_descartar):
                player.señal_privada = f"NOT {estado_descartado}"


class Group(BaseGroup):
    estado_verdadero = models.StringField()
    valor_verdadero = models.CurrencyField()

    # Para almacenar la mejor predicción y número de ganadores
    mejor_prediccion = models.IntegerField()
    n_ganadores = models.IntegerField()


class Player(BasePlayer):
    señal_privada = models.StringField()

    # Predicción del jugador
    prediccion = models.IntegerField(
        min=0,
        max=480,
        label="¿Cuál crees que es el valor verdadero del activo?"
    )

    # Para tracking
    es_ganador = models.BooleanField(initial=False)


# FUNCTIONS
def set_payoffs(group: Group):
    """Calcula los pagos basados en qué tan cerca estuvieron las predicciones"""
    players = group.get_players()
    predicciones = [p.prediccion for p in players]

    # Encontrar la predicción más cercana al valor verdadero
    valor_real = int(group.valor_verdadero)
    group.mejor_prediccion = min(predicciones, key=lambda pred: abs(pred - valor_real))

    # Encontrar todos los ganadores (los que hicieron la mejor predicción)
    ganadores = [p for p in players if p.prediccion == group.mejor_prediccion]
    group.n_ganadores = len(ganadores)

    # Asignar pagos
    for p in ganadores:
        p.es_ganador = True
        p.payoff = C.PREMIO / group.n_ganadores


# PAGES
class Instrucciones(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Prediccion(Page):
    form_model = 'player'
    form_fields = ['prediccion']

    @staticmethod
    def vars_for_template(player: Player):
        # Calcular qué valores son posibles según la señal
        señal = player.señal_privada
        if "NOT X" in señal:
            valores_posibles = [240, 480]
            valor_esperado = (240 + 480) / 2
        elif "NOT Y" in señal:
            valores_posibles = [0, 480]
            valor_esperado = (0 + 480) / 2
        else:  # NOT Z
            valores_posibles = [0, 240]
            valor_esperado = (0 + 240) / 2

        # Combinar histórico de predicciones y valores en una lista de diccionarios
        historico = []
        for ronda in range(1, player.round_number):
            pred = player.in_round(ronda).prediccion
            valor = player.group.in_round(ronda).valor_verdadero
            error = abs(pred - int(valor))
            historico.append({
                'ronda': ronda,
                'prediccion': pred,
                'valor': valor,
                'error': error
            })

        # Si estamos en ronda 4 o 5, calcular estadísticas agregadas del grupo de rondas 1-3
        estadisticas_grupo = None
        if player.round_number >= 4:
            todas_predicciones_1_3 = []
            for ronda in range(1, 4):  # rondas 1, 2, 3
                group_in_ronda = player.group.in_round(ronda)
                for p in group_in_ronda.get_players():
                    todas_predicciones_1_3.append(p.prediccion)

            if todas_predicciones_1_3:
                estadisticas_grupo = {
                    'promedio': round(sum(todas_predicciones_1_3) / len(todas_predicciones_1_3), 2),
                    'minimo': min(todas_predicciones_1_3),
                    'maximo': max(todas_predicciones_1_3),
                    'total_predicciones': len(todas_predicciones_1_3)
                }

        return dict(
            valores_posibles=valores_posibles,
            valor_esperado=valor_esperado,
            historico=historico,
            estadisticas_grupo=estadisticas_grupo
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Resultados(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        # Obtener todas las predicciones ordenadas
        predicciones_ordenadas = sorted([p.prediccion for p in group.get_players()])

        # Calcular error de la predicción del jugador
        error = abs(player.prediccion - int(group.valor_verdadero))

        return dict(
            predicciones_ordenadas=predicciones_ordenadas,
            error=error
        )


class ResultadosFinales(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        # Calcular payoff total acumulado de cada jugador
        jugadores_info = []
        for p in player.group.get_players():
            total_payoff = sum([p.in_round(r).payoff for r in range(1, C.NUM_ROUNDS + 1)])
            jugadores_info.append({
                'id': p.id_in_group,
                'payoff': total_payoff
            })

        # Ordenar por payoff (de mayor a menor)
        jugadores_info.sort(key=lambda x: x['payoff'], reverse=True)

        # Agregar ranking con manejo de empates
        current_rank = 1
        for idx, jugador in enumerate(jugadores_info):
            if idx > 0 and jugadores_info[idx]['payoff'] < jugadores_info[idx-1]['payoff']:
                current_rank = idx + 1
            jugador['ranking'] = current_rank

        # Encontrar el payoff total del jugador actual
        mi_payoff_total = sum([player.in_round(r).payoff for r in range(1, C.NUM_ROUNDS + 1)])

        # Encontrar el ranking del jugador actual
        mi_ranking = next(j['ranking'] for j in jugadores_info if j['id'] == player.id_in_group)

        # Extraer Top 3 (puede ser más de 3 si hay empates en posición 3)
        top_3 = []
        for jugador in jugadores_info:
            if jugador['ranking'] <= 3:
                top_3.append(jugador)

        return dict(
            top_3=top_3,
            mi_payoff_total=mi_payoff_total,
            mi_ranking=mi_ranking
        )


page_sequence = [Instrucciones, Prediccion, ResultsWaitPage, Resultados, ResultadosFinales]
