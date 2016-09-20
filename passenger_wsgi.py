import os
import sys

INTERP = os.path.expanduser('~/python.valsarn.com/venv/bin/python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# append current dir to module path
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + 'wp_game')
sys.path.append(cwd + '/venv/bin')

from wpgame.app import app as application
