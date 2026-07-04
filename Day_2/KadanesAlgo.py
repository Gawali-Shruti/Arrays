# Input number of elements
n = int(input("Enter number of elements: "))

# Input array elements
arr = list(map(int, input("Enter elements: ").split()))

max_sum = arr[0]
current_sum = 0

for num in arr:
    current_sum += num

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print("Maximum Subarray Sum =", max_sum)