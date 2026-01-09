#!/usr/bin/env python3
"""
Solution: Exercise 4 - Collections Module
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

from collections import Counter, defaultdict, deque, namedtuple

print("=" * 60)
print(f"Solution: Exercise 4 - Collections Module")
print("=" * 60)

# Task 1: Use Counter to count elements
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(items)
print(f"1. Counter: {counter}")

# Task 2: Get most common items from Counter
most_common = counter.most_common(2)
print(f"2. Most common 2: {most_common}")

# Task 3: Use defaultdict
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(3)
print(f"3. Defaultdict: {dict(dd)}")

# Task 4: Use deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to left
dq.append(4)      # Add to right
dq.popleft()      # Remove from left
print(f"4. Deque: {dq}")

# Task 5: Named tuple for coordinates
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(f"5. Point: {point}, x={point.x}, y={point.y}")

# Task 6: Counter arithmetic
counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'b', 'b'])
combined = counter1 + counter2
print(f"6. Combined counters: {combined}")

# Task 7: Use defaultdict with int default
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry']
for word in words:
    word_count[word] += 1
print(f"7. Word count: {dict(word_count)}")

# Task 8: Deque rotation
dq2 = deque([1, 2, 3, 4, 5])
dq2.rotate(2)  # Rotate right by 2
print(f"8. Rotated deque: {dq2}")

# Task 9: Named tuple with methods
Person = namedtuple('Person', ['name', 'age'])
person = Person('Alice', 30)
print(f"9. Person: {person}, name={person.name}, age={person.age}")

# Task 10: Counter from string
text = "hello world"
char_counter = Counter(text)
print(f"10. Character frequencies: {dict(char_counter)}")

print("\n✅ Solution completed!")
