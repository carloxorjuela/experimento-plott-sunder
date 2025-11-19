# Experimento Plott & Sunder (1988) - Simplificado

Implementación simplificada del experimento de agregación de información de Plott & Sunder (1988) en oTree con 5 rondas.

## 🎯 Características Principales

### 1. Grupos Flexibles Automáticos
El experimento ahora funciona con **cualquier número de participantes**. El sistema automáticamente divide a los participantes en grupos de 3 jugadores cada uno.

**Ejemplos:**
- 3 participantes → 1 grupo de 3
- 6 participantes → 2 grupos de 3
- 9 participantes → 3 grupos de 3
- 30 participantes → 10 grupos de 3

Si el número de participantes no es múltiplo de 3, los grupos restantes se ajustan automáticamente:
- 4 participantes → 1 grupo de 3 + 1 grupo de 1
- 5 participantes → 1 grupo de 3 + 1 grupo de 2
- 7 participantes → 2 grupos de 3 + 1 grupo de 1

### 2. Distribución Inteligente de Señales

El sistema asigna señales privadas según el tamaño del grupo:

#### Grupo de 3 jugadores (ideal):
- Jugador 1: "NOT X" → Sabe que vale 240 o 480
- Jugador 2: "NOT Y" → Sabe que vale 0 o 480
- Jugador 3: "NOT Z" → Sabe que vale 0 o 240

#### Grupo de 2 jugadores:
- Cada jugador recibe una señal diferente aleatoriamente seleccionada

#### Grupo de 1 jugador:
- Recibe una señal aleatoria

### 3. Top 3 Ganadores

La página de resultados finales muestra:
- **Solo los 3 primeros lugares** con medallas 🥇🥈🥉
- Tarjetas grandes y visibles para cada ganador
- Si estás en el Top 3, tu tarjeta se resalta con borde verde
- Si NO estás en el Top 3, se muestra tu posición arriba

