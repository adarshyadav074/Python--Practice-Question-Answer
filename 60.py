# Print numbers 1–10 but stop at 5 (break)
for i in range(1,11):
    if i == 5:
        break   
    print(i)

# Print numbers 1–10 but skip 5 (continue)
for i in range(1,11):
    if i == 5:
        continue
    print(i)