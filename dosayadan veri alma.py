import os
path="C:\\Users\\feridun\\Desktop\\dnm.txt"
if os.path.exists(path):
    print("txt is exists")
    if os.path.isfile(path):
        print("that is  a file")
else:
    print("no txt file")
with open("C:\\Users\\feridun\Desktop\\dnm.txt","r+") as file:
    file.write("ben messi\n")
    print(file.read())

 