**Manejo de empates:**
- Si hay empate en primer lugar, todos los empatados reciben 🥇
- El ranking se ajusta correctamente (ej: si hay 2 primeros, el siguiente es #3)

## 🚀 Instalación Rápida (Windows - 1 Click)

### Primera Vez:

1. **Doble click en**: `INSTALAR.bat` (instala todo automáticamente en 2-3 minutos)
2. **Doble click en**: `INICIAR_CON_ENTORNO_VIRTUAL.bat` (inicia el servidor)
3. **Elige opción**: 1 (localhost) o 2 (red local)

### Usos Posteriores:

- **Doble click en**: `INICIAR_CON_ENTORNO_VIRTUAL.bat`

🎉 **No necesitas usar la terminal** - Todo está automatizado.

### 📋 Scripts Disponibles:

- **`INSTALAR.bat`** - Instalación automática (solo primera vez)
- **`INICIAR_CON_ENTORNO_VIRTUAL.bat`** - ✅ **RECOMENDADO** (localhost o red local)
- **`INICIAR_SIN_ENTORNO_VIRTUAL.bat`** - Sin entorno virtual (requiere oTree global)
- **`INICIAR_EXPERIMENTO.bat`** - Versión simple (solo localhost)

**📖 Ver guía completa**: `GUIA_DE_SCRIPTS.md`

---

## 🎮 Uso Básico

Después de hacer doble click en `INICIAR_EXPERIMENTO.bat`:

1. Se abrirá el navegador en http://localhost:8000
2. Login: **admin** / **admin123**
3. Sessions → Create new session
4. Selecciona "Experimento Plott & Sunder (1988) - Simplificado"
5. Participantes: Ingresa un **múltiplo de 3** (ej: 3, 6, 9, 12, 15, 30, etc.)
6. Click "Create"
7. Comparte los links con los estudiantes

---

## 💻 Instalación Manual (Alternativa)

Si prefieres hacerlo manualmente:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Resetear base de datos
otree resetdb --noinput

# Iniciar servidor
otree devserver
```

---

## 🎮 Modo Producción

Para ejecutar con participantes reales:

```bash
venv\Scripts\activate
otree prodserver
```

## 📊 Configuración

### Cambiar número de jugadores por grupo

Edita `plott_sunder/__init__.py` línea 13:

```python
PLAYERS_PER_GROUP = 3  # Cambiar a None para grupos dinámicos
```

**Recomendado:** Mantener en 3 para la mejor experiencia pedagógica.

### Cambiar número de rondas

Edita `plott_sunder/__init__.py` línea 14:

```python
NUM_ROUNDS = 5  # Cambiar al número deseado
```

### Cambiar premio por ronda

Edita `plott_sunder/__init__.py` línea 21:

```python
PREMIO = cu(1000)  # Cambiar al valor deseado
```

## 🎓 Concepto Pedagógico

Este experimento enseña:

✅ **Información asimétrica**: Cada jugador posee información privada diferente
✅ **Agregación de información**: Las decisiones individuales pueden revelar información colectiva
✅ **Valor esperado**: Cálculo de predicción racional bajo incertidumbre
✅ **Inferencia bayesiana**: Actualización de creencias con nueva información

## 📁 Estructura del Proyecto

```
plott_sunder/
├── settings.py                 # Configuración de oTree
├── requirements.txt            # Dependencias
├── README.md                   # Esta documentación
└── plott_sunder/              # App principal
    ├── __init__.py            # Lógica del juego
    ├── Instrucciones.html     # Página de instrucciones
    ├── Prediccion.html        # Página de predicción
    ├── Resultados.html        # Resultados por ronda
    └── ResultadosFinales.html # Top 3 ganadores
```

## 🏆 Sistema de Puntos

- Cada ronda otorga **1000 puntos** al mejor predictor
- Si hay empate, el premio se divide equitativamente
- El ranking final se basa en puntos acumulados de las 5 rondas
- Máximo posible: 5000 puntos (ganar las 5 rondas)
- **Rondas 4 y 5**: Los jugadores ven estadísticas públicas (promedio, mínimo, máximo) de las predicciones del grupo en rondas 1-3

## 🔧 Ejemplos de Configuración

### Clase pequeña (9 estudiantes)
```python
PLAYERS_PER_GROUP = 3
num_demo_participants = 9
```
Resultado: 3 grupos de 3 jugadores

### Clase mediana (30 estudiantes)
```python
PLAYERS_PER_GROUP = 3
num_demo_participants = 30
```
Resultado: 10 grupos de 3 jugadores

### Experimento individual
```python
PLAYERS_PER_GROUP = None  # Grupos dinámicos
num_demo_participants = 1
```
Resultado: 1 grupo de 1 jugador

## ❓ Preguntas Frecuentes

**P: ¿Qué pasa si tengo 10 participantes?**
R: Se crearán 3 grupos de 3 + 1 grupo de 1. El sistema funciona con cualquier número.

**P: ¿Puedo cambiar los valores del activo?**
R: Sí, edita `VALORES_POSIBLES` en `__init__.py` línea 17.

**P: ¿Cuántos jugadores pueden ganar por ronda?**
R: Entre 1 y todos los jugadores del grupo, si empatan en la mejor predicción.

## 📚 Referencia

Plott, C. R., & Sunder, S. (1988). Rational expectations and the aggregation of diverse information in laboratory security markets. *Econometrica*, 1085-1118.

## 🔒 ¿Por qué usar Entorno Virtual?

Este proyecto usa un **entorno virtual de Python** (`venv/`) porque:

✅ **Aislamiento**: Las dependencias del proyecto no interfieren con otras instalaciones de Python
✅ **Versiones específicas**: oTree requiere Django 3.2.x - si el sistema tiene otra versión, puede haber conflictos
✅ **Portabilidad**: El proyecto funciona igual en cualquier computador
✅ **Profesionalismo**: Es la mejor práctica estándar en desarrollo Python
✅ **Seguridad**: Se puede borrar completamente sin afectar el sistema (solo la carpeta `venv/`)

**Para el profesor**: Los scripts `INSTALAR.bat` e `INICIAR_EXPERIMENTO.bat` manejan el entorno virtual automáticamente. Solo haz doble click y listo.

---

## 📝 Licencia

Proyecto académico para uso educativo.
