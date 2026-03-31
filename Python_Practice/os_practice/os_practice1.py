import os

print(f'hello from {os.getcwd()}')
if not os.path.exists('New Folder'): #os.path.isdir('New Folder')
    os.mkdir('New Folder')

os.chdir('New Folder')
print(f'Current working directory: {os.getcwd()}')

if not os.path.exists('Folder1'):
    os.makedirs('Folder1/Folder2/Folder3')

os.chdir('..')
print(f'Current working directory: {os.getcwd()}')

# with open(f'New Folder/text.txt', 'w') as f:
#     for num in range(1, 101):
#         f.write(str(num) + '\n')
#
# os.rename('New Folder/text.txt', 'New Folder/New_text.txt')

os.chdir('New Folder')

if not os.path.exists('Folder1/New_text.txt'):
    os.replace('New_text.txt', 'Folder1/New_text.txt')

print(os.listdir("Folder1"))

os.chdir('..')

for dirpath, dir_names, filenames in os.walk('.'):
    for dir_name in dir_names:
        print(os.path.join(dirpath, dir_name))
    for file in filenames:
        print(os.path.join(dirpath, file))

# os.remove('New Folder/Delete_it.txt') delete file
# os.rmdir('New Folder/Delete_it') delete directory
# os.removedirs('New Folder/Delete_it') delete directory with directories

os.chdir('New Folder')
os.chdir('Folder1')

print(os.stat('New_text.txt'))
print(os.stat('New_text.txt')[6])
print(os.stat('New_text.txt').st_size)