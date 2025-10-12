# ds_helper Library

### Created by: **Muhammed Shamil**  
### Course: **BCAP204 – Data Science Project**  
---

##  Project Overview

**ds_helper** is a lightweight and reusable Python library designed to simplify **data analysis and preprocessing** tasks.  
It integrates three key modules — `column_detector`, `auto_visualizer`, and `text_cleaner` — to help identify data types, visualize datasets automatically, and clean text data efficiently.

This project demonstrates **modular programming** and **open-source library structure** development as part of the BCAP204 coursework.

---

##  Modules in the Library

###  1. `column_detector`
- Detects column types in a DataFrame (numerical, categorical, or text).
- Helps in selecting the correct preprocessing or visualization method.

###  2. `auto_visualizer`
- Automatically generates relevant visualizations for each column type.
- Creates:
  - **Numerical** → Histogram, Boxplot, Scatter plot  
  - **Categorical** → Count plot, Bar chart  
  - **Text** → Word cloud, Top word frequency chart  

###  3. `text_cleaner`
- Cleans and preprocesses text data.
- Features:
  - Converts text to lowercase  
  - Removes punctuation and filler words  
  - Removes stopwords  
  - Applies lemmatization (via NLTK)

---

##  Installation Steps

1. Open **PowerShell** or **Command Prompt**.
2. Navigate to your project folder:
   ```bash
   cd "C:\Users\shami\OneDrive\Desktop\ds_helper"
Install the package locally:

pip install .
Install required dependencies (if not already installed):

pip install pandas matplotlib seaborn wordcloud nltk
(Optional) Download NLTK data for text processing:

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

 Usage Example
import pandas as pd
from ds_helper import detect_column_types, visualize, TextCleaner

## Example dataset
df = pd.DataFrame({
    "Age": [23, 25, 30, 40, 29, 35],
    "Salary": [3000, 3500, 4000, 4200, 5000, 5500],
    "Gender": ["M", "F", "M", "M", "F", "F"],
    "Review": [
        "Good product",
        "Excellent service and fast delivery",
        "Bad experience",
        "Nice",
        "Very useful and handy",
        "Average quality"
    ]
})

### 1️⃣ Detect column types
print(detect_column_types(df))

### 2️⃣ Visualize the data automatically
visualize(df)

### 3️⃣ Clean text data
cleaner = TextCleaner()
cleaned_df = cleaner.clean_dataframe(df, ["Review"])
print(cleaned_df)

 Test with Real Dataset (Example)
You can test ds_helper using a built-in dataset from Seaborn (e.g., Titanic):

import seaborn as sns
from ds_helper import detect_column_types, visualize, TextCleaner

titanic = sns.load_dataset("titanic")

### Detect types
print(detect_column_types(titanic))

### Visualize data
visualize(titanic)

### Clean sample text column
sample = titanic[["who", "embarked"]].dropna().head(5)
cleaner = TextCleaner()
print(cleaner.clean_dataframe(sample, ["who"]))

 Project Structure
markdown
Copy code
ds_helper/
│
├── setup.py
├── README.md
├── test_script.py
│
└── ds_helper/
    ├── __init__.py
    ├── column_detector.py
    ├── auto_visualizer.py
    └── text_cleaner.py
