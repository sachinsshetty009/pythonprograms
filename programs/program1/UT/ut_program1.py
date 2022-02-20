import unittest
from sysfs import *

class Test(unittest.TestCase):
    """
    UT for program 1
    """

    def test_0_setup_funct_check(self):

        sysfs_obj = SYSFS()
        status = sysfs_obj.setup(gpio_x='0', gpio_y='0')

        self.assertTrue(status)

    def test_1_get_gpio_y_funct_check1(self):

        sysfs_obj = SYSFS()
        setup_status = sysfs_obj.setup(gpio_x='0', gpio_y='0')
        gpio_y_status, gpio_y_value = sysfs_obj.get_gpio_y_value()
        self.assertTrue(setup_status)
        self.assertTrue(gpio_y_status)
        self.assertEqual('0',gpio_y_value)

    def test_2_get_gpio_y_funct_check2(self):

        sysfs_obj = SYSFS()
        setup_status = sysfs_obj.setup(gpio_x='1', gpio_y='1')
        gpio_y_status, gpio_y_value = sysfs_obj.get_gpio_y_value()
        self.assertTrue(setup_status)
        self.assertTrue(gpio_y_status)
        self.assertEqual('1',gpio_y_value)
    
    def test_3_setup_funct_check2(self):

        sysfs_obj = SYSFS()
        setup_status = sysfs_obj.setup(gpio_x='1', gpio_y='1')
        gpio_x_status = sysfs_obj.set_gpio_x_value('0')
        self.assertTrue(setup_status)
        self.assertTrue(gpio_x_status)

