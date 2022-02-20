import sys
import os
import logging

#RPI status
IsRPI_Device= False if os.environ["RPISTATUS"] == "False" else True

def set_logger_setting():
    """
    setting logger config
    """
    # logging setting
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("program1.log"),
            logging.StreamHandler(sys.stdout)
        ],
        format='%(asctime)-15s %(name)s line:%(lineno)d %(levelname)s %(message)s'
    )
