# Sentiment Analyzer Tool

A Python-based sentiment analysis tool that analyzes text to determine whether it expresses positive, negative, or neutral sentiment.

## Features

- **Text Input Analysis**: Analyze sentiment from direct text input
- **File Analysis**: Analyze sentiment from text files
- **Detailed Metrics**: Provides polarity and subjectivity scores
- **User-Friendly**: Simple command-line interface

## How It Works

The tool uses the TextBlob library for natural language processing to:
1. Analyze the polarity of text (positive vs negative)
2. Measure subjectivity (objective vs subjective)
3. Classify overall sentiment as Positive, Negative, or Neutral

### Sentiment Scores

- **Polarity**: Ranges from -1 (most negative) to 1 (most positive)
  - Positive sentiment: polarity > 0.1
  - Negative sentiment: polarity < -0.1
  - Neutral sentiment: -0.1 ≤ polarity ≤ 0.1

- **Subjectivity**: Ranges from 0 (objective) to 1 (subjective)

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Download TextBlob corpora (first-time setup):

```bash
python -m textblob.download_corpora
```

## Usage

Run the program:

```bash
python sentiment_analyzer.py
```

### Option 1: Analyze Text Input

1. Select option 1
2. Enter or paste your text
3. Press Enter twice to finish
4. View the sentiment analysis results

Example:
```
Enter your text (press Enter twice to finish):
I love this product! It's amazing and works perfectly.

Analysis Results:
Sentiment: Positive
Polarity Score: 0.65
Subjectivity Score: 0.85
```

### Option 2: Analyze Text from File

1. Select option 2
2. Enter the path to your text file
3. View the sentiment analysis results

Example:
```
Enter the filename: review.txt

Analysis Results:
Sentiment: Negative
Polarity Score: -0.45
Subjectivity Score: 0.60
```

## Use Cases

- **Product Reviews**: Analyze customer feedback and reviews
- **Social Media**: Understand sentiment in tweets, posts, and comments
- **Customer Support**: Analyze support tickets and emails
- **Content Analysis**: Evaluate tone of articles and documents
- **Learning**: Educational tool for understanding NLP and sentiment analysis

## Requirements

- Python 3.6 or higher
- textblob library (see requirements.txt)

## Example Outputs

**Positive Text:**
```
Text: "This is the best day ever! I'm so happy and excited!"
Sentiment: Positive
Polarity: 0.85
Subjectivity: 1.0
```

**Negative Text:**
```
Text: "I'm disappointed and frustrated with this terrible experience."
Sentiment: Negative
Polarity: -0.75
Subjectivity: 0.90
```

**Neutral Text:**
```
Text: "The meeting is scheduled for 3 PM in the conference room."
Sentiment: Neutral
Polarity: 0.0
Subjectivity: 0.0
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this tool.

## License

This project is part of the PyVerse collection and follows the repository's license.
