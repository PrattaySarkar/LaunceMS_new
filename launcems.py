#
# ╔══════════════════════════════════╗
# ║  LaunceMS_New By Prattay Sarkar  ║
# ║   aka. PrattaySarkar On Github   ║
# ╚══════════════════════════════════╝
#

import configparser
from colorama import Fore
from flask import Flask, render_template

print(Fore.GREEN + "╔══════════╣ LaunceMS Server ╠══════════╗")
print(Fore.GREEN + "║+-       Made Proudly In India       -+║")
print(Fore.GREEN + "║+-       By Prattay Sarkar, WB       -+║")
print(Fore.GREEN + "╚═══════════════════════════════════════╝\n")
print(Fore.YELLOW + "|+- Trying To Start LaunceMS Dev Server...")

app = Flask(__name__, template_folder="HTML")


# ══════════════╣  USER AREA  ╠════════════════

@app.route('/')
def index():
    return render_template('index.html')


# ═════════════════════════════════════════════

if __name__ == '__main__':
    print(Fore.BLUE + "|+- Switching To Flask Output For Error Checking...\n")
    app.run(host='0.0.0.0', port=8080)
