import sys
import logging
from common_settings import set_logger_setting
import getopt
from web_application import web_application_lauch

# logger name
logger = logging.getLogger("MAIN")

def main():

  set_logger_setting()
  web_application_lauch()

if __name__ == '__main__':
    main()