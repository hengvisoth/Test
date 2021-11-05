
try:
    f = open('C:/Users/Admin/Desktop/KITpython/File_Handling/asd',"w")

    f.write('Studentttt hello ')

except:
    print("There is no directory or file")
finally:
    f.close()
    print("File close successfully")
