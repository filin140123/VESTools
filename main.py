"""
Main file aka shell
"""

import os

from click_shell import shell

import settings as st


@shell(prompt="vestools > ", intro="""Welcome to the VESTools!
Please enter a command down below. Enter "help" to see a list of all avaliable commands.\n""")
def vestools_shell():
    """
    Init shell
    :return: None
    """
    pass


@vestools_shell.command()
def help() -> None:
    """
    Prints help
    :return: None
    """
    print("""\nList of commands:
    
        --- Main commands ---
help        See this list
ytget       Mass YT videos download
imget       Mass images download
auget       Mass audio extractor
version     See version of VESTools
settings    See settings
getreqs     Refresh all requirments
exit        Exit the application

        --- Experimental ---
scenes      Cut videos into scenes
imgconv     Convert images into .png
oldimget    Mass images download (old version)
            in case if imget not working 
""")


@vestools_shell.command()
def ytget():
    """
    Launch ytget.py
    :return: None
    """
    os.system("python ytget.py")


@vestools_shell.command()
def oldimget():
    """
    Launch oldimget.py
    :return: None
    """
    os.system("python oldimget.py")


@vestools_shell.command()
def imget():
    """
    Launch imget.py
    :return: None
    """
    os.system("python imget.py")


@vestools_shell.command()
def scenes():
    """
    Launch scenecutter.py
    :return: None
    """
    os.system("python scenecutter.py")


@vestools_shell.command()
def imgconv():
    """
    Launch imgconv.py
    :return: None
    """
    os.system("python imgconv.py")


@vestools_shell.command()
def getreqs():
    """
    Launch getreqs.py
    :return: None
    """
    os.system("python getreqs.py")


@vestools_shell.command()
def auget():
    """
    Launch auget.py
    :return: None
    """
    os.system("python auget.py")


@vestools_shell.command()
def version():
    """
    Prints current version
    :return: None
    """
    print(f"\nCurrent version:    {st.VERSION}\n")

@vestools_shell.command()
def settings():
    """
    Prints settings
    :return: None
    """
    print()
    print(f"Directory for videos:    ./{st.DIRNAME}/")
    print(f"Directory for images:    ./{st.IMGDIRNAME}/")
    print(f"Directory for audio:     ./{st.AUDIRNAME}/")
    print(f"Default images amount:   {st.IMGDEFCOUNT} images")
    print()


if __name__ == "__main__":
    vestools_shell()
