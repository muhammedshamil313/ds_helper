import pandas as pd
def column_detector(df,threshold=3):
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

data = {
    "Age": [23, 25, 30, 40],
    "Gender": ["M", "F", "M", "F"],
    "Review": ["Good", "Excellent product, very useful!", "Nice", "Bad experience"]
}

df=pd.DataFrame(data)
print(column_detector(df))