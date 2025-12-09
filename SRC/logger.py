## logger is for the purpose that if any execution happens.
# we should be able to log all the info in some files
# so that we will be able to track if there is some errors,
#even the custom exception error, we will try to log that into
# the text file
import logging
import os

"""Imports the os module, which allows your program to interact 
with the operating system.

Used for:
Creating folders
Building file paths
Accessing current directories"""
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

""".strftime(...):- Converts date/time to a formatted string"""

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True) ##exist_ok = True means
# even there is already a directory or folder keep appending inside
# the folder.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

"""Level=logging.INFO
Sets the minimum severity level of messages that will be recorded.

Levels (lowest → highest):

Level	Meaning
DEBUG	Extra detailed messages
INFO	Normal operational messages
WARNING	Something may go wrong
ERROR	Something failed
CRITICAL	System crash / failure

Since you set INFO, anything INFO and above will be logged
 (INFO, WARNING, ERROR, CRITICAL)."""
##Checking if logger is working properly
'''if __name__ == "__main__":
    logging.info("Logging has started")
'''


## Now what our aim is when will get some exception, we will take
# that exception and use logging.info to put it inside the file