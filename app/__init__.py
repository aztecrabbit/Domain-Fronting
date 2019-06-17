import os
from .domainfronting import domainfronting, domainfronting_handler
from .important import *
from .default import *
from .log import log, colors

os.system('cls' if os.name == 'nt' else 'clear')
print(colors(''.join(open(real_path('/data/banners.txt')).readlines())))
