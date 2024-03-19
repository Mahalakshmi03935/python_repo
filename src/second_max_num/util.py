import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


# Define utility function to find the runner-up score
def find_runner_up_score(n, scores):
    if len(scores) < 2:
        return None
    unique_scores = sorted(set(scores), reverse=True)
    if len(unique_scores) < 2:
        return None
    return unique_scores[1]
n=int(input("enter the number:"))
scores = list(map(int,input("enter the input:").split()))
logging.debug(runner_up_score)
