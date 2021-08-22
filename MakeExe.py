from main import VERSION
import os
os.system(f'pyinstaller main.py -w -n 贪吃蛇{VERSION} -i ico\\icon.ico')