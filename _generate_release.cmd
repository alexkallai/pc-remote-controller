CALL .\venv\Scripts\activate.bat
cd src
py -m PyInstaller --uac-admin --distpath ".\..\_RELEASE" --workpath ".\..\_BUILD" -w -F --add-data "templates;templates" --add-data "static;static" --add-data "remote_icon.png;remote_icon.png" app.py