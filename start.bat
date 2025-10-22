# Crear el archivo start.bat
@"
@echo off
cls
echo ============================================
echo   Experimento Plott ^& Sunder (1988)
echo ============================================
echo.

REM Crear _static si no existe
if not exist "_static" mkdir _static

REM Agregar al PATH temporalmente
set PATH=%PATH%;%APPDATA%\Python\Python310\Scripts

REM Verificar si otree está instalado
where otree >nul 2>&1
if errorlevel 1 (
    echo [ERROR] oTree no esta instalado
    echo Por favor ejecuta: pip install otree
    echo.
    pause
    exit /b 1
)

REM Resetear base de datos
echo Reseteando base de datos...
otree resetdb --noinput

REM Abrir navegador
start http://localhost:8000

REM Correr servidor
echo.
echo ============================================
echo   Servidor corriendo en http://localhost:8000
echo   Presiona Ctrl+C para detener
echo ============================================
echo.
otree devserver

pause
"@ | Out-File -FilePath "start.bat" -Encoding ASCII
