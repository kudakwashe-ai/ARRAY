while True:
    user_input = input("Enter at least 5 numbers separated by spaces: ")
    stats_numbers = list(map(int, user_input.split()))
    if len(stats_numbers) >= 5:
        break
    print("Please enter at least 5 numbers.")

stats_numbers.sort()
minimum = stats_numbers[0]
maximum = stats_numbers[-1]
average = sum(stats_numbers) / len(stats_numbers)
# Calculate median
n = len(stats_numbers)
if n % 2 == 0:
    median = (stats_numbers[n//2 - 1] + stats_numbers[n//2]) / 2
else:
    median = stats_numbers[n//2]

print("Sorted List:", stats_numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Median:", median)
