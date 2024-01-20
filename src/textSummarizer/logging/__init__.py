import os
import sys
import logging

logging_str= "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
log_dir="logs"
log_file_path=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_file_path), #sends logging output to the diskfile
        logging.StreamHandler(sys.stdout)  #sends logging output to streams described path or file which supports write and flush methods
    ]
)

logger=logging.getLogger("textSummarizerlogger")