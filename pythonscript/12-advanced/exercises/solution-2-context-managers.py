#!/usr/bin/env python3
"""
Solution: Exercise 2 - Context Managers
"""
print("=" * 60)
print("Solution: Exercise 2 - Context Managers")
print("=" * 60)

class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False

with FileManager('test.txt') as f:
    f.write("Hello")
print("1. File written and closed")

from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    file = open(filename, 'w')
    try:
        yield file
    finally:
        file.close()

with file_manager('test2.txt') as f:
    f.write("World")
print("2. File written using contextmanager")

print("\n✅ Solution completed!")
