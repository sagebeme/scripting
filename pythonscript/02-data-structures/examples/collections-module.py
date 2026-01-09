#!/usr/bin/env python3
"""
Example 3: Collections Module
Demonstrate collections utilities
"""

from collections import Counter, defaultdict, deque, namedtuple

print("=== Collections Module ===")
print()

# Counter
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(items)
print(f"1. Counter: {counter}")
print(f"   Most common: {counter.most_common(2)}")
print()

# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')
print(f"2. Defaultdict: {dict(dd)}")
print()

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"3. Deque: {list(dq)}")
print(f"   Rotate right: ", end="")
dq.rotate(1)
print(list(dq))
print()

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"4. Named tuple: {p}")
print(f"   x coordinate: {p.x}, y coordinate: {p.y}")
print()

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'b'])
print(f"5. Counter addition: {c1 + c2}")
print(f"   Counter subtraction: {c1 - c2}")
