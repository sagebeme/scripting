#!/usr/bin/env python3
"""
Solution: Exercise 3 - Special Methods
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 3 - Special Methods")
print("=" * 60)

# Task 1: Implement __str__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Python Guide", "John Doe", 300)
print(f"1. {str(book)}")

# Task 2: Implement __repr__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Python Guide", "John Doe", 300)
print(f"2. {repr(book)}")

# Task 3: Implement __len__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __len__(self):
        return self.pages

book = Book("Python Guide", "John Doe", 300)
print(f"3. Length: {len(book)} pages")

# Task 4: Implement __eq__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Python Guide", "John Doe", 250)
print(f"4. Books equal: {book1 == book2}")

# Task 5: Implement __lt__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __lt__(self, other):
        return self.pages < other.pages

book1 = Book("Book 1", "Author 1", 200)
book2 = Book("Book 2", "Author 2", 300)
print(f"5. book1 < book2: {book1 < book2}")

# Task 6: Implement __add__
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

book1 = Book("Book 1", 200)
book2 = Book("Book 2", 300)
combined = book1 + book2
print(f"6. Combined: {combined.title}, {combined.pages} pages")

# Task 7: Implement __getitem__
class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters
    
    def __getitem__(self, index):
        return self.chapters[index]

book = Book("Python Guide", ["Intro", "Basics", "Advanced"])
print(f"7. Chapter 0: {book[0]}")

# Task 8: Implement __contains__
class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters
    
    def __contains__(self, chapter):
        return chapter in self.chapters

book = Book("Python Guide", ["Intro", "Basics", "Advanced"])
print(f"8. 'Basics' in book: {'Basics' in book}")

# Task 9: Implement __call__
class Book:
    def __init__(self, title):
        self.title = title
    
    def __call__(self, chapter):
        return f"Reading chapter: {chapter}"

book = Book("Python Guide")
print(f"9. {book('Introduction')}")

# Task 10: Implement __enter__ and __exit__ (context manager)
class Book:
    def __init__(self, title):
        self.title = title
    
    def __enter__(self):
        print(f"Opening {self.title}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.title}")

print("10. Context manager:")
with Book("Python Guide") as book:
    print(f"   Reading {book.title}")

print("\n✅ Solution completed!")
