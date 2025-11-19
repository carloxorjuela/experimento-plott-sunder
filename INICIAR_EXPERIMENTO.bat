@echo off
chcp 65001 >nul
cls
echo ============================================================
echo   Experimento Plott ^& Sunder (1988) - 5 Rondas
echo ============================================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Entorno virtual no encontrado
    echo.
    echo Por favor ejecuta primero: INSTALAR.bat
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate.bat

REM Crear _static si no existe
if not exist "_static" mkdir _static

REM Verificar si otree está instalado
python -c "import otree" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] oTree no está instalado en el entorno virtual
    echo Por favor ejecuta primero: INSTALAR.bat
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

REM Abrir navegador
echo [INFO] Abriendo navegador en http://localhost:8000
start http://localhost:8000

REM Correr servidor
echo.
echo ============================================================
echo   ✓ SERVIDOR CORRIENDO
echo ============================================================
echo.
echo   URL: http://localhost:8000
echo   Usuario: admin
echo   Contraseña: admin123
echo.
echo   Para DETENER el servidor: Presiona Ctrl+C
echo ============================================================
echo.

otree devserver

pause
