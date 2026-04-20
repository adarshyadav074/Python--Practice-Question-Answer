# 👉 Check:
# 👉 word "python" present hai ya nahi file me
file_name = "2.txt"
with open (file_name, "r") as f:
    content = f.read()
    if "Python" in content or "python" in content:
        print("Yes, Python is present in file.")
    else:
        print("No, Python isn't present in file.")