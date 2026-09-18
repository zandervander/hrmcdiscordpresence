input("Hit enter to start the discord presence tool. No this is not malware, look at the code yourself.")
import subprocess
import sys

subprocess.Popen([sys.executable, "discordpresence-script.py"])

print("Discord presence script ran, opening visual app...")

from cmu_graphics import *
Label("HRMC | Discord Presence",200,200,size=20,fill='blue')
cmu_graphics.run()
