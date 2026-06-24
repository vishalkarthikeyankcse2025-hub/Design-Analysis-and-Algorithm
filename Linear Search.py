arr = [12, 45, 7, 89, 23, 56, 31]  # 7 elements
target = 23

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Target found at index:", i)
        found = True
        break

if not found:
    print("Target not found")