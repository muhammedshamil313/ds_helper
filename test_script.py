import seaborn as sns
from ds_helper import detect_column_types, visualize, TextCleaner

titanic = sns.load_dataset("titanic")

print(detect_column_types(titanic))

visualize(titanic)

sample = titanic[["embarked", "class", "who"]].dropna().head(5)
cleaner = TextCleaner()
print(cleaner.clean_dataframe(sample, ["who"]))
