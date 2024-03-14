from python_repo.src.second_max_num.util import find_runner_up_score
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Define some sample scores
n=int(input("enter the number:"))
scores = list(map(int,input("enter the input:").split()))

# Call the function
runner_up_score = find_runner_up_score(n,scores)

# Log the result
logging.debug(runner_up_score)
