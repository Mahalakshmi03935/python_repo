import logging


def text_alignment(thickness):
    c = 'H'
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    ans = ''

    for i in range(thickness):
        logging.info((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        ans += (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
        ans += '\n'


    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        ans += (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        ans += '\n'


    for i in range((thickness + 1) // 2):
        logging.info((c * thickness * 5).center(thickness * 6))
        ans += (c * thickness * 5).center(thickness * 6)
        ans += '\n'


    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        ans += (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        ans += '\n'


    for i in range(thickness):
        logging.info(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
        ans += ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
        ans += '\n'
    return ans