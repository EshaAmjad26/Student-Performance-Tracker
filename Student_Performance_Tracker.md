# Student Performance Tracker

## Features

- Add students and their scores for multiple subjects
- Calculate individual average score for each student
- Check if each student is passing based on a set passing score
- Calculate and display the class average
- Input validation to ensure that scores are integers within the range (0-100)

## Classes

### Student Class

#### Attributes:

- **name**: Stores the name of the student.
- **score**: A list of scores (marks) for different subjects.

#### Methods:

- **`__init__(self, name, score)`**: Initializes a student with their name and scores.
- **`Calculate_Average(self)`**: Calculates the average score of the student. Returns `0` if there are no scores.
- **`isPassing(self, passing: int = 40)`**: Checks if the student has passed (i.e., all scores are greater than or equal to the passing mark).
- **`show(self)`**: Returns a string representation of the student's name and scores.

### Performance_Tracker Class

#### Attributes:

- **student**: A dictionary storing student names as keys and their respective `Student` objects as values.
- **score**: A list to store scores for new students (used in the `main()` function).

#### Methods:

- **`__init__(self)`**: Initializes the `Performance_Tracker` with an empty dictionary for students and an empty score list.
- **`add_Student(self, name, score)`**: Adds a new student to the tracker with the provided name and score.
- **`Calculate_Class_Average(self)`**: Calculates the class average by computing the average of all students' scores.
- **`Display_Student_Performance(self)`**: Displays the performance of each student, including their name, average score, and pass/fail status. Also shows the class average.

## Example

### Code

```python
def main():
    P1 = Performance_Tracker()
    name : str
    while True:
        name = input('Enter Student Name or q to "Quit " ')
        if name == 'q':
            break

        score : int = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    marks: int = int(input(f'Enter {subject} Marks of {name} range (0-100) '))
                    if 0 <= marks <= 100:
                        score.append(marks)
                        break
                    else:
                        print('Invalid Marks. Should be in range (0-100)')

                except Exception:
                    print('Invalid Marks.  Marks should be an Integer range (0-100)')
        P1.add_Student(name, score)
        choice = input('Do you want to add more Students yes or no (Press y/n)')

        if choice.lower() != 'y':
            break
    P1.Display_Student_Performance()

main()
```

## Sample Output

```
Enter Student Name or q to "Quit " John
Enter Math Marks of John range (0-100) 75
Enter Science Marks of John range (0-100) 80
Enter English Marks of John range (0-100) 85
Do you want to add more Students yes or no (Press y/n) y
Enter Student Name or q to "Quit " Alice
Enter Math Marks of Alice range (0-100) 40
Enter Science Marks of Alice range (0-100) 55
Enter English Marks of Alice range (0-100) 45
Do you want to add more Students yes or no (Press y/n) n
------Display Student Performance------
Student Name: John, Average Score: 80.0, Status: Pass
Student Name: Alice, Average Score: 46.666666666666664, Status: Needs Improvement

 Class Average Score 63.333333333333336
```

## Usage

1. Run the script in a Python environment.
2. Input the student's name and marks for each subject (Math, Science, and English).
3. The program will display the performance of all entered students, showing their average score and whether they are passing or need improvement.
4. It will also display the class average at the end.

## Requirements to Run the Code

1. Python Version
   <br>-The code is written in Python 3.x.
   <br>-Ensure that you have a Python 3.x version installed.
   <br>-You can check your Python version by running:

`python --version`

2. Python Modules Required
   <br>-The code relies on built-in Python libraries, so no external libraries or packages are required. You can directly run the code without any need for installation.
3. How to Run the Code
   <br>-Save the Code: Copy the provided code and save it in a file with the .py extension (e.g., student_performance_tracker.py).
   <br>-Open Command Line or Terminal: Navigate to the directory where your Python file is saved.
   <br>-Run the Code: In your terminal or command prompt, run the Python file by typing:

   `python student_performance_tracker.py`

4. Run code in colab Notebook
   <br>- You can also run this code in a Google Colab notebook.
   <br>- To do so, simply copy the entire code into a new Colab notebook cell.
   <br>- Press `Shift + Enter` to run the code interactively.

5. Output
   <br>- After entering the data for all students, the program will display:
   <br>-The student names, their average score, and whether they have passed or need improvement.
   <br>-The overall class average score.
