**Python Repo**:This repository contains the Python programs

``**1.Percentage_Problem:**`
Allows users to input the number of students and their corresponding marks and Computes the average marks for a given student.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program.

**Functions Used:**

**student_marks()**:This function prompts the user to input the number of students and their respective marks.
It stores the input data in a dictionary where the keys are student names and the values are lists of their marks.

**calculate_average(student_marks, query_name)**:This function calculates the average marks for a specific student.
It takes two parameters:
student_marks: Dictionary containing student names as keys and lists of their marks as values.
query_name: Name of the student for whom the average marks need to be calculated.
Returns the calculated average marks for the specified student.

**Modules Used:**
**logging**: Utilized for basic logging functionalities such as displaying debug messages.

**`2.Word_Order:**
Allows users to input a list of words and counts the occurrences of each unique word.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**word_order():**
Prompts the user to input the length of the words list.
Accepts user input for words and counts the occurrences of each unique word.
Returns the count of unique words and their respective occurrences as a string.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying debug messages.

**3.Time_delta:**
 Computes the time difference in seconds between two datetime strings.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**time_delta():**

Prompts the user to input the number of test cases.
Accepts datetime strings for each test case.
Parses the datetime strings and calculates the time difference in seconds.
Returns the time difference as an integer.

**Modules used:**

**logging:** Utilized for basic logging functionalities such as displaying debug messages.

**datetime:** Imported to work with datetime objects and perform datetime operations.

**4.Text_alignment**:Generates a pattern of text aligned in various ways using a specified character and thickness.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**text_alignment(thickness):**
Generates a pattern of text aligned in different ways using the specified character and thickness.
Returns the generated pattern as a string.

**Modules:**
logging: Utilized for basic logging functionalities such as displaying information about the text alignment process.

**5.Second_max_num**:Identifies the second highest score from a list of scores.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**find_runner_up_score(n, scores):**
Accepts the number of scores (n) and the list of scores (scores).
Returns the second highest score from the list.
If there are less than two scores or less than two unique scores, it returns None.

**Modules:**
logging: Utilized for basic logging functionalities such as displaying debug messages.

**6.Calendar_module**:Determines the day of the week for a specified date

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**find_day():**
Accepts input in the format mm dd yyyy (month, day, year).
Utilizes the calendar module to find the day of the week for the provided date.
Returns the day of the week as a string.

Modules used:

**logging:** Utilized for basic logging functionalities such as displaying information about the found day.

**calendar:** Imported to work with date-related functionalities, specifically to find the day of the week.