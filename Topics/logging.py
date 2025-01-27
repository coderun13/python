#Logging: Used to log information(like errors)

import logging
import os

#create a logger object
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok =True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)
#path = LOG_DIR+ "/"+LOG_FILE_NAME
# print(log_path)

logging.basicConfig(
    filename=log_path,
    format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

logging.info("Hello world")
