@echo off
cd /d "%~dp0"
chcp 65001 >nul 2>&1

echo ============================================================
echo   Experimento Plott y Sunder (1988)
echo ============================================================
echo.

REM Verificar Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no encontrado
    echo Instala Python desde https://www.python.org
    pause
    exit /b 1
)
echo [OK] Python encontrado

REM Crear entorno virtual si no existe
if not exist "venv\Scripts\activate.bat" (
    echo.
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] No se pudo crear entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado

    echo [INFO] Instalando dependencias...
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip >nul 2>&1
    pip install otree >nul 2>&1
    echo [OK] Dependencias instaladas
) else (
    call venv\Scripts\activate.bat
)

echo [OK] Entorno activado

REM Crear _static si no existe
if not exist "_static" mkdir _static

REM Resetear base de datos
echo [INFO] Preparando base de datos...
venv\Scripts\otree.exe resetdb --noinput >nul 2>&1
echo [OK] Listo

echo.
echo [INFO] Iniciando servidor...
echo.

REM Abrir navegador despues de un delay
start "" cmd /c "timeout /t 3 /nobreak >nul && start http://localhost:8000"

echo ============================================================
echo   SERVIDOR CORRIENDO
echo ============================================================
echo.
echo   URL: http://localhost:8000
echo   Usuario: admin
echo   Contrasena: admin123
echo.
echo   Para DETENER: Cierra esta ventana
echo ============================================================
echo.

venv\Scripts\otree.exe devserver

pause
