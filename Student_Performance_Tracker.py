class Student:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def Calculate_Average(self):
        if len(self.score) == 0:
            return 0
        return  sum(self.score) / len(self.score)

    def isPassing(self, passing: int = 40):
        return all(score >= passing for score in self.score)
    
           
        
class Performance_Tracker():
    def __init__(self):
        self.student = {}
        self.score = []

    def add_Student(self, name,score):
        student = Student(name , score)
        self.student[name]= student

    def Calculate_Class_Average(self):
        if len(self.student) == 0:
            return 0
        Total_Average = sum(student.Calculate_Average()  for student in self.student.values())
        return Total_Average/ len(self.student)
    def Display_Student_Performance(self):
        print("------Display Student Performance------")
        for student in self.student.values():
            average_score = student.Calculate_Average()
            if student.isPassing():
                status = 'Pass'
            else:
                status = 'Needs Improvement'
            print(f"Student Name: {student.name}, Average Score: {average_score}, Status: {status}")
        print(f'\n Class Average Score {self.Calculate_Class_Average()}')                

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
            


    

