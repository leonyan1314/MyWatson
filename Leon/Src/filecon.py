with open("test.log","r") as content:
   print( content.read())


'''myfile = open("test.log", "r")
try:
    myfile.write("this is a %s time insert\n")
    print(myfile.read())
except IOError as e:
    print(e)
finally:
    myfile.close()

myfile1=open("test.log","r")
print(myfile1.read())
myfile1.close()
for i in myfile :
    if "html" in i:
        print("this is le")
        '''