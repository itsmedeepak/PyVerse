import re
from collections import Counter
import os
from tkinter import Tk, filedialog

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = self._extract_words()
    
    def _extract_words(self):
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-z]+\b', self.text.lower())
        return words
    
    def count_words(self):
        return len(self.words)
    
    def count_characters(self):
        return len(self.text)
    
    def count_sentences(self):
        # Split by common sentence endings
        sentences = re.split(r'[.!?]+', self.text)
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    
    def most_common_words(self, n=5):
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'it'}
        
        # Filter out stop words
        filtered_words = [w for w in self.words if w not in stop_words]
        
        # Count word frequencies
        word_counts = Counter(filtered_words)
        return word_counts.most_common(n)
    
    def display_analysis(self):
        print("\n" + "="*50)
        print("TEXT ANALYSIS RESULTS")
        print("="*50)
        
        print(f"\nTotal Characters: {self.count_characters()}")
        print(f"Total Words: {self.count_words()}")
        print(f"Total Sentences: {self.count_sentences()}")
        
        print(f"\n Most Common Words:")
        print("-" * 30)
        common_words = self.most_common_words(5)
        
        if common_words:
            for i, (word, count) in enumerate(common_words, 1):
                print(f"{i}. '{word}' - {count} times")
        else:
            print("No words found.")
        
        print("="*50 + "\n")


def read_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def select_file():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    filename = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()
    return filename


def main():
    print("="*50)
    print("WELCOME TO TEXT ANALYZER")
    print("="*50)
    
    while True:
        print("\nChoose an option:")
        print("1. Enter text manually")
        print("2. Read text from a file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\nEnter your text (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
            
            text = '\n'.join(lines[:-1])  # Remove last empty line
            
            if text.strip():
                analyzer = TextAnalyzer(text)
                analyzer.display_analysis()
            else:
                print("No text entered. Please try again.")
        
        elif choice == '2':
            print("\nOpening file dialog...")
            filename = select_file()
            
            if filename:
                print(f"Selected file: {filename}")
                text = read_from_file(filename)
                
                if text:
                    analyzer = TextAnalyzer(text)
                    analyzer.display_analysis()
            else:
                print("No file selected.")
        
        elif choice == '3':
            print("\nThank you for using Text Analyzer!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()