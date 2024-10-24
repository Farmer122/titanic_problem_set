def add_family_size(df, sibsp_col='SibSp', parch_col='Parch'):
    """
    Adds a 'Family Size' column to the DataFrame based on 'SibSp' and 'Parch' columns.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to modify.
    - sibsp_col (str): The name of the column representing siblings/spouses. Default is 'SibSp'.
    - parch_col (str): The name of the column representing parents/children. Default is 'Parch'.
    
    Returns:
    - pd.DataFrame: The DataFrame with the added 'Family Size' column.
    """
    df['Family Size'] = df[sibsp_col] + df[parch_col] + 1
    return df


def add_age_interval(df, age_col='Age', interval_col='Age Interval'):
    """
    Adds an 'Age Interval' column to the DataFrame based on age ranges.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to modify.
    - age_col (str): The name of the column representing age. Default is 'Age'.
    - interval_col (str): The name of the column to store the age intervals. Default is 'Age Interval'.
    
    Returns:
    - pd.DataFrame: The DataFrame with the added 'Age Interval' column.
    """
    # Initialize the interval column with a default value
    df[interval_col] = 0.0

    # Assign intervals based on age ranges
    df.loc[df[age_col] <= 16, interval_col] = 0
    df.loc[(df[age_col] > 16) & (df[age_col] <= 32), interval_col] = 1
    df.loc[(df[age_col] > 32) & (df[age_col] <= 48), interval_col] = 2
    df.loc[(df[age_col] > 48) & (df[age_col] <= 64), interval_col] = 3
    df.loc[df[age_col] > 64, interval_col] = 4

    return df

def add_fare_interval(df, fare_col='Fare', interval_col='Fare Interval'):
    """
    Adds a 'Fare Interval' column to the DataFrame based on fare ranges.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to modify.
    - fare_col (str): The name of the column representing fare. Default is 'Fare'.
    - interval_col (str): The name of the column to store the fare intervals. Default is 'Fare Interval'.
    
    Returns:
    - pd.DataFrame: The DataFrame with the added 'Fare Interval' column.
    """
    # Initialize the interval column with a default value
    df[interval_col] = 0.0

    # Assign intervals based on fare ranges
    df.loc[df[fare_col] <= 7.91, interval_col] = 0
    df.loc[(df[fare_col] > 7.91) & (df[fare_col] <= 14.454), interval_col] = 1
    df.loc[(df[fare_col] > 14.454) & (df[fare_col] <= 31), interval_col] = 2
    df.loc[df[fare_col] > 31, interval_col] = 3

    return df



