


#面向对象练习


class Student():

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def study(self,course_name):
        self.course_name =course_name
        print('%s正在学习%s'%(self.name,self.course_name))

    def watch_av(self):
        if self.age <18:
            print("%s正在学习"%self.name)
        else:
            print("%s正在看av"%self.name)


def main():
    stu1 = Student('小汪',19)
    stu1.study('英语')
    stu1.watch_av()


if __name__ == '__main__':
    main()