import time

print("Running Everything")
exec(open('Scripts/compress.py').read())
time.sleep(1)
exec(open('Scripts/copy.py').read())
print("Finished")