import subprocess
import os

cmd = ['7z', 'a', '../out/MinimlistArmorPack-1.16.5.zip', 'assets', 'pack.mcmeta', 'pack.png']

def current_path():
    print("Current working directory")
    print(os.getcwd())
    print()
    
def compress():
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    print("Resource Pack Compressed to /out")


os.chdir('../1.16.5/')
compress()

