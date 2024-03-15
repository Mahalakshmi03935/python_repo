import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def generate_hackerrank_logo(thickness):
    if thickness % 2 == 0:
        raise ValueError("Thickness must be an odd number")

    logo = ''
    width = thickness * 3

    # Top Cone
    for i in range(thickness):
        line = 'H' * (2 * i + 1)
        logo += line.center(width, '-') + '\n'

    # Top Pillars
    for i in range(thickness + 1):
        line = ('H' * thickness).center(thickness * 2, ' ')
        logo += line + line + '\n'

    # Middle Belt
    for i in range((thickness + 1) // 2):
        logo += ('H' * thickness * 5).center(thickness * 6, ' ') + '\n'

    # Bottom Pillars
    for i in range(thickness + 1):
        line = ('H' * thickness).center(thickness * 2, ' ')
        logo += line + line + '\n'

    # Bottom Cone
    for i in range(thickness):
        line = 'H' * (2 * (thickness - i) - 1)
        logo += line.center(width, '-') + '\n'

    logger.info("Generated HackerRank logo with thickness: %d", thickness)
    return logo

