import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE = os.path.join(ROOT_DIR, "execution.log")
print(ROOT_DIR)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w'):
        pass