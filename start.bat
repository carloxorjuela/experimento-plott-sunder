@echo off
echo ========================================
echo   Experimento Plott ^& Sunder (1988)
echo ========================================
echo.

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo [ERROR] No se encontro el entorno virtual.
    echo Por favor ejecuta primero: python -m venv venv
    echo.
    pause
    exit /b 1
)

echo [1/3] Activando entorno virtual...
call venv\Scripts\activate.bat

echo [2/3] Verificando Redis...
tasklist /FI "IMAGENAME eq redis-server.exe" 2>NUL | find /I /N "redis-server.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo [ADVERTENCIA] Redis no esta ejecutandose.
    echo Por favor inicia Redis en otra terminal con: redis-server
    echo.
)

echo [3/3] Iniciando servidor de oTree...
echo.
echo ========================================
echo   Servidor iniciado en:
echo   http://localhost:8000
echo.
echo   Usuario: admin
echo   Password: admin123
echo ========================================
echo.

otree devserver

pause
