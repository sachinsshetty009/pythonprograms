from common_settings import *
from sysfs_rpi import *
import getopt

# logger name
logger = logging.getLogger("MAIN")


def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:",["log"]) 
        gpio_x = -1
        gpio_y = -1
        for opt, arg in opts:
            if opt == '-i':
                gpio_x = arg
            elif opt == '-o':
                gpio_y = arg
            elif opt == "--log":
                set_logger_setting()
            else:
                raise()

        if gpio_x == -1 or gpio_y == -1:
            raise()
    except getopt.GetoptError:
      logger.error(f'-i <gpio_x_value> -o <gpio_y_value> (optional) --log')
      sys.exit(2)
    except Exception as e:
      logger.error(f'Either less arg or wrong arg')
      logger.error(f'-i <gpio_x_value> -o <gpio_y_value> (optional) --log')
      sys.exit(2)

    logger.info(f'gpio_x= {gpio_x} gpio_y= {gpio_y}')

    if (gpio_y == '0' or gpio_y == '1') and (gpio_x == '0' or gpio_x == '1'):
        sysfs_rpi_obj = SYSFS_RPI.getInstance()
        sysfs_rpi_obj.setup_sysfs_rpi_interface(gpio_x=gpio_x, gpio_y=gpio_y)
        if sysfs_rpi_obj.get_setup_status():
            sysfs_rpi_obj.toggle_gpio_x_value()
    else:
        logger.error(f'Value gpio(x/y) arg value error')

if __name__ == '__main__':
    main()




