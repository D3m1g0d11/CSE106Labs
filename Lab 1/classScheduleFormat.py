import string

class course:
        def __init__(self, subj, num, name, units, days, start, end, ave):
            self.dept = str(subj)
            self.classNum = num
            self.className = name
            self.classUnits = units
            self.classDays = days
            self.classStart = start
            self.classEnd = end
            self.classAve = ave

        def printSchedule(count, self):
            print("Course " + str(count) + ": " + str(self.dept) + self.classNum + ": " + self.className)      
            print("Number of Credits: " + self.classUnits)
            print("Days of Lectures: " + self.classDays)
            print("Lecture Time: " + self.classStart + " - " + self.classEnd)
            print("Stat: on average, students get " + self.classave + "% in this course")

def classScheduleFormat():
    #Change path here
    path = "/Users/John Biton/College Code/CSE S23/CSE 106/Lab 1/"
    with open(path + 'classesInput.txt', 'r') as file:

        count = int(file.readline())

        for i in range(1, count):
            
            subj = file.readline().strip()
            num = file.readline().strip()
            name = file.readline().strip()
            units = file.readline().strip()
            days = file.readline().strip()
            start = file.readline().strip()
            end = file.readline().strip()
            ave = file.readline().strip()
            
            courseOne = course(subj, num, name, units, days, start, end, ave) 
            courseOne.printSchedule(i)
            
    file.close()

classScheduleFormat()