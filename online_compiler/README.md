# PHP
## Базовая команда
```php
<?php
echo "11";
echo file_get_contents('/home/app/test/nlthas.php');
echo "22";
?>
```

---

## php.ini
В php.ini есть запрещенные к выполнению функции,
но `file_get_contents()` среди них нет.

В `disable_functions` есть:
- opendir, file_exists, is_writable, is_file, и пр.
- file_put_contents и пр.
- [Все функции для работы с файловой системой](https://www.php.net/manual/en/ref.filesystem.php)
(кроме `file_get_contents()`)

Доступные функции:
- var_dump
- print_r
- eval

### Cписок доступных функций
Как пользоваться:
- `make` - сгенерировать `all+.txt` и `available.txt`.
- `make clean` - убрать `all+.txt` и `available.txt`.

Файлы:
- `all.txt` - с
[оф. сайта](https://www.php.net/manual/en/indexes.functions.php)
- `all+.txt` - с сайта + запрещенные
- `available.txt` - не запрещенные

---

## file_get_contents()
Работает только в `/home/app/test/`
(почему - строка 318 php.ini)

Не работает с:
- /etc/passwd
- /nlthas.php
- nlthas.php
- file:///etc/passwd
- /home/app/.bashrc
- /home/app/app.py
- /home/app/test/app.py
- /usr/lib/python3.9/unittest/__main__.py

Работает с:
- /home/app/test/свой_файл.php
- file:///home/app/test/свой_файл.php
- http://www.example.com/

### get_defined_functions()
Не выдает eval, но eval работает

### eval()
Работает
```php
<?php
echo "11 ";
eval("echo file_get_contents('/home/app/test/eholos.php');");
echo " 22";
?>
```

---


# app.py
- Нельзя предсказать random
- Запустил сервис у себя, сделаю docker, если кому-то надо будет


# def compile() (часть с питоном)

## Popen()
Popen() выполняет первый аргумент **через шелл**.
Если через `check_file()` протолкнуть

`filename = '-c 2+2; whoami; #py'`,

то таск решен.

---

- Для питона другая папка: `/home/app/testpy/` вместо `/home/app/test/`

---

## Можно запустить любой файл на питоне:
- `check_file()` проверяет один файл, а запускается другой,
  так как CWD не в `/home/app/test/`
- `cd ../` работает в /
- `../../../` выравнивает `'/home/app/testpy/'+filename` и `filename`,
так что `check_file()` проверяет тот файл, который потом запустится

```bash
curl 'http://onlinecompiler.2021.3k.ctf.to:5000/compile' \
  --data-raw 'c_type=python&filename=../../../usr/lib/python3.8/unittest/__main__.py'
```

### Ответы:
- noop - файл должен оканчиваться на 'py'
- failed - файла не существует
- <пусто>, или что-то еще - файл был запущен

---

### Запуск папки
- Можно запустить папку, если в ней есть `__main__.py`
- Нельзя запустить папку, если в ней есть `__main__`
- Папка `/home/app/testpy` не запускается
