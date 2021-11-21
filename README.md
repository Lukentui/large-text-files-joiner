[![CodeFactor](https://www.codefactor.io/repository/github/lukentui/big-data-files-joiner/badge)](https://www.codefactor.io/repository/github/lukentui/big-data-files-joiner)

### Как использовать?
1. Поместите скрипт(main.py) в удобную Вам папку
2. Создайте в папке со скриптом папку `INPUT_TXT` и поместите туда текстовые файлы(.txt или иные) любых названий, все файлы
3. Запустите скрипт main.py с помощью Python 3

### Как оно работает?
Все файлы из папки `INPUT_TXT` соединяются в файл `_latest.txt`(в папке со скриптом main.py).

### Пример структуры файлов
- `main.py` : скрипт
- `_latest.txt` : файл с выводом, будет создан автоматически после первого запуска
- `INPUT_TXT` : папка с файлами для склейки
  - `base1.txt` : пример файла для склейки
  - `base2.txt` : пример файла для склейки
  - `mailpass.txt` : пример файла для склейки
