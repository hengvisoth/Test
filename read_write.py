try :
    f = open("C:/Users/Admin/Desktop/KITpython/File_Handling/Test","r+")

    # read=f.read() # after it reads, pointer will stay at the end
    # print(read)
    # f.seek(1)
    f.seek(0,2)
    write = f.write("3") # pointer start at the beginning
except Exception as e :
    print(e)

