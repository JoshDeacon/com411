file_path = ("C:/Users/User/OneDrive - Solent University/Year 1/com411-1/Data/Files/txt/books.txt")
wd=("C:/Users/User/OneDrive - Solent University/Year 1/com411-1/Data/Files/txt")

def search(fname):
    print("Searching...", end="")
    sections_list = []
    books_list = []
    with open(fname) as file:
        for line in file:
            if line.startswith("Section"):
                sections_list.append(line.split(":"))
            else:
                books_list.append(line)
    print("Done!")
    tuple_list=(sections_list, books_list)
    return tuple_list

def save(fname, tuple_list):
    print("Saving...", end="")
    with open(fname, "w") as writing:
        writing.write("Sections:")
        for sections_list in tuple_list[0]: 
            writing.write(str(sections_list)+", ")
        writing.write("Books:")
        for books_list in tuple_list[1]: 
            writing.write(str(books_list)+", ")
    print("Done!")

   
def run():
    data=search(file_path)
    save(wd+"/section-books.txt",data)
run()