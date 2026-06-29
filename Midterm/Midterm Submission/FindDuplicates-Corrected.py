def partition(array, low, high):
    # Modified to track descending order sort (>= pivot instead of <= pivot)
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Load data safely
data = []
try:
    with open("p2.txt", 'r') as fin:
        for line in fin:
            if line.strip():
                data.append(int(line.strip()))
except FileNotFoundError:
    print("Error: p2.txt file not found. Generating dummy test values.")
    data = [10, 20, 20, 30, 30, 30, 40]

print("Unsorted Array")
print(len(data), "items")

# Perform Sort
size = len(data)
quickSort(data, 0, size - 1)

# Count Duplicates using a frequency strategy to guarantee accuracy 
counts = {}
for value in data:
    counts[value] = counts.get(value, 0) + 1

count_duplicates = 0
for count in counts.values():
    if count > 1:
        count_duplicates += (count - 1)

print("Found", count_duplicates, "duplicates")
