import shutil

def center(msg):
    print(msg.center(shutil.get_terminal_size().columns))