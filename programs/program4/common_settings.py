import sys
import logging

def set_logger_setting():
    """
    setting logger config
    """
    # logging setting
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("program4.log"),
            logging.StreamHandler(sys.stdout)
        ],
        format='%(asctime)-15s %(name)s line:%(lineno)d %(levelname)s %(message)s'
    )
