import os, sys

sys.path = ['/var/www/ha'] + sys.path
import bottle
#sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

import app
#from app import app

application = bottle.default_app()
