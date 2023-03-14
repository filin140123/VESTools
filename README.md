# VESTools: Video Editing Scripts and Tools

## :uk: English Version

**NEW!** — VESTools avaliable as shell application! Just launch `main.py`

**ytget.py** — Mass uploading of videos from YouTube with sound and the highest possible resolution. You can cut videos into scenes if you want

**imget.py** — Mass uploading of images from Google Images with options. All pictures will be converted to `.png` format

Image conversion or video cutting can be done directly with the `imgconv.py` and `scenecutter.py` scripts.

You can tweak some attributes in `settings.py` file.

_For **Windows** only (for now)_

### Requirements:
Launch `getreqs.py` or do installation yourself:

#### Python Packages

Run in a terminal:
```cmd
pip install click-shell pillow pytube scenedetect imagesize google_images_download
```

#### FFMPEG

Download the archive from the official site, then find `ffmpeg.exe` in `/bin` folder, put it in a directory of your choice, then run in a terminal:
```cmd
set PATH=%PATH%;C:/your/dir/here
```

#### Fixing google_images_download

You need to fix `google_images_download` package.

- Download this file: [GitHub Link](https://github.com/Joeclinton1/google-images-download/raw/patch-1/google_images_download/google_images_download.py)
- Go to: `C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\YOUR_PYTHON_VERSION_HERE\Lib\site-packages\google_images_download`
- Replace `google_images_download.py` with file that you get earlier and open it in code editor
- Replace 407 line (`info = data[11]`) with `info = data[23]` and save

## :ru: Русская версия

**NEW!** — VESTools доступны как приложение для командной строки! Просто запустите `main.py`

**ytget.py** — массовая загрузка видео с YouTube со звуком и максимально возможным разрешением. Есть функция нарезки видео на сцены по желанию

**imget.py** — массовая загрузка изображений по нескольким запросам из Google Images с опциями. Все фото конвертируются в формат `.png`

Конвертация изображений или нарезка видео может быть выполнена непосредственно с помощью скриптов `imgconv.py` и `scenecutter.py`.

Вы можете настроить некоторые атрибуты в файле `settings.py`.

_Только для **Windows** (пока что)_

### Требования:
Запустите `getreqs.py` или настройте все сами:

#### Пакеты Python

Выполните в терминале:
```cmd
pip install click-shell pillow pytube scenedetect imagesize google_images_download
```

#### FFMPEG

Скачайте архив с официального сайта, затем найдите там `ffmpeg.exe` в папке `bin`, поместите его в директорию на ваш выбор, затем выполните в терминале:
```cmd
set PATH=%PATH%;C:/your/dir/here
```

#### Чиним пакет google_images_download

Нужно исправить пакет `google_images_download`.

- Скачайте файл: [GitHub Link](https://github.com/Joeclinton1/google-images-download/raw/patch-1/google_images_download/google_images_download.py)
- Перейдите сюда: `C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\YOUR_PYTHON_VERSION_HERE\Lib\site-packages\google_images_download`
- Замените `google_images_download.py` файлом, который вы скачали ранее и откройте его в редакторе кода
- Замените 407-ую строку (`info = data[11]`) на `info = data[23]` и сохраните файл
