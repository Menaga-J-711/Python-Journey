
# 🟢 Task 2 — Student Marks
# Ask the user for:
# - Student name
# - Tamil mark
# - English mark
# - Maths mark
# - Science mark
# - Computer Science mark
# Then print all the details and total marks.

#CODE

student_name = input("Enter Student Name:")
tamil_mark = int(input("Enter Tamil Mark:"))
english_mark = int(input("Enter English Mark:"))
maths_mark = int(input("Enter Maths Mark:"))
scinece_mark = int(input("Enter Science Mark:"))
Computer_mark = int(input("Enter Computer Science Mark:"))
total = tamil_mark+english_mark+maths_mark+scinece_mark+Computer_mark
print()
print("---------Student Mark Details--------")
print("Tamil:", tamil_mark)
print("English:", english_mark)
print("Maths:", maths_mark)
print("Science:", scinece_mark)
print("Computer Science:", Computer_mark)
print()
print("------------------------------------------")
print("Total Mark of ",student_name ,"is ", total)
print("------------------------------------------")
print()



#OUTPUT


# Enter Student Name:Menaga J     
# Enter Tamil Mark:90
# Enter English Mark:89
# Enter Maths Mark:99
# Enter Science Mark:90
# Enter Computer Science Mark:80

# ---------Student Mark Details--------
# Tamil: 90
# English: 89
# Maths: 99
# Science: 90
# Computer Science: 80

# ------------------------------------------
# Total Mark of  Menaga J  is  448
# ------------------------------------------