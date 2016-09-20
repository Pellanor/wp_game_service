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


from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'


#from wp_game.app import app as application

