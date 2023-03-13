from datetime import datetime
from setup import Config
import os


class Logger:

    def __init__(self):
        self.filename = 'debug.log'
        self.file_path = 'logs/'
        self.env = Config.DEBUG_MODE

    def log(self, message):
        if int(self.env):
            message = str(datetime.utcnow()) + " " + message + '\n'
            print(message)
            file_logger = open(self.file_path+self.filename, 'a')
            file_logger.writelines(message)
            file_logger.close()
