# try:
#     f1 = open("C:/Users/Admin/Desktop/text1.txt","r")
#     text1 = f1.read()
#     user_input = int(input("Enter the number of pointer : "))
#     f2 = open("C:/Users/Admin/Desktop/text2.txt","r+")
#     f2.seek(user_input)
#     text2 = f2.write(text1)
#
# except Exception as e:
#     print("Exception : ",e)
# finally:
#     f1.close()
#     f2.close()
#     print("File close successfully")

try:
    file_control1 = open("C:/Users/Admin/Desktop/text1.txt", "w+")
    user_input = input("Input some text...")
    file_control1.write(user_input)
    file_control1.seek(0, 0)
    text = file_control1.read()
    pointer = int(input("Enter the number you want to point: "))
    file_control2 = open("C:/Users/Admin/Desktop/text2.txt","r+")
    file_control2.seek(pointer)
    file_control2.write(text)


except Exception as e:
    print("Exception",e)
finally:
    file_control1.close()
    file_control2.close()
    print("File closed successfully!")
