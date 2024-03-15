from util import calculate_average_marks

def main():
    n = int(input("Enter the number of students: ").strip())
    student_records = {}
    for _ in range(n):
        name, *marks = input("Enter name and marks separated by space: ").split()
        student_records[name] = list(map(float, marks))
    query_name = input("Enter the name of the student to query: ").strip()

    result = calculate_average_marks(student_records, query_name)
    print(f"The average marks for {query_name} are {result}")

if __name__ == "__main__":
    main()

