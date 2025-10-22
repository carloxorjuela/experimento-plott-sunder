@echo off
echo Cerrando todos los servidores oTree...
taskkill /F /IM python.exe 2>nul
echo.
echo Todos los procesos Python han sido terminados.
echo Ahora puedes ejecutar: otree devserver
pause
