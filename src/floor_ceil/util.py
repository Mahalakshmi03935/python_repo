import logging
import numpy
logging.basicConfig(level=logging.INFO,format="%(message)s")
def floor_ceil():
    numpy.set_printoptions(sign=' ')
    array = numpy.array(input().split(), float)
    logging.info(numpy.floor(array))
    logging.info(numpy.ceil(array))


