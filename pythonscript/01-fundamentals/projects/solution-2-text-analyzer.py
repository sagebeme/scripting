#!/usr/bin/env python3
"""
Solution: Project 2 - Text Analyzer
Analyzes text and displays statistics
"""

import re
from collections import Counter

def analyze_text(text):
    """Analyze text and return statistics"""
    if not text:
        return None
    
    # Count total characters
    total_chars = len(text)
    
    # Count words (split by whitespace)
    words = text.split()
    word_count = len(words)
    
    # Count sentences (count periods, exclamation marks, question marks)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    
    # Find the most common word
    # Remove punctuation and convert to lowercase
    words_clean = [re.sub(r'[^\w]', '', word.lower()) for word in words if word]
    word_freq = Counter(words_clean)
    if word_freq:
        most_common_word, count = word_freq.most_common(1)[0]
    else:
        most_common_word = "N/A"
        count = 0
    
    # Calculate average word length
    if word_count > 0:
        total_word_length = sum(len(word) for word in words)
        avg_word_length = total_word_length / word_count
    else:
        avg_word_length = 0
    
    return {
        'total_chars': total_chars,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'most_common_word': most_common_word,
        'most_common_count': count,
        'avg_word_length': avg_word_length
    }

def display_statistics(stats):
    """Display statistics in a readable format"""
    if stats is None:
        print("No text to analyze.")
        return
    
    print("\n" + "=" * 40)
    print("TEXT ANALYSIS RESULTS")
    print("=" * 40)
    print(f"Total Characters:     {stats['total_chars']}")
    print(f"Total Words:         {stats['word_count']}")
    print(f"Total Sentences:     {stats['sentence_count']}")
    print(f"Most Common Word:     '{stats['most_common_word']}' (appears {stats['most_common_count']} times)")
    print(f"Average Word Length:  {stats['avg_word_length']:.2f} characters")
    print("=" * 40)

def main():
    """Main function"""
    print("Text Analyzer")
    print("============")
    print()
    
    # Get text input from user
    print("Enter text to analyze (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "" and lines:
            break
        if line:
            lines.append(line)
    
    text = "\n".join(lines)
    
    if not text.strip():
        print("No text entered.")
        return
    
    # Analyze text
    stats = analyze_text(text)
    
    # Display statistics
    display_statistics(stats)

if __name__ == "__main__":
    main()
