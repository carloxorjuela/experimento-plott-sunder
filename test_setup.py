#!/usr/bin/env python
"""
Script de prueba para verificar que el proyecto está configurado correctamente
"""

import sys
import os

def test_imports():
    """Prueba que todos los imports necesarios funcionen"""
    print("=" * 60)
    print("PRUEBA 1: Verificando imports...")
    print("=" * 60)

    try:
        import django
        print("✅ Django importado correctamente:", django.__version__)
    except ImportError as e:
        print("❌ Error importando Django:", e)
        return False

    try:
        import otree
        print("✅ oTree importado correctamente")
    except ImportError as e:
        print("❌ Error importando oTree:", e)
        return False

    try:
        import channels
        print("✅ Channels importado correctamente")
    except ImportError as e:
        print("❌ Error importando Channels:", e)
        return False

    return True

def test_settings():
    """Prueba que settings.py sea válido"""
    print("\n" + "=" * 60)
    print("PRUEBA 2: Verificando settings.py...")
    print("=" * 60)

    try:
        import settings
        print("✅ settings.py cargado correctamente")

        if hasattr(settings, 'SESSION_CONFIGS'):
            print(f"✅ SESSION_CONFIGS encontrado con {len(settings.SESSION_CONFIGS)} configuración(es)")
            for config in settings.SESSION_CONFIGS:
                print(f"   - {config.get('display_name', 'Sin nombre')}")
                app_seq = config.get('app_sequence', [])
                print(f"     app_sequence: {app_seq}")
                if 'plott_sunder' in app_seq:
                    print("   ✅ app_sequence correcto: ['plott_sunder']")
                else:
                    print(f"   ⚠️  app_sequence: {app_seq} (debería ser ['plott_sunder'])")
        else:
            print("❌ SESSION_CONFIGS no encontrado")
            return False

        if hasattr(settings, 'SECRET_KEY'):
            print("✅ SECRET_KEY configurado")
        else:
            print("❌ SECRET_KEY no encontrado")
            return False

        return True
    except Exception as e:
        print(f"❌ Error cargando settings.py: {e}")
        return False

def test_structure():
    """Prueba que la estructura de carpetas sea correcta"""
    print("\n" + "=" * 60)
    print("PRUEBA 3: Verificando estructura de carpetas...")
    print("=" * 60)

    required_items = {
        'settings.py': 'archivo',
        'requirements.txt': 'archivo',
        '_static': 'carpeta',
        'plott_sunder': 'carpeta',
        'plott_sunder/__init__.py': 'archivo',
    }

    all_ok = True
    for item, tipo in required_items.items():
        exists = os.path.exists(item)
        if exists:
            if tipo == 'carpeta' and os.path.isdir(item):
                print(f"✅ {item}/ encontrado")
            elif tipo == 'archivo' and os.path.isfile(item):
                print(f"✅ {item} encontrado")
            else:
                print(f"⚠️  {item} existe pero tipo incorrecto")
                all_ok = False
        else:
            print(f"❌ {item} NO encontrado")
            all_ok = False

    return all_ok

def test_app():
    """Prueba que la app principal se pueda importar"""
    print("\n" + "=" * 60)
    print("PRUEBA 4: Verificando la app plott_sunder...")
    print("=" * 60)

    try:
        # Agregar el directorio actual al path si no está
        if '.' not in sys.path:
            sys.path.insert(0, '.')

        import plott_sunder as app
        print("✅ App plott_sunder importada correctamente")

        # Verificar que tenga las clases necesarias
        checks = [
            ('C', 'Constants'),
            ('Subsession', 'Subsession'),
            ('Group', 'Group'),
            ('Player', 'Player'),
        ]

        for attr, name in checks:
            if hasattr(app, attr):
                print(f"✅ Clase {name} encontrada")
            else:
                print(f"❌ Clase {name} NO encontrada")
                return False

        # Verificar páginas
        if hasattr(app, 'page_sequence'):
            pages = app.page_sequence
            print(f"✅ page_sequence encontrado con {len(pages)} páginas:")
            for page in pages:
                page_name = page.__name__ if hasattr(page, '__name__') else str(page)
                print(f"   - {page_name}")
        else:
            print("❌ page_sequence no encontrado")
            return False

        return True
    except Exception as e:
        print(f"❌ Error importando la app: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_templates():
    """Prueba que los templates existan"""
    print("\n" + "=" * 60)
    print("PRUEBA 5: Verificando templates HTML...")
    print("=" * 60)

    templates = [
        'plott_sunder/Instrucciones.html',
        'plott_sunder/SeñalPrivada.html',
        'plott_sunder/Mercado.html',
        'plott_sunder/Resultados.html'
    ]

    all_exist = True
    for template in templates:
        if os.path.exists(template):
            size = os.path.getsize(template)
            filename = os.path.basename(template)
            print(f"✅ {filename} encontrado ({size} bytes)")
        else:
            print(f"❌ {template} NO encontrado")
            all_exist = False

    # Verificar _templates/global/Page.html
    global_template = os.path.join('plott_sunder', '_templates', 'global', 'Page.html')
    if os.path.exists(global_template):
        print(f"✅ _templates/global/Page.html encontrado")
    else:
        print(f"❌ _templates/global/Page.html NO encontrado")
        all_exist = False

    return all_exist

def main():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "VERIFICACIÓN DE CONFIGURACIÓN OTREE" + " " * 12 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    # Verificar que estamos en el directorio correcto
    if not os.path.exists('settings.py'):
        print("❌ ERROR: settings.py no encontrado en el directorio actual")
        print("   Por favor ejecuta este script desde el directorio del proyecto")
        print(f"   Directorio actual: {os.getcwd()}")
        return False

    results = []

    # Ejecutar pruebas
    results.append(("Imports", test_imports()))
    results.append(("Settings", test_settings()))
    results.append(("Estructura", test_structure()))
    results.append(("App", test_app()))
    results.append(("Templates", test_templates()))

    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)

    all_passed = True
    for name, passed in results:
        status = "✅ PASÓ" if passed else "❌ FALLÓ"
        print(f"{name:.<30} {status}")
        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("=" * 60)
        print("\nPuedes ejecutar el servidor con:")
        print("  otree devserver")
        print("\nO primero resetear la base de datos:")
        print("  otree resetdb")
        print("  otree devserver")
    else:
        print("⚠️  ALGUNAS PRUEBAS FALLARON")
        print("=" * 60)
        print("\nConsulta ESTRUCTURA_CORRECTA.md para verificar la estructura")
        print("Consulta SOLUCION_ERRORES.md para más ayuda")
    print()

    return all_passed

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nPrueba interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
