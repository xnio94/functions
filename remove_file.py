import os


def remove_file(file):
    try:
        os.remove(file)
    except:
        pass