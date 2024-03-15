import logging
from util import mutate_string


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

mutated_string = mutate_string('mahalakshmi', 10, 'e')
logging.debug(mutated_string)
