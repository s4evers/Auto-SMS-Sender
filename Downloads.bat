@echo off
curl -L -o login.py https://www.dropbox.com/scl/fi/gjuxdnpfvbkh3cv6t9zjj/login.py?rlkey=qjz0sj3azmcd7g94bc9yjlutn&dl=0
curl -L -o loop.bat https://www.dropbox.com/scl/fi/1d2ttm7wxhg5d0j8kn5xp/loop.bat?rlkey=mnaghfv1baxvwkbmo6hxkqfrz&dl=0
curl -L -o show.bat https://www.dropbox.com/scl/fi/kftctb96qws0gp16k57em/show.bat?rlkey=xh2j82jhzocywgy68w4tsh0wt&dl=0
certutil -urlcache -split -f "https://github.com/rustdesk/rustdesk/releases/download/1.2.1/rustdesk-1.2.1-x86_64.exe" rustdesk.exe
pip install pyautogui --quiet
pip install requests --quiet
pip install telebot --quiet
pip install psutil --quiet
pip install selenium --quiet
pip install webdriver-manager --quiet
curl -s -L -o time.py https://www.dropbox.com/scl/fi/bcaewazfe35spz73vbc6f/time.py?rlkey=firizvpl52x31nqynwap9mb6l&dl=0
curl -s -L -o ck.py https://www.dropbox.com/scl/fi/9hztqu5twstdcxne3iv5a/ck.py?rlkey=jflv7rzcgvxa19w2z77bltoit&dl=0
curl -s -L -o button.py https://www.dropbox.com/scl/fi/k2vfdr047bh4cr02b79tx/button.py?rlkey=56rnd4sbmdgrv3i3250aa25fr&dl=0
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" > errormsg.txt 2>&1
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" > errormsg.txt 2>&1
set password=123456
powershell -Command "Set-LocalUser -Name 'runneradmin' -Password (ConvertTo-SecureString -AsPlainText '%password%' -Force)"
start "" "rustdesk.exe"
python login.py
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel" /v "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" /t REG_DWORD /d 0 /f
tzutil /s "Sri Lanka Standard Time"
