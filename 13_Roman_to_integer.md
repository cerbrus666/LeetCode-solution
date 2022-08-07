- The solution applies Left-To-Right passing method
- It basically checks from left to right with certain conditions:
    1. If left is bigger than right, then adds up the total and move one pointer
    2. If left is smaller than right, then right value will minus the left value and add ups to the total, then move two pointer
    3. Also if left is smaller than right, needs to make that there is at least two pointer space to move

- The Roman Numerals are represented as the following:
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
