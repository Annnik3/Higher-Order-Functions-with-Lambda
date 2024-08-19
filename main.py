def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]


doubled = apply_operation([5, 6, 7, 8, 9], lambda x: x * 2)
print("Doubled:", doubled)

squared = apply_operation([5, 6, 7, 8, 9], lambda x: x ** 2)
print("Squared:", squared)


filtered = apply_operation([5, 6, 7, 8, 9], lambda x: x if x % 2 != 0 else None)
filtered = [x for x in filtered if x is not None]  # Remove 'None' values
print("Filtered (odd numbers):", filtered)