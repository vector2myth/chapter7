import os


'''
    run函数列举了当前目录下的所有文件，
    并蒋文件的列表作为字符串返回
'''
def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)
