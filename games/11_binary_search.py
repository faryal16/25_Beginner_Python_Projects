import streamlit as st

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # target not found


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def run():
    st.title("Binary Search Tool")

    st.write("Enter a list of sorted numbers (comma-separated):")
    user_input = st.text_input("List:", "2, 4, 6, 8, 10, 12, 14, 16,18,20")
    target_input = st.number_input("Target value to search for:", step=1)

    if st.button("Search"):
        try:
            numbers = sorted([int(x.strip()) for x in user_input.split(",")])
            target = int(target_input)

            result_iter = binary_search_iterative(numbers, target)
            result_recur = binary_search_recursive(numbers, target, 0, len(numbers) - 1)

            st.write(f"Sorted List: {numbers}")
            st.write(f"Target: {target}")
            st.success(f"Iterative Result: Found at index {result_iter}" if result_iter != -1 else "Iterative Result: Target not found")
            st.success(f"Recursive Result: Found at index {result_recur}" if result_recur != -1 else "Recursive Result: Target not found")

        except ValueError:
            st.error("Please enter valid integers separated by commas.")

if __name__ == "__main__":
    run()
