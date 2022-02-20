from common_settings import *
import subprocess

# logger name
logger = logging.getLogger("SYSFS")

class SYSFS:
    """
    sysfs gpio operation
    """
    gpio_x = '0' 
    gpio_y = '0'

    def __execute_command(self, command):

        results_output = ""

        results = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
        if results.returncode == 0:
            results_output = results.stdout.decode('utf-8')
        
        return results_output

    def setup(self, gpio_x, gpio_y):
        """
        setup gpio pins
        """
        try:

            if IsRPI_Device: # This fucntionality can't be verified as HW not present
                # X pin  Pin 11
                command_x = "echo 17 >/sys/class/gpio/export"
                self.__execute_command(command=command_x)
                # X pin  Pin 12
                command_y = "echo 18 >/sys/class/gpio/export"
                self.__execute_command(command=command_y)

                #set both to output pins
                command_x = "echo out >/sys/class/gpio/gpio17/direction"
                command_y = "echo out >/sys/class/gpio/gpio18/direction"
                self.__execute_command(command=command_x)
                self.__execute_command(command=command_y)

                #set arg values passed to program
                command_x = f'echo {gpio_x} > /sys/class/gpio/gpio17/value'
                command_x = f'echo {gpio_y} > /sys/class/gpio/gpio18/value'
                self.__execute_command(command=command_x)
                self.__execute_command(command=command_y)
            else:
                SYSFS.gpio_x = gpio_x
                SYSFS.gpio_y = gpio_y

        except Exception as e:
            logger.exception(f'Exception ocuured {str(e)}', exc_info=False)
            return False
        
        return True
    
    def get_gpio_y_value(self):
        """
        read the gpio value and return
        """
        status = False
        gpio_y_value = '0'
        try:
            if IsRPI_Device: # This fucntionality can't be verified as HW not present
                command_y = "cat /sys/class/gpio/gpio18/value"
                gpio_y_value = self.__execute_command(command=command_y)
                status = True
            else:
                gpio_y_value = SYSFS.gpio_y
                status = True
        except Exception as e:
            logger.exception(f'Exception ocuured {str(e)}', exc_info=False)
            return status, gpio_y_value
        logger.info(f'gpio_y = {gpio_y_value} is returned')
        return status, gpio_y_value
    
    def set_gpio_x_value(self, gpio_x):
        """
        write to gpio_x pin
        """
        status = False
        try:
            if IsRPI_Device: # This fucntionality can't be verified as HW not present
                command_x = f'echo 1 >/sys/class/gpio/gpio17/value'
                self.__execute_command(command=command_x)
                status = True
            else:
                SYSFS.gpio_x = gpio_x
                status = True
        except Exception as e:
            logger.exception(f'Exception ocuured {str(e)}', exc_info=False)
            return status
        
        logger.info(f'gpio_x = {gpio_x} is set')
        return status


    



