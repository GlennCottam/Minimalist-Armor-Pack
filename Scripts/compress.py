import subprocess
import os
vr = "1.16.5/"
cmd = ['7z', 'a', '../out/MinimalistArmorPack.zip', 'assets', 'pack.mcmeta', 'pack.png']

def current_path():
    print("Current working directory")
    print(os.getcwd())
    print()
    
def compress():
    print("Running Command: ", cmd)
    os.chdir(vr)
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    os.chdir('../')
    print("Resource Pack Compressed to /out")

compress()


