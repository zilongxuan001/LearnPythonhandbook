animals = "{}, {}, {} ,{}"
numbers = "{}"

print(animals.format("dog", "cat", "rabbit", "mouse"))
print(numbers.format(1))

print(int(numbers.format(4)) + int(numbers.format(7)))

print(animals.format(
    "a good dog",
    "don't bite people.",
    "Do you know",
    "it?"
    ))

