import os

# переменные окружения — это будет в каждом FastAPI проекте
os.getenv('DATABASE_URL', 'default_value')
os.environ['MY_VAR'] = 'value'

# работа с путями — очень часто используется
os.path.join('folder', 'subfolder', 'file.txt')  # кроссплатформенный путь
os.path.abspath('file.txt')  # абсолютный путь
os.path.dirname('/home/user/file.txt')  # → /home/user
os.path.basename('/home/user/file.txt')  # → file.txt
os.path.splitext('file.txt')  # → ('file', '.txt')