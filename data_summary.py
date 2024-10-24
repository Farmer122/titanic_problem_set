import pandas as pd
import numpy as np

def summarize_frequent_items(df):
    """
    Summarizes the most frequent items in each column of a DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the total count, most frequent item,
                    its frequency, and its percentage from the total for each column.
    """
    # Calculate total non-missing counts for each column
    total = df.count()
    tt = pd.DataFrame(total, columns=['Total'])
    
    # Initialize lists to store the most frequent item and its frequency
    items = []
    vals = []
    
    # Loop through each column to find the most frequent item and its count
    for col in df.columns:
        try:
            itm = df[col].value_counts().index[0]
            val = df[col].value_counts().values[0]
        except Exception as ex:
            print(f"Error processing column {col}: {ex}")
            itm, val = 0, 0
        
        items.append(itm)
        vals.append(val)
    
    # Add the most frequent item, its frequency, and the percentage from total to the DataFrame
    tt['Most frequent item'] = items
    tt['Frequency'] = vals
    tt['Percent from total'] = np.round(vals / total * 100, 3)
    
    return tt.transpose()


def summarize_unique_counts(df):
    """
    Summarizes the unique counts in each column of a DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the total count of non-missing values 
                    and the number of unique values for each column.
    """
    # Calculate total non-missing counts for each column
    total = df.count()
    tt = pd.DataFrame(total, columns=['Total'])
    
    # Calculate the number of unique values for each column
    uniques = [df[col].nunique() for col in df.columns]
    tt['Uniques'] = uniques
    
    # Transpose the DataFrame for better readability
    return tt.transpose()



def summarize_missing_values(df):
    """
    Summarizes missing values in a DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the total missing values, 
                    percentage of missing values, and data types for each column.
    """
    total = df.isnull().sum()
    percent = (df.isnull().sum() / df.isnull().count() * 100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
    # Get the data types of each column
    tt['Types'] = df.dtypes.astype(str)
    
    return tt.transpose()

