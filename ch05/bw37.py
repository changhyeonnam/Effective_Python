class SimpleGradebook:
    def __init__(self):
        self._grades={}
    def add_student(self,name):
        self._grades[name]=[]
    def report_grade(self,name,score):
        self._grades[name].append(score)
    def average_grade(self,name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

book = SimpleGradebook()
book.add_student('Jimmy')
book.report_grade("Jimmy",10);
book.report_grade("Jimmy",20);
book.report_grade("Jimmy",30);
print(book.average_grade("Jimmy"))

from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades ={}
