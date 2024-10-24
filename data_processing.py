import pandas as pd

def combine_train_test(train_df, test_df, target_column='Survived'):
    """
    Combines the train and test DataFrames into one and adds a column 
    indicating the origin of each row (train or test).
    
    Parameters:
    - train_df (pd.DataFrame): The training DataFrame.
    - test_df (pd.DataFrame): The testing DataFrame.
    - target_column (str): The name of the target column to identify missing values in the test set.
    
    Returns:
    - pd.DataFrame: The combined DataFrame with an additional 'set' column.
    """
    # Concatenate train and test DataFrames
    all_df = pd.concat([train_df, test_df], axis=0)
    
    # Add a 'set' column, defaulting to 'train'
    all_df['set'] = 'train'
    
    # Update 'set' column for rows where the target column is missing
    all_df.loc[all_df[target_column].isna(), 'set'] = 'test'
    
    return all_df

