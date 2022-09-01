@Echo Off
chcp 65001 
COLOR 70
:a
cls
Set /a _rand=(%RANDOM%*100/32768)+1
Echo : %_rand%
set /p c="Un autre ? O/N? "
if "%c%"=="O" goto a
if "%c%"=="o" goto a
exit