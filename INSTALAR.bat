@echo off
chcp 65001 >nul
cls
echo ============================================================
echo   INSTALACIÓN AUTOMÁTICA - Experimento Plott ^& Sunder
echo ============================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo Por favor instala Python 3.8+ desde https://www.python.org
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verificar si existe el entorno virtual
if exist "venv\Scripts\activate.bat" (
    echo [OK] Entorno virtual ya existe
    echo.
) else (
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado
    echo.
)

REM Activar entorno virtual
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate.bat

REM Actualizar pip
echo [INFO] Actualizando pip...
python -m pip install --upgrade pip --quiet

REM Instalar dependencias
echo [INFO] Instalando dependencias (esto puede tomar 1-2 minutos)...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Error al instalar dependencias
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   ✓ INSTALACIÓN COMPLETADA
echo ============================================================
echo.
echo El entorno virtual está configurado en: venv\
echo.
echo PRÓXIMOS PASOS:
echo   1. Cierra esta ventana
echo   2. Haz doble click en: INICIAR_EXPERIMENTO.bat
echo.
pause
