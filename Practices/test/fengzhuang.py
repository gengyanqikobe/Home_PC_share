

class student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def student_print(self):
        print("%s 's score is :%s"%(self.name,self.score))

    def compare(self,s):
        if self.score > s:
            print("%s's better!"%(self.name))
        elif self.score == s:
            print("all better")
        else:
            print("%s's worse!"%(self.name))


Alex = student('Alex',90)

Alex.student_print()

Alex.compare(10)
Alex.compare(90)
Alex.compare(100)