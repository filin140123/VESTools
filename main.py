import os

from settings import *
from click_shell import shell


@shell(prompt="vestools > ", intro="""Welcome to the VESTools!
Please enter a command down below. If you want to see a list of all avaliable commands, enter "help".\n""")
def vestools_shell():
    pass


@vestools_shell.command()
def help():
    print("""\nList of commands:
    
        --- Main commands ---
help        See this list
ytget       Mass YT videos download
imget       Mass images download
version     See version of VESTools
settings    See settings
exit        Exit the application

        --- Experimental ---
scenes      Cut videos into scenes
imgconv     Convert images into .png
""")


@vestools_shell.command()
def ytget():
    os.system("python ytget.py")


@vestools_shell.command()
def imget():
    os.system("python imget.py")


@vestools_shell.command()
def scenes():
    os.system("python scenecutter.py")


@vestools_shell.command()
def imgconv():
    os.system("python imgconv.py")


@vestools_shell.command()
def version():
    print()
    print(f"Current version:    {VERSION}")
    print()


@vestools_shell.command()
def settings():
    print()
    print(f"Directory for videos:    ./{DIRNAME}")
    print(f"Directory for images:    ./{IMGDIRNAME}")
    print(f"Default images amount:   {IMGDEFCOUNT} images")
    print()


if __name__ == "__main__":
    vestools_shell()
