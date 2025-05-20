import pandas as pd

def explore_dataframe(df: pd.DataFrame, name: str = "DataFrame"):
    """
    Displays basic info, descriptive statistics, data types, unique values,
    and null values of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to explore.
        name (str): Optional name for the DataFrame, mostly used in print statements.
    """

    print(f"Exploring {name}\n")

    # check dataframe info
    print(f"DataFrame info :\n{df.info()}\n")

    # check descriptive statistics
    print(f"Descriptive statistics: \n{df.describe(include='all')}\n")

    # check the data types
    print(f"Data types: \n{df.dtypes}\n")

    # check for unique values
    print(f"Number of unique values per column: \n{df.nunique()}\n")

    ## check for null values
    nulls = df.isnull().sum()
    print(nulls[nulls > 0] if nulls.sum() > 0 else "No missing values found.")