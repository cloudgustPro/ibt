def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    raw_values = input("Enter a sorted list of numbers separated by spaces: ")
    try:
        arr = [int(value) for value in raw_values.split()]
    except ValueError:
        print("Please enter only integer values.")
        return

    if not arr:
        print("No numbers were entered.")
        return

    try:
        target = int(input("Enter the number to search for: "))
    except ValueError:
        print("Please enter a valid integer for the target.")
        return

    index = binary_search(arr, target)
    if index != -1:
        print(f"Found {target} at index {index}.")
    else:
        print(f"{target} was not found in the list.")


if __name__ == "__main__":
    main()