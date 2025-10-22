from os import environ

# SESSION CONFIGS
SESSION_CONFIGS = [
    dict(
        name='plott_sunder',
        display_name='Experimento Plott & Sunder (1988) - Simplificado',
        app_sequence=['plott_sunder'],
        num_demo_participants=3,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# PARTICIPANT_FIELDS: campos personalizados que se pueden acceder entre apps
PARTICIPANT_FIELDS = []

# SESSION_FIELDS: campos personalizados a nivel de sesión
SESSION_FIELDS = []

# ISO-639 code
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = True

# ADMIN CREDENTIALS (cambiar en producción)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin123')

# SECRET_KEY (cambiar en producción con una cadena aleatoria segura)
SECRET_KEY = '7k@9m#p$r2x!q5w&8n*d4f-j6h+b3v=c1z%a0e^t'

# DEBUG MODE
DEBUG = True

# ROOMS configuration (opcional)
ROOMS = [
    dict(
        name='plott_sunder_lab',
        display_name='Laboratorio Plott & Sunder',
    ),
]

# AUTH LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL', 'STUDY')

# Configuración de producción
DEMO_PAGE_INTRO_HTML = """
<p>Experimentos económicos implementados en oTree</p>
"""
