# VESTools: Video Editing Scripts and Tools

## :uk: English Version

**NEW!** — VESTools avaliable as shell application! Just launch `main.py`

**ytget.py** — Mass uploading of videos from YouTube with sound and the highest possible resolution. You can cut videos into scenes if you want

**imget.py** — Mass uploading of images from Google Images with options. All pictures will be converted to `.png` format

Image conversion or video cutting can be done directly with the `imgconv.py` and `scenecutter.py` scripts.

You can tweak some attributes in `settings.py` file.

_For **Windows** only (for now)_

### Requirements:
Run `!installreqs.py` OR

- **requests**, **click-shell**, **pillow**, **pytube**, **scenedetect**, **imagesize**: run `pip install click-shell pillow pytube scenedetect imagesize` in a terminal
- **ffmpeg**: download the archive from the official site, then find `ffmpeg.exe` in it, put it in a directory of your choice, then run `set PATH=%PATH%;C:/your/dir/here` in a terminal


## :ru: Русская версия

**NEW!** — VESTools доступны как приложение для командной строки! Просто запустите `main.py`

**ytget.py** — массовая загрузка видео с YouTube со звуком и максимально возможным разрешением. Есть функция нарезки видео на сцены по желанию

**imget.py** — массовая загрузка изображений по нескольким запросам из Google Images с опциями. Все фото конвертируются в формат `.png`

Конвертация изображений или нарезка видео может быть выполнена непосредственно с помощью скриптов `imgconv.py` и `scenecutter.py`.

Вы можете настроить некоторые атрибуты в файле `settings.py`.

_Только для **Windows** (пока что)_

### Требования:
Запустите `!installreqs.py` ИЛИ

- **requests**, **click-shell**, **pillow**, **pytube**, **scenedetect**, **imagesize**: запустите `!installreqs.bat` ИЛИ выполните `pip install requests click-shell pillow pytube scenedetect imagesize` в терминале
- **ffmpeg**: скачайте архив с официального сайта, затем найдите там `ffmpeg.exe`, поместите его в директорию на ваш выбор, затем выполните `set PATH=%PATH%;C:/ваша/директория` в терминале

