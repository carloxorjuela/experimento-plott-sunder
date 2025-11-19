@echo off
chcp 65001 >nul
cls
echo ============================================================
echo   Experimento Plott ^& Sunder - SIN ENTORNO VIRTUAL
echo ============================================================
echo.
echo [ADVERTENCIA] Este script usa Python global del sistema
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo Por favor instala Python 3.8+ desde https://www.python.org
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Crear _static si no existe
if not exist "_static" mkdir _static

REM Verificar si otree está instalado globalmente
python -c "import otree" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] oTree no esta instalado en el sistema
    echo.
    echo Por favor instala oTree con:
    echo   pip install otree
    echo.
    echo O usa el script: INICIAR_CON_ENTORNO_VIRTUAL.bat
    echo.
    pause
    exit /b 1
)

echo [OK] oTree encontrado
echo.

REM Resetear base de datos
echo [INFO] Reseteando base de datos...
otree resetdb --noinput
echo.

REM Menú de selección
echo ============================================================
echo   SELECCIONA MODO DE ACCESO:
echo ============================================================
echo.
echo   1. LOCALHOST (solo este computador)
echo      URL: http://localhost:8000
echo.
echo   2. RED LOCAL (otros dispositivos pueden conectarse)
echo      URL: http://[TU_IP]:8000
echo.
set /p OPCION="Ingresa tu opcion (1 o 2): "

if "%OPCION%"=="1" (
    set HOST=localhost
    set URL=http://localhost:8000
) else if "%OPCION%"=="2" (
    REM Obtener IP local automáticamente
    for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
        set IP_TEMP=%%a
        goto :ip_found
    )
    :ip_found
    REM Limpiar espacios
    for /f "tokens=* delims= " %%a in ("%IP_TEMP%") do set IP_LOCAL=%%a
    set HOST=0.0.0.0
    set URL=http://%IP_LOCAL%:8000
) else (
    echo [ERROR] Opcion invalida
    pause
    exit /b 1
)

cls
echo ============================================================
echo   SERVIDOR INICIANDO...
echo ============================================================
echo.
echo [INFO] Modo seleccionado: %OPCION%
echo [INFO] Host: %HOST%
echo.

REM Abrir navegador
echo [INFO] Abriendo navegador...
start %URL%

REM Esperar 2 segundos
timeout /t 2 /nobreak >nul

REM Mostrar información de acceso
cls
echo ============================================================
echo   ✓ SERVIDOR CORRIENDO
echo ============================================================
echo.
if "%OPCION%"=="1" (
    echo   Modo: LOCALHOST
    echo   URL: %URL%
    echo.
    echo   [i] Solo accesible desde este computador
) else (
    echo   Modo: RED LOCAL
    echo   URL: %URL%
    echo.
    echo   [i] Compartir esta URL con los participantes:
    echo   [i] %URL%
    echo   [i] Todos deben estar en la misma red WiFi
)
echo.
echo   Usuario: admin
echo   Contrasena: admin123
echo.
echo   Para DETENER: Presiona Ctrl+C
echo ============================================================
echo.

REM Correr servidor
otree devserver %HOST%:8000

pause
