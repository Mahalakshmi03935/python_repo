import logging

logging.basicConfig(level=logging.INFO)

def calculate_average():
    n = int(input())
    student_records = {}
    for _ in range(n):
        name, *marks = input().split()
        scores = list(map(float, marks))
        student_records[name] = scores
    student_name = input()
    try:
        average_score = sum(student_records[student_name]) / len(student_records[student_name])
        logging.info(f"Average score for {student_name}: {average_score}")
        return round(average_score, 2)
    except KeyError:
        logging.error(f"Student {student_name} not found in records.")
        return None
