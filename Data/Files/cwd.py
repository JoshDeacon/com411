import os

def cwd():
    path = os.getcwd()
    print(f"Current Working Folder Path: {path}")

    for file in os.listdir(path):
        print(file)
        path=["path"]

def run():
    print("Processing...")
    cwd()
run()