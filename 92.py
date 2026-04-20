# Print:
# numbers 1–20
# but:
# skip even numbers
# stop at 15

def num():
    for i in range(1,21):
        if i%2 == 0:
            continue
        elif i == 15:
            break
        print(i)

num()