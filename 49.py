# 👉 Spam detector:
# 👉 check if message contains:
# "buy now"
# "click here"
# 👉 print "Spam"

a = input("Enter Comment: ").lower()

if "buy now" in a or "click here" in a:
    print("Spam Detected!!")
else:
    print("Comment printed.")