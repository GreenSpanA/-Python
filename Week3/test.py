import os.path
from solution import File
path_to_file = 'some_filename.txt'


os.path.exists(path_to_file) # False

file_obj = File(path_to_file)
os.path.exists(path_to_file) #True
print(file_obj)

file_obj.read() #''

file_obj.write('some text') #9

file_obj.read() #somne text


file_obj.write('other text') #10

file_obj.read()  #other text

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n') #7
file_obj_2.write('line 2\n') #7

new_file_obj = file_obj_1 + file_obj_2
isinstance(new_file_obj, File) #True

print(new_file_obj) #C:\Users\Media\AppData\Local\Temp\71b9e7b695f64d85a7488f07f2bc051c\

for line in new_file_obj:
    print(ascii(line))  
'''    
'line 1\n'
'line 2\n'
'''

