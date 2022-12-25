activate () {
    ./venv/bin/activate
}
cd src
./../venv/bin/python3 -m PyInstaller --distpath "./../_LINUX_RELEASE" --workpath "./../_LINUX_BUILD" -w -F --add-data "templates:templates" --add-data "static:static" --add-data "remote_icon.png:." app.py
cp ./../settings.cfg ./../_LINUX_RELEASE/settings.cfg