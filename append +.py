try:
    f = open("C:/Users/Admin/Desktop/KITpython/File_Handling/Test","a+")
    read = f.read()
    print(read)
    write = f.write("New testingggggggg")
except:
    print("There is no directory or file")
finally:
    f.close()
    print("File close successfully")
