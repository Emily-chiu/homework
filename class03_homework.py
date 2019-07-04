class Course(): #課程
    def __init__(self, name, number, credit, classification, introduction, teacher, time):
        self.name = name
        self.number = number
        self.credit = credit
        self.classification = classification
        self.introduction = introduction
        self.teacher = teacher
        self.time = time

    def courseshow(self):
        print("課程名稱:",self.name)
        print("課程編碼:",self.number)
        print("學分:",self.credit)
        print("修習別:",self.classification)
        print("課程介紹:",self.introduction)
        print("授課老師:",self.teacher)
        print("上課時間:",self.time)

class Grade(Course):    #成績
    def __init__(self, name, number, credit, classification, introduction, teacher, time, grade):
        super().__init__(name, number, credit, classification, introduction, teacher, time)
        self.grade = grade
    
    def courseshow(self):
        Course.courseshow(self)
        print("成績:",self.grade)

class Human():
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def humanshow(self):
        print("姓名:",self.name)

class Student(Human):   #學生
    def __init__(self, name, number, course):
        super().__init__(name, number)
        self.course = course
    
    def avg(self): #算平均
        grade_sum = 0
        credit_sum = 0
        for course_object in self.course[0]:
            if course_object.grade == " ":
                # course_object.grade = 0
                # course_object.credit = 0
                pass
            else:
                grade_sum += course_object.grade * course_object.credit
                credit_sum += course_object.credit
            
        avg_temp = grade_sum/credit_sum
        print("加權平均:",avg_temp)
        print("已修",credit_sum,"學分")

    def studentshow(self):
        credits_list = []
        grades_list = []
        credits_sum = 0
        Human.humanshow(self)
        print("學號:",self.number)
        course_grade(self.course[0],self.course[1]) #父 -> 子
        for i in self.course[0]:
            i.courseshow()
            print("---------------------------------")

        self.avg()

def course_grade(course, grade):    #父 -> 子
    for course_num in range(len(course)):
        course[course_num] = Grade(course[course_num].name, course[course_num].number, course[course_num].credit, course[course_num].classification, course[course_num].introduction, course[course_num].teacher, course[course_num].time, grade[course_num])
    return course

#呼叫Course類別，印出課程詳細資料        
web_programming = Course("Web程式設計" , "IECS272", 3 , "選修" , "教導學生開發Responsive Web應用程式的知識與能力" , "陳錫民" , "(二)10:10-12:00 (四)17:10-18:00")
the_shih_chithe = Course("史記","CHIN205" , 2 , "選修" ,"史記" , "楊美美" , "(四)13:10-15:00")
cryptography = Course("密碼學","IECS352" , 3 , "選修" ,"概述密碼學及其相關應用的基礎知識" , "魏國瑞" , "(三)18:10-21:00")
japanese = Course("日文(一)","LC101", 2 , "選修" , "從日語的五十音教起，配合選定教材，讓同學活用於日常會話之中。" , "林盈萱" , "(三)15:10-17:00")
special_topics_study = Course("專題研究(二) ","COME492", 1 , "必修" , "專題討論" , "陳益生" , "(六)12:10-13:00")
korean = Course("韓文(二) ","LC124", 2 , "選修" , "本課程希望透過韓文，增進同學對韓國的社會變遷與生活環境有深刻的瞭解。" , "韓連善" , "(三)13:10-15:00")
Electromagnetics = Course("電磁學(二) ","COME21", 3 , "必修" , "學習Maxwell's Equation" , "林漢年" , "(二) 10:10~12:00 (四)08:10~09:00")
itec = Course("電磁相容導論","COME413", 3 , "選修" , "學習EMI和EMS" , "彭嘉美" , "(四) 08:10~12:00")
efec = Course("電磁相容實習 ","COME414", 1 , "選修" , "量測電磁干擾" , "林漢年" , "(三) 13:10~16:00 ")
mca = Course("微波電路分析","COME634", 2 , "選修" , "本課程主要在講授微波電路，內容涵蓋阻抗匹配、低雜訊放大器、功率放大器、混頻器等。" , "何滿龍" , "(四) 14:10~17:00")

s1_course = [web_programming , the_shih_chithe, cryptography, japanese, special_topics_study]
s1_grade = [78,80,80,86,91]

s1 = Student("張三", "D0448185", [s1_course, s1_grade])
s1.studentshow()
print("===================我是分割線===============================")

s2_course = [web_programming , the_shih_chithe, korean , japanese, special_topics_study]
s2_grade = [75,82,88,87,91]

s2 = Student("李四", "D0448495", [s2_course, s2_grade])
s2.studentshow()

print("===================我是分割線===============================")

s3_course = [web_programming , the_shih_chithe, korean]
s3_grade = [75,82," "]

s3 = Student("王五", "D045", [s3_course, s3_grade])
s3.studentshow()

