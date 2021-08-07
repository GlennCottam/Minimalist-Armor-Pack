import subprocess
import os
import shutil

to = 'C:/Users/glenn/curseforge/minecraft/Instances/Minimalist_Armor_Testing/resourcepacks/MinimalistArmorPack-1.16.5.zip'

def current_path():
    print("Current working directory")
    print(os.getcwd())
    print()

def copy():
    print("Copying resource pack to: " + to)
    shutil.copy('./out/MinimalistArmorPack-1.16.5.zip', to)
    print("Copy finished")

copy()
