CALL .\venv\Scripts\activate.bat
cd src
py -m PyInstaller --uac-admin --distpath ".\..\_WINDOWS_RELEASE" --workpath ".\..\_WINDOWS_BUILD" -w -F --add-data "templates;templates" --add-data "static;static" --add-data "remote_icon.png;." app.py
cd ..
copy .\settings.cfg .\_WINDOWS_RELEASE\