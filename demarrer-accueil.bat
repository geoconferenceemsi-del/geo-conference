@echo off
cd /d "%~dp0"
start "" http://localhost:8080/accueil.html
python -m http.server 8080 --bind 0.0.0.0
pause
