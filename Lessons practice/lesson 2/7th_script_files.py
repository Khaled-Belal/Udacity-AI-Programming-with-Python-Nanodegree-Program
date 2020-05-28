f=open('text.txt','w')
f.write("hello!creating this file here!\n khaled is here")
f.close()

files = []
for i in range(10000):
    # with open('text.txt', 'r') as f:
        # files.append(f.read())
    # f=open('text.txt','r')
    # open('text.txt','r')
    # f.close()
    files.append(open('text.txt', 'r')) #too many handels
    print(i)
    # print(type(files[0]))
    # break