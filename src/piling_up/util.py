# util.py

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def can_stack_cubes(test_cases):
    results = []

    for cubes in test_cases:
        left, right = 0, len(cubes) - 1
        prev_cube = float('inf')
        possible = True

        while left <= right:
            if cubes[left] >= cubes[right]:
                if cubes[left] <= prev_cube:
                    prev_cube = cubes[left]
                    left += 1
                else:
                    possible = False
                    break
            else:
                if cubes[right] <= prev_cube:
                    prev_cube = cubes[right]
                    right -= 1
                else:
                    possible = False
                    break

        if possible:
            results.append("Yes")
        else:
            results.append("No")

    return results
