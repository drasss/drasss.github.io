@echo off
:start
set /p nom="quel est le nom de ton dossier utilisateur ? (celui ou il y a minecraft) "  
if C:\Users\%nom%\AppData\Roaming\.minecraft\saves EXISTS goto oui
:oui
copy 
exit