import logging


def count_word_occurrences(n, words):
    logging.info("Counting word occurrences...")

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words = list(word_count.keys())
    occurrences = [word_count[word] for word in distinct_words]

    return distinct_words, occurrences
