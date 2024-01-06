import time
import sys
import subprocess
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
    
def colored_text(text, color_code):
    return f"{color_code}{text}{Colors.RESET}"




print('Installing')
time.sleep(3)
def install_package(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Beispiel: Automatische Installation von Bibliotheken
required_libraries = ['requests', 'tqdm']

for library in required_libraries:
    install_package(library)
    
print('')
print('')
import requests
from tqdm import tqdm  # Fortschrittsbalken-Anzeige, optional

def download_from_github(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(save_path, 'wb') as file, tqdm(
        desc=save_path,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            bar.update(len(data))
            file.write(data)

github_url = 'https://raw.githubusercontent.com/beeware/cricket/main/setup.py'
local_save_path = 'dev/down1.py'

download_from_github(github_url, local_save_path)
print(colored_text("Install Sucess!", Colors.GREEN))
time.sleep(1)
print(colored_text("Bitte Warten, die Instalation wird Abgeschlossen! Dies könnte einen Moment dauern! Bitte Schließen sie dieses Fenster Nicht!", Colors.GREEN))
time.sleep(5)
sys.exit()
