# Monkey Climbing Pole Problem

# input
H = int(input("Enter height of pole (H): ").strip())  # height of pole
X = int(input("Enter climb distance (X): ").strip())  # climb distance
Y = int(input("Enter slip distance (Y): ").strip())  # slip distance

jumps = 0
current_height = 0

while current_height < H:
    jumps += 1
    current_height += X

    if current_height >= H:
        break

    current_height -= Y

print("It need", jumps, "jumps")