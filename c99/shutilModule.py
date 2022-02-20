import shutil
import os

path = 'C:/Users/shish/OneDrive/Desktop/shishir/c99/newFolder'

print("Before copying file: ")
print(os.listdir(path))

'''
#copying the file
source =  'C:/Users/shish/OneDrive/Desktop/shishir/c99/newFolder/file1.txt'

destination = 'C:/Users/shish/OneDrive/Desktop/shishir/c99/newFolder/file2.txt'


dest = shutil.copy(source,destination)
'''
#moving the file
source =  'C:/Users/shish/OneDrive/Desktop/shishir/c99/newFolder'

destination = 'C:/Users/shish/OneDrive/Desktop/shishir/c99/newFolder1'


dest = shutil.move(source,destination)



print("After copying file: ")
print(os.listdir(path))
