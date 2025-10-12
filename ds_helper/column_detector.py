import pandas as pd
def detect_column_types(df,threshold=3):
    column_types={}
    for col in df.columns:
        unique_vals=df[col].nunique(dropna=True)
        dtype=df[col].dtype
        if unique_vals<threshold:
            column_types[col]="categorical"
        elif pd.api.types.is_numeric_dtype(dtype):
            column_types[col]="numerical"
        elif pd.api.types.is_string_dtype(dtype):
            avg_len=df[col].astype(str).str.len().mean()
            if avg_len>10:
                column_types[col]="text"
            else:
                column_types[col]="categorical"
        else:
            column_types[col]="unknown"
    return column_types



df = pd.DataFrame({
        "Age": [23, 25, 30, 40, 29, 35],
        "Salary": [3000, 3500, 4000, 4200, 5000, 5500],  # another numerical col
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
print(detect_column_types(df))