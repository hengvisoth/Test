# string = input("Enter a string")
file_name = input("Enter file name : ")
f = open(file_name)
read = f.readlines()
for i in read :

    if '"' in i:
        print(i)
    # if a.startswith("#"):
    #     print(a)
# a = read.strip('\n')
# print(a)
# for i in read :
#     if i.startswith("#"):
#         print(i)
# print(read)
# for i in read :
#     print(i)
    # if lines.startswith("#"):
    #     print(lines)

