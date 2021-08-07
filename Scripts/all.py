import time

print("Running Everything")
exec(open('Scripts/compress.py').read())
time.sleep(2)
exec(open('Scripts/copy.py').read())
print("Finished")