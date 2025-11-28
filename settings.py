from os import environ

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

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'es'
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = True

ADMIN_USERNAME = environ.get('OTREE_ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = environ.get('OTREE_SECRET_KEY', '7k@9m#p$r2x!q5w&8n*d4f-j6h+b3v=c1z%a0e^t')

DEBUG = environ.get('OTREE_DEBUG', '') == '1'

ROOMS = [
    dict(
        name='plott_sunder_lab',
        display_name='Laboratorio Plott & Sunder',
    ),
]

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL', 'STUDY')

DEMO_PAGE_INTRO_HTML = """
<p>Experimentos económicos implementados en oTree</p>
"""
