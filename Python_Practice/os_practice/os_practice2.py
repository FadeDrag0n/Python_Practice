import os
from dotenv import load_dotenv

load_dotenv('test.env')

# переменные окружения — это будет в каждом FastAPI проекте
print(os.getenv('DATABASE_URL', 'default_value'))
os.environ['MY_VAR'] = 'value'
debug = os.getenv('DEBUG', 'False')
print(debug)

# работа с путями — очень часто используется
os.path.join('folder', 'subfolder', 'file.txt')  # кроссплатформенный путь # Windows: folder\subfolder\file.txt
# Linux/Mac: folder/subfolder/file.txt
os.path.abspath('file.txt')  # абсолютный путь # → /home/fade/projects/myapp/file.txt
os.path.dirname('/home/user/file.txt')  # → /home/user
os.path.basename('/home/user/file.txt')  # → file.txt
os.path.splitext('file.txt')  # → ('file', '.txt')

name, ext = os.path.splitext('photo.jpg')
if ext in ('.jpg', '.png', '.webp'):
    print('это картинка')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)