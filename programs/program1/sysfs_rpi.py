import time
from common_settings import *
from sysfs import *

# logger name
logger = logging.getLogger("SYSFS RPI")

class SYSFS_RPI:
    """
    An interface for querying GPIO X and Y pins
    """
    __sysfs_rpi_instance = None
    sysfs_obj = None

    @staticmethod
    def getInstance():
        """
        One instance created for GPIO SYSFS interface
        """
        if SYSFS_RPI.__sysfs_rpi_instance is None:
            SYSFS_RPI.__sysfs_rpi_instance = SYSFS_RPI.__new__(SYSFS_RPI)
        return SYSFS_RPI.__sysfs_rpi_instance
    
    def __init__(self):
        raise Exception('Call getInstance')

    def setup_sysfs_rpi_interface(self, gpio_x, gpio_y):
        """
        Interface for setting X and Y pins
        """
        sysfs_obj = SYSFS()
        if sysfs_obj.setup(gpio_x=gpio_x, gpio_y=gpio_y):
            SYSFS_RPI.sysfs_obj = sysfs_obj
            logger.info("Setup sucess")
        else:
            logger.error(f'Operation faied with error')
    
    def get_setup_status(self):

        if SYSFS_RPI.sysfs_obj != None:
            logger.info("SYSFS_RPI.sysfs_obj not None")
            return True
        else:
            logger.error("SYSFS_RPI.sysfs_obj is None")
            return False

    def toggle_gpio_x_value(self):
        """
        1) if gpio Y is in HIGH then gpio X need to be toggled this way (LOW-HIGH-LOW-HIGH...) every 1 second
        2) if gpio Y is LOW, gpio X should remain in LOW as well
        """

        if self.get_setup_status():
            gpio_y_status, gpio_y_value = SYSFS_RPI.sysfs_obj.get_gpio_y_value()
            if gpio_y_status and gpio_y_value == '1': # condition (1)
                while True: # event loop
                    if SYSFS_RPI.sysfs_obj.set_gpio_x_value('0'): # LOW
                        logger.info("gpio <Y> HIGH gpio <X> LOW")
                        print("** gpio <Y> HIGH gpio <X> LOW **")
                    time.sleep(1)
                    if SYSFS_RPI.sysfs_obj.set_gpio_x_value('1'): # HIGH
                        logger.info("gpio <Y> HIGH gpio <X> HIGH")
                        print("** gpio <Y> HIGH gpio <X> HIGH **")
                    time.sleep(1)
            elif gpio_y_status and gpio_y_value == '0': # condition (2)
                if SYSFS_RPI.sysfs_obj.set_gpio_x_value('0'): # first LOW
                    logger.info("gpio <Y> LOW gpio <X> LOW")
                    print("** gpio <Y> LOW gpio <X> LOW **")
            else:
                logger.error(f'gpio_y_status = {gpio_y_status} and gpio_y_value = {gpio_y_value} error')
        else:
            logger.error(f'Either SYSFS_RPI.sysfs_obj = None')