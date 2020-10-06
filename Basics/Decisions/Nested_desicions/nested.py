print("What type of cover does the book have?")
btype=input()
if btype=="soft":
    print("Is the book perfect-bound?")
    bound=input()
    if bound=="yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
if btype=="hard":
    print("Books with hard covers can be more expensive!")

