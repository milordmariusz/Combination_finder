@echo off
setlocal enabledelayedexpansion

:menu
echo. " _____           _               _        _                   _     _                  _ _ "
echo. "/  ___|         | |             (_)      | |                 | |   (_)                (_|_)"
echo. "\ `--. _____   _| | ____ _ _ __  _  ___  | | _____  _ __ ___ | |__  _ _ __   __ _  ___ _ _ "
echo. " `--. \_  / | | | |/ / _` | '_ \| |/ _ \ | |/ / _ \| '_ ` _ \| '_ \| | '_ \ / _` |/ __| | |"
echo. "/\__/ // /| |_| |   < (_| | | | | |  __/ |   < (_) | | | | | | |_) | | | | | (_| | (__| | |"
echo. "\____//___|\__,_|_|\_\__,_|_| |_|_|\___| |_|\_\___/|_| |_| |_|_.__/|_|_| |_|\__,_|\___| |_|"
echo. "                                                                                     _/ |  "
echo. "                                                                                    |__/   "
echo.                                        =================
echo.                                          1. Start
echo.                                          2. Informacje
echo.                                          3. Backup
echo.                                          4. Zakoncz
echo.                                        =================

set /p input=Wybierz opcje: 
if %input% EQU 1 goto start
if %input% EQU 2 goto info
if %input% EQU 3 goto backup
if %input% EQU 4 (
    exit
) else (
    cls
    goto menu
) 

:start
python app.py
python web.py
set /p c=Nacisnij enter
cls 
goto menu

:info 
echo.
echo Program rozbija liczbe naturalna na wszystkie mozliwe kombinacje sum ktore daja jako wynik podana liczbe.
echo Program pobiera dane wejsciowe z pliku appIn.txt.
echo Efekt pierwszego skryptu jest zapisywany w pliku appOut.txt ktory jest nastepniezamieniany na strone internetowa.
echo.
echo Autor: Mariusz Wrobel
echo.
set /p c=Nacisnij enter
cls 
goto menu

:backup
set czas=%time:~0,8%
set czas=%czas::=.%
set name=Backup-%date%-%czas%
mkdir backup\%name%
copy "*.*" "backup\%name%" > nul
echo.
echo Backup zostal zapisany w folderze backup pod nazwa: %name%
echo.
set /p c=Nacisnij enter
cls 
goto menu

pause