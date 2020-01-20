import os


def fun(dirs, files=[]):
    if os.path.isdir(dirs):
        for item in os.listdir(dirs):
            new_dir = os.path.join(dirs, item)
            fun(new_dir, files)
    else:
        files.append(dirs)
    return files


if __name__ == '__main__':
    x = fun(r'D:\t_src')
    print(x)
