import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


# Define utility function to find the runner-up score
def find_runner_up_score(n,scores):
    if len(scores) < 2:
        return None
    sorted_scores = sorted(scores, reverse=True)
    runner_up_score = sorted_scores[1]
    return runner_up_score