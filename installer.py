import os
import shutil

if not os.path.exists("C:/AVCDO-File"):
    os.mkdir("C:/AVCDO-File")
else:
    ...

current_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists("C:/AVCDO-File/Remember_To_Do"):
    shutil.copytree(current_path, "C:/AVCDO-File/Remember_To_Do")
    print("Installation was successful!")
else:
    print("An error occured, please contact Avo-Catto#6922 on discord")

input()
