import logging

def merge_the_tools(s, k):
    n = len(s)
    substrings = [s[i:i+k] for i in range(0, n, k)]
    result = ""
    for substring in substrings:
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
        result += ''.join(unique_chars) + "\n"
        logging.debug(''.join(unique_chars))
    return result

