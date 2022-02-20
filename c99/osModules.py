import os

#check the system date
#print(os.system('date'))

#create a new  folder
#os.mkdir("newFolder1")

#check current working directory
#print(os.getcwd())


#check if a file exists
'''path = 'C:/Users/shish/OneDrive/Desktop/shishir/c98/modules.py'
exists = os.path.exists(path)
print(exists)'''


#split the folder and the extension
#path = 'C:/Users/shish/OneDrive/Desktop/shishir/c99/modules.py'
#rootExt = os.path.splitext(path)

#print('root part: ',rootExt[0])
#print('ext part: ',rootExt[1])

#list all the files and folders


print(os.listdir())