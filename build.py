import time
import subprocess
required_libraries = ['requests', 'tqdm']
import sys


print('███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗')
print('███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗')
print('████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██║     ██║██╔════╝ ██║  ██║╚══██╔══╝')
print('██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║██║     ██║██║  ███╗███████║   ██║   ')  
print('██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██║     ██║██║   ██║██╔══██║   ██║   ')  
print('██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗██║╚██████╔╝██║  ██║   ██║   ') 
print('╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ')  
print('Moonlight V1 | LeopardenGames ©')
print('you can change settings in the "conf" data')
print("Starting...")
time.sleep(3)
def install_package(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
for library in required_libraries:
    install_package(library)
    
print("##########")
print("# Sucess #")
print("##########")

import requests
from tqdm import tqdm

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


github_url = 'https://raw.githubusercontent.com/LeopardenGames/LeopardenGames/main/down1.py'
local_save_path = 'dev/down1.py'

download_from_github(github_url, local_save_path)
