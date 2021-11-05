try:
    f = open("C:/Users/Admin/Desktop/KITpython/File_Handling/Test","a")
    text ='New testing'
    f.write(text)
except:
    print("There is no directory or file")
finally:
    f.close()
    print("File close successfully")
