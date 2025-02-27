import os
import sys
from PyInstaller.__main__ import run

def build_app():
    # 设置打包参数
    options = [
        '--name=dycap',  # 设置打包后的应用程序名称
        '--onefile',  # 打包为单个可执行文件
        # '--windowed',  # 不显示命令行窗口
        '--add-data=source;source',  # 添加需要打包的文件夹及其相对路径
        # 可以添加更多的文件夹，格式为'--add-data=源文件夹;目标文件夹'
    ]

    # 拼接打包命令
    args = ['dycap.py','__init__.py'] + options

    # 执行打包命令
    run(args)

if __name__ == '__main__':
    build_app()