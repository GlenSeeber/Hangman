#funcs
def convert(string):
    li = list(string.split('\n\n'))
    return li

#run
f = open('image.txt', 'r')
myDoc = f.read()
f.close()

myDoc = convert(myDoc)
for i in myDoc:
    print(i)
