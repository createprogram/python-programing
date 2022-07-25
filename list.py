#list data type

marks =[10,20,30,40]
print(marks)
print(marks[0])
print(marks[0:2])

#operations in list
#1.appends
marks =[10,20,30,40,50]
marks.append(60)
print(marks)

#2.insert operation
marks =[10,20,30,40]
marks.insert(1,90)
print(marks)
print(90 in marks)

#3.length operation
print(len(marks))

#4.how to while in intrect
marks =[50,60,70]
i=0
while i<len(marks):
    print(marks[i])
    i=i+1

#5.clear operation
marks =[20,30,50]
marks.clear()
print(marks)


