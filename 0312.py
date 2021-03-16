class Student:
    def __init__(self, name, number, school, department, tall ):
        self.studentName = name
        self.studentNumber = number
        self.studentSchool = school
        self.studentDepartment = department
        self.studentTall = tall
    def showinfo(x):
        print(x.studentName, x.studentNumber, x.studentSchool , x.studentDepartment, x.studentTall)
 
x1 = Student("張祐瑋", 109021085, "亞洲", "資工", 173)
x2 = Student("張又仁", 109334021, "中興", "環育", 169)
x3 = Student("蕭指尹", 109069045, "大葉", "環育", 176)

x1.showinfo()
x2.showinfo()
x3.showinfo()

class Book:
    def __init__(self, name, year, author, publish, price ):
        self.bookName = name
        self.bookYear = year
        self.bookAuthor = author
        self.bookPublish = publish
        self.bookPrice = price
    def showinfo(y):
        print(y.bookName, y.bookYear, y.bookAuthor , y.bookPublish, y.bookPrice)
 
y1 = Book("冰菓", 2011, "米澤穗信", "角川", 300)
y2 = Student("心", 2014, "夏目漱石", "大牌", 252)
y3 = Student("游牧人生", 2019, "潔西卡", "臉譜", 332)

y1.showinfo()
y2.showinfo()
y3.showinfo()