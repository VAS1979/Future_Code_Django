echo off
cls
:: enter to venv
call venv\Scripts\activate.bat

:: start program
python .\app\manage.py runserver
echo project starting...
