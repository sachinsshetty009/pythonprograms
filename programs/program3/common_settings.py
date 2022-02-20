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
            logging.FileHandler("program3.log"),
            logging.StreamHandler(sys.stdout)
        ],
        format='%(asctime)-15s %(name)s line:%(lineno)d %(levelname)s %(message)s'
    )

# marking if a request is received on each port
visited_8080 = False
visited_8081 = False
visited_8082 = False