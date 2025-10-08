# Text Analyzer 📝

A Python-based text analysis tool that provides comprehensive statistics and insights about any text document or manual input.

## Features ✨

- **Word Count** - Count total number of words in the text
- **Character Count** - Count all characters including spaces and punctuation
- **Sentence Count** - Automatically detect and count sentences
- **Most Common Words** - Identify frequently used words with their frequencies
- **Dual Input Methods** - Analyze text entered manually or read from a file
- **Stop Words Filtering** - Excludes common words for more meaningful analysis

## Requirements 📋

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

### Checking Your Python Version

```bash
python --version
```

or

```bash
python3 --version
```

### Option 1: Manual Text Entry

1. Select option `1` from the menu
2. Type or paste your text
3. Press **Enter twice** when finished
4. View the analysis results

### Option 2: File Upload

1. Select option `2` from the menu
2. A file browser window will open automatically
3. Navigate to and select your text file
4. View the analysis results

### Option 3: Exit

Select option `3` to close the program

## Example Output 📊

```
==================================================
TEXT ANALYSIS RESULTS
==================================================

Total Characters: 523
Total Words: 98
Total Sentences: 5

Most Common Words:
------------------------------
1. 'python' - 12 times
2. 'text' - 8 times
3. 'analysis' - 7 times
4. 'program' - 5 times
5. 'file' - 4 times
==================================================
```

## How It Works 🔧

### TextAnalyzer Class

The core `TextAnalyzer` class handles all text processing:

- **`_extract_words()`** - Extracts words using regex, converting to lowercase
- **`count_words()`** - Returns total word count
- **`count_characters()`** - Returns total character count
- **`count_sentences()`** - Splits text by sentence delimiters (. ! ?)
- **`most_common_words(n)`** - Returns the n most frequent words
- **`display_analysis()`** - Prints formatted analysis results

### Stop Words

The analyzer filters out common English stop words for more meaningful results:
- Articles: the, a, an
- Conjunctions: and, or, but
- Prepositions: in, on, at, to, for, of, with
- Common verbs: is, it

## File Support 📄

Supported file types:
- `.txt` files (recommended)
- Any text-based files (`.md`, `.csv`, `.log`, etc.)

**Note:** The analyzer works best with plain text files. Rich text formats (`.docx`, `.pdf`) are not supported.

**Happy Analyzing!** 🎉