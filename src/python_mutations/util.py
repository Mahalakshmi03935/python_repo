import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def mutate_string(string, position, character):
    if position < 0 or position >= len(string):
        logging.error("Invalid position provided.")
        return string
    else:
        string_list = list(string)#mahalakshmi
        string_list[position] = character#4-->l
        result = ''.join(string_list)
        logging.debug(result)
        return result
