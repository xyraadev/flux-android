<<<<<<< HEAD
[app]
title = Flux Mobile
package.name = fluxmobile
package.domain = org.flux

version = 1.0
version.code = 1

source.dir = .
source.main = main.py

requirements = python3, kivy, openssl

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.minapi = 21
android.targetapi = 34

orientation = portrait

[buildozer]
log_level = 2
=======
[app]
# Название приложения
title = Flux Mobile
# Уникальное имя пакета (должно быть уникальным!)
package.name = fluxmobile
package.domain = org.flux

# Версия
version = 1.0
version.code = 1

# Главный файл
source.dir = .
source.main = main.py

# Требования
requirements = python3, kivy, openssl, requests

# Разрешения Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Минимальная версия Android
android.minapi = 21
# Целевая версия Android
android.targetapi = 34
# Разрешить аппаратное ускорение
android.allow_android_accelerated_rendering = True

# Иконка (можно добавить позже)
# icon.filename = %(source.dir)s/icon.png

# Ориентация экрана
orientation = portrait

# Настройки сборки
[buildozer]
# Уровень логов (2 = нормальный)
log_level = 2
# Папка для сборки
build_dir = .buildozer
# Папка для бинарников
bin_dir = ./bin

# Предупреждения
warn_on_root = 1
>>>>>>> a008b8df93bcf1c0d554764ed418ce90d94723a9
