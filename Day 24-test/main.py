# with open("my_file.txt") as whatever:
#     contents = whatever.read()
#     print(contents)

# with open("my_file.txt", mode="a") as whatever:   #add to file
#     whatever.write("    New text")

# with open("my_file.txt", mode="w") as whatever:     #write to file but clear everythin
#     whatever.write("    New text")

with open("../Desktop/my_file.txt") as whatever:     #append to file
    contents = whatever.read()
    print(contents)