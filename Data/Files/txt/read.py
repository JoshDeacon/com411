file_path = ("C:/Users/User/OneDrive - Solent University/Year 1/com411-1/Data/Files/txt/locations.txt")

def search(fname):
    print("Searching...")
    with open(fname) as file:
        for line in file:
            print(f"Looked in {line}",end="")
    print("\n")
    print("...Done!")
    
def run():
    search(file_path)
run()