from common_settings import *
import getopt
import json
import os
import operator

# logger name
logger = logging.getLogger("MAIN")

class MyException(Exception):
    pass

def sort_values(record_list):
    return sorted(sorted(record_list, key=operator.itemgetter(1, 2)), key=operator.itemgetter(0, 1))

def validate_input_json_file(inputfile):
    """
    1) Read the JSON file 
    2) Prepare a tuple list
    """
    status = False
    record_list = []
    try:
        if os.path.exists(inputfile) and ".json" in inputfile:
            file_ref = open(inputfile, mode='r', encoding='utf-8')
            json_record_content = json.loads(file_ref.read())
            json_record_list = json_record_content["record_list"]

            for json_record in json_record_list:
                record = (json_record['name'], json_record['age'], json_record['score'])
                record_list.append(record)
            
            status=True
        else:
            raise MyException("Invalid JSON file input")

    except MyException as e:
        logger.exception(f'Exception occured {str(e)}')
        return status, record_list
    return status, record_list

def main():

    logger.info(f'Arg len = {len(sys.argv)}')
    logger.info(f'Arg list = {str(sys.argv)}')
    set_logger_setting()
    try:
        inputfile = None
        opts, args = getopt.getopt(sys.argv[1:], "i:")
        for opt, arg in opts:
            if opt == '-i':
                inputfile = arg
    
        if inputfile == None:
            raise MyException("input file error")
        
        logger.info(f'inputfile= {inputfile}')
    except getopt.GetoptError:
        logger.error(f'-i <inputfile>')
        sys.exit(2)
    except MyException as e:
        logger.error(f'-i <inputfile>')
        logger.error(f'Exception occured as {str(e)}')
        sys.exit(2)

    status, record_list = validate_input_json_file(inputfile)

    if status:
        print(sort_values(record_list))

if __name__ == '__main__':
    main()




