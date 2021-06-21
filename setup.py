import getopt
import sys
import os
from distutils.dir_util import copy_tree


WINDOWS_PATH = "C:\\Users\\user_name\\AppData\Roaming\\jupyter\\nbextensions"
LINUX_PATH = "/usr/local/share/jupyter/nbextensions/"


def setup(argv):
    opts, args = getopt.getopt(argv, "o:u:")
    oper_sys = 'linux'
    user_name = ''
    extension_name = 'runtime_plotter'
    for opt in opts:
        print(opt)
        if opt[0] == '-o':
            oper_sys = opt[1]
        elif opt[0] == '-u':
            user_name = opt[1]

    if 'win' in oper_sys.lower():
        win_path = WINDOWS_PATH.replace("user_name", user_name)
        path = win_path + "\\" + extension_name
        os.mkdir(path)
        copy_tree("runtime_plotter_extension", path)
    else:
        path = LINUX_PATH + extension_name
        os.mkdir(path)
        copy_tree("runtime_plotter_extension/", path)


if __name__ == "__main__":
    setup(sys.argv[1:])
