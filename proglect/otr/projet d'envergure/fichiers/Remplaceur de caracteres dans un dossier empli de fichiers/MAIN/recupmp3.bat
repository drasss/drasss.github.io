@echo off 
chcp 65001
dir ..\%1 /B>recup.txt
chcp 1252
exit