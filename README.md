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

**Modules used:**

**logging:** Utilized for basic logging functionalities such as displaying information about the found day.

**calendar:** Imported to work with date-related functionalities, specifically to find the day of the week.

**7.Floor_Ceiling_rint**: Computes the floor, ceiling, and rint values of elements in a given array.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**floor_ceil_rint():**
Accepts input array elements separated by space.
Utilizes the numpy module to calculate the floor, ceiling, and rounding values of the array elements.
Returns the floor, ceiling, and rounding values as numpy arrays.

**Modules used:**

**logging:** Utilized for basic logging functionalities such as displaying information about the calculated values.
**numpy:** Imported to perform mathematical operations and array manipulations efficiently.

**8.Python_string_formatting:** Formats numbers in decimal, octal, hexadecimal, and binary representations.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**string_formatting():**
Accepts an integer n as input.
Calculates the spacing required for formatting based on the binary representation of n.
Formats numbers from 1 to n in decimal, octal, hexadecimal, and binary representations with proper spacing.
Returns the formatted string.

**Modules used:**
**logging**: Utilized for basic logging functionalities such as displaying formatted strings.

9.**Python_mutations:** Replaces a character at a specified position in a given string.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**mutate_string():**
Prompts the user to input a string and the position along with the character to replace.
Replaces the character at the specified position in the string.
Returns the mutated string.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying debug messages.

10.**Min_Max:** Identifies the minimum of the maximum values in rows of a 2D array.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**min_max_num():**
Accepts input for the dimensions of the 2D array and its elements.
Utilizes the numpy module to create a numpy array from the input data.
Computes the maximum values in each row and then finds the minimum among them.
Returns the minimum of the maximum values.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying information about the minimum of maximum values.

**numpy:** Imported to work with arrays and perform mathematical operations efficiently.

11.Linear_algebra:Computes the determinant of a square matrix.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**linear_algebra():**
Accepts input for the dimensions of the square matrix and its elements.
Utilizes the numpy module to create a numpy array from the input data.
Calculates the determinant of the square matrix using NumPy's linear algebra module.
Returns the determinant rounded to two decimal places.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying information about the calculated determinant.

**numpy:** Imported to perform linear algebra operations efficiently.

**12.Py_collections:** Computes the average of a specific column in a dataset using namedtuple.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**calculate_average():**
Accepts input for the number of records (n) and the column names.
Utilizes namedtuple to create a structured representation of each record.
Calculates the total marks from the specified column for n records.
Returns the average of the specified column.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying debug messages with timestamps and levels.

**collections.namedtuple**: Imported to create a lightweight object-oriented structure for representing records.

**13.Mean_var_std:**  Computes the mean, variance, and standard deviation along each row of a 2D array.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program


**Functions used:**
**calculate_mean_var_std():**
Accepts input for the dimensions of the 2D array and its elements.
Utilizes the numpy module to create a numpy array from the input data.
Calculates the mean, variance, and standard deviation along each row of the array.
Returns three arrays containing the mean, variance, and standard deviation values.

**Modules used:**

**logging:** Utilized for basic logging functionalities such as displaying debug messages with timestamps and levels.

**numpy:** Imported to perform mathematical operations and array manipulations efficiently.

**14.Merge_the_tools:** Splits a string into substrings of a specified length and removes duplicate characters within each substring.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**merge_the_tools():**
Prompts the user to input a string and a factor value.
Splits the string into substrings of length k.
Removes duplicate characters within each substring.
Returns a string containing the modified substrings separated by newlines.

**Modules used:**
**logging:** Utilized for basic logging functionalities such as displaying debug messages.

**15.No_idea:** Calculates happiness based on given arrays and a reference array.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**

**calculate_happiness():**
Accepts input arrays a, A, and B.
Sorts arrays A and B.
Calculates happiness by comparing elements of arrays A and B with the corresponding elements in array b.
Returns the absolute value of the calculated happiness.

**Modules used:**
logging: Utilized for basic logging functionalities such as displaying debug messages.

**16.Iterators_problem :**  Determines the probability of selecting combinations containing a specified element.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**iterators():**
Accepts input for the total number of elements, a list of elements, and the size of combinations to consider.
Computes all possible combinations of the given elements.
Calculates the probability of selecting combinations containing a specified element "a".
Returns the probability as a floating-point value.

**Modules used:**

**logging:** Utilized for basic logging functionalities such as displaying debug messages.

**itertools.combinations:** Imported to generate combinations of elements efficiently.

**17.Piling_up:** Checks if a stack of cubes can be formed with given cube lengths.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**can_stack_cubes(num_cubes, cube_lengths):**
Accepts the number of cubes and a list of cube lengths as input.
Determines if it's possible to form a stack of cubes based on the given lengths.
Returns "Yes" if a stack can be formed, otherwise "No".

**Main Function:**
**main():**
Accepts input for the number of test cases.
For each test case, it inputs the number of cubes and their lengths, then calls can_stack_cubes() function.
Prints the result indicating whether a stack of cubes can be formed for each test case.

**18.email_address:**  Validates email addresses and sorts them in lexicographical order.

**Files:**

util.py: Contains the main functions for managing student marks.

driver.py: Entry point script for executing the program

**Functions used:**
**is_valid_email(email):** Validates the given email address using regular expressions.
Returns True if the email address is valid, otherwise False.
function():Accepts input for the number of email addresses (n) and the email addresses themselves (s).
Extracts the email addresses from the input string.
Filters and sorts the valid email addresses in lexicographical order.
Returns a list of sorted valid email addresses.

**Modules used:**

**re:** Utilized for regular expression operations to validate email addresses.

**logging:** Utilized for basic logging functionalities such as displaying debug messages.