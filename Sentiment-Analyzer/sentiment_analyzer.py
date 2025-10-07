"""
Sentiment Analyzer Tool
Analyzes text sentiment (positive, negative, or neutral) using TextBlob library.
"""

from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.

    Args:
        text (str): The text to analyze

    Returns:
        dict: Contains sentiment label, polarity score, and subjectivity score
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Determine sentiment label
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }


def analyze_from_file(filename):
    """
    Analyze sentiment from a text file.

    Args:
        filename (str): Path to the text file

    Returns:
        dict: Sentiment analysis results
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        return analyze_sentiment(text)
    except FileNotFoundError:
        return {"error": f"File '{filename}' not found"}
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}


def main():
    """Main function to run the sentiment analyzer."""
    print("=" * 50)
    print("Sentiment Analyzer Tool")
    print("=" * 50)
    print("\nChoose an option:")
    print("1. Analyze text input")
    print("2. Analyze text from file")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        print("\nEnter your text (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        text = " ".join(lines)

        if text.strip():
            result = analyze_sentiment(text)
            print("\n" + "=" * 50)
            print("Analysis Results:")
            print("=" * 50)
            print(f"Sentiment: {result['sentiment']}")
            print(f"Polarity Score: {result['polarity']} (Range: -1 to 1)")
            print(f"Subjectivity Score: {result['subjectivity']} (Range: 0 to 1)")
            print("\nNote:")
            print("- Polarity: Negative values = negative sentiment, Positive values = positive sentiment")
            print("- Subjectivity: 0 = objective, 1 = subjective")
        else:
            print("\nError: No text provided!")

    elif choice == "2":
        filename = input("\nEnter the filename: ").strip()
        result = analyze_from_file(filename)

        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\n" + "=" * 50)
            print("Analysis Results:")
            print("=" * 50)
            print(f"Sentiment: {result['sentiment']}")
            print(f"Polarity Score: {result['polarity']} (Range: -1 to 1)")
            print(f"Subjectivity Score: {result['subjectivity']} (Range: 0 to 1)")
            print("\nNote:")
            print("- Polarity: Negative values = negative sentiment, Positive values = positive sentiment")
            print("- Subjectivity: 0 = objective, 1 = subjective")

    elif choice == "3":
        print("\nThank you for using Sentiment Analyzer!")
        return

    else:
        print("\nInvalid choice! Please run the program again.")


if __name__ == "__main__":
    main()
