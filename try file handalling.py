# To read files and display
# f=open("log.txt",'r')
# c=f.readline()
# a=f.readlines()
# print(c)
# print(a)
# f.close

# To over write word from inside cotation
# f=open("log.txt",'w')
# f.writelines('ram')
# f.close

# To add the list
# list=['ram','shyam','hari']
# f=open("log.txt",'w')
# f.writelines(list)
# f.close

# x create new file if not exist
# list=['ram','shyam','hari']
# f=open("lopg.txt",'x')
# f.writelines(list)
# f.close

# r+ help to read and write
# f=open("log.txt",'r+')
# c=f.readline()
# print(c)
# f.write("python")
# a=f.read()
# print(a)
# f.close

# f=open('log.txt','a+')
# # f.write('programming')
# f.seek(3)
# c=f.read()
# print(c)
# f.close


# if mode not given then it is read mode
# with open('log.txt') as f:
#     data=f.read()
#     print(data)
# print(f.close)

# f=open('log.txt',mode='r')
# print("File name:",f.name)
# print("File mode:",f.name)
# print("File readable:",f.readable)
# print("File wiryable:",f.writable)
# print("file close:",f.closed)
# f.close()
# print("File closed: ",f.closed)


# this is to copy info of one file to another
# f=open("log.txt",'r')
# c=f.read()
# f1=open('log2.txt','w')
# f1.write(c)
# f.close()
# f1.close()

# import pickle
# f=open('log.txt','rb')
# # doc={"1":"ram","2":"hari"}
# c=pickle.load(f)
# print(c)
# f.close

import pickle
a=['ram','shyam']
c=pickle.dumps(a)
print(c)
d=pickle.loads(c)
print(d)
a.close