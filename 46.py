# 👉 Take marks:
# 👉 print grade:
# 90+ → A
# 80+ → B
# 70+ → C
# else → Fail

mark = int(input("Enter your math marks: "))

if mark>=90:
    print("Grade 'A'.")
elif mark>=80:
    print("Grade 'B'.")
elif mark>=70:
    print("Grade 'C'.")
else:
    print("Fail.")

if mark>0:
    print("Number is Positive.")
elif mark==0:
    print("Number is Zero.")
else:
    print("Number is Negative.")