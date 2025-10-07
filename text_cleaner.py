import string
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextCleaner:
    """
    A utility class to clean and preprocess text data.
    Features:
        - Remove punctuation
        - Remove filler words (e.g., "uh", "um", "like")
        - Remove stopwords
        - Lowercasing
        - Lemmatization (optional)
    """

    def __init__(self, remove_stopwords=True, lemmatize=True):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.filler_words = {"uh", "um", "like", "you know", "actually", "basically", "literally"}

    def clean_text(self, text: str) -> str:
        """Clean and preprocess a single string of text."""
        if not isinstance(text, str):
            return ""

        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))

        for filler in self.filler_words:
            pattern = r'\b' + re.escape(filler) + r'\b'
            text = re.sub(pattern, '', text)

        tokens = text.split()

        if self.remove_stopwords:
            tokens = [word for word in tokens if word not in self.stop_words]

        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

        return " ".join(tokens)

    def clean_dataframe(self, df: pd.DataFrame, text_columns: list):
        """Clean text columns in a DataFrame."""
        df_copy = df.copy()
        for col in text_columns:
            df_copy[col] = df_copy[col].astype(str).apply(self.clean_text)
        return df_copy


if __name__ == "__main__":
    df = pd.DataFrame({
        "Review": [
            "Um, I literally think this is like actually a great product!",
            "Uh, the service was bad!",
            "Very useful and handy!",
            "Nice experience.",
        ]
    })

    cleaner = TextCleaner()
    cleaned_df = cleaner.clean_dataframe(df, ["Review"])
    print("Before cleaning:\n", df["Review"])
    print("\nAfter cleaning:\n", cleaned_df["Review"])
