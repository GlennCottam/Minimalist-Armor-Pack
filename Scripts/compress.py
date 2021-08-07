import subprocess
import os

vr = "1.16.5/"
cmd = ['7z', 'a', 'out/MinimalistArmorPack-1.16.5.zip', vr + 'assets', vr + 'pack.mcmeta', vr + 'pack.png']

def current_path():
    print("Current working directory")
    print(os.getcwd())
    print()
    
def compress():
    print("Running Command: ", cmd)
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    print("Resource Pack Compressed to /out")

compress()


