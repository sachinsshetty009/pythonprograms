import sys
import logging
from common_settings import set_logger_setting

# logger name
logger = logging.getLogger("MAIN")

def calculate_word_count(input_string):

    word_count_dict = dict()
    for word in input_string:
        logger.info(f'The word = {word}')
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + 1
        else:
            word_count_dict[word] = 1

    word_count_dict = dict(sorted(word_count_dict.items()))
    return word_count_dict

def print_word_dict(word_count_dict):

    logger.info(f'The word dict = {word_count_dict}')
    for word in word_count_dict.keys():
        print(f'{word}:{word_count_dict[word]}')

def main():

    set_logger_setting()

    logger.info(f'Arg len = {len(sys.argv)}')
    logger.info(f'Arg list = {str(sys.argv)}')

    if len(sys.argv) == 1:
        logger.error(f' -i <gpio_x_value> -o <gpio_y_value> (optional) --log')
        sys.exit(2)

    word_count_dict = calculate_word_count(input_string=sys.argv[1:])

    print_word_dict(word_count_dict)

if __name__ == '__main__':
    main()