def add_sex_pclass(df, sex_col='Sex', pclass_col='Pclass', new_col='Sex_Pclass'):
    """
    Adds a 'Sex_Pclass' column to the DataFrame by combining the first letter of the 'Sex'
    column and the 'Pclass' value.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to modify.
    - sex_col (str): The name of the column representing sex. Default is 'Sex'.
    - pclass_col (str): The name of the column representing passenger class. Default is 'Pclass'.
    - new_col (str): The name of the new column. Default is 'Sex_Pclass'.
    
    Returns:
    - pd.DataFrame: The DataFrame with the added 'Sex_Pclass' column.
    """
    df[new_col] = df.apply(lambda row: row[sex_col][0].upper() + "_C" + str(row[pclass_col]), axis=1)
    return df


def add_family_type(datasets, size_col='Family Size', type_col='Family Type'):
    """
    Adds a 'Family Type' column to each DataFrame in a list, copying values from 'Family Size'.
    
    Parameters:
    - datasets (list of pd.DataFrame): A list of DataFrames to modify.
    - size_col (str): The name of the column representing family size. Default is 'Family Size'.
    - type_col (str): The name of the new column to store the family type. Default is 'Family Type'.
    
    Returns:
    - list of pd.DataFrame: The list of modified DataFrames with the added 'Family Type' column.
    """
    for df in datasets:
        df[type_col] = df[size_col]
    return datasets



def classify_family_type(datasets, size_col='Family Size', type_col='Family Type'):
    """
    Classifies families into 'Single', 'Small', or 'Large' based on their size 
    and updates the 'Family Type' column for each DataFrame in a list.
    
    Parameters:
    - datasets (list of pd.DataFrame): A list of DataFrames to modify.
    - size_col (str): The name of the column representing family size. Default is 'Family Size'.
    - type_col (str): The name of the column to store the family type. Default is 'Family Type'.
    
    Returns:
    - list of pd.DataFrame: The list of modified DataFrames with updated 'Family Type' classifications.
    """
    for df in datasets:
        df.loc[df[size_col] == 1, type_col] = "Single"
        df.loc[(df[size_col] > 1) & (df[size_col] < 5), type_col] = "Small"
        df.loc[df[size_col] >= 5, type_col] = "Large"
    return datasets


def unify_titles(datasets, title_col='Titles'):
    """
    Unifies common titles in the specified column of each DataFrame in the provided list.
    
    Parameters:
    - datasets (list of pd.DataFrame): A list of DataFrames to modify.
    - title_col (str): The name of the column containing titles. Default is 'Titles'.
    
    Returns:
    - list of pd.DataFrame: The list of modified DataFrames with standardised titles.
    """
    for df in datasets:
        # Unify 'Miss.'
        df[title_col] = df[title_col].replace(['Mlle.', 'Ms.'], 'Miss.')
        # Unify 'Mrs.'
        df[title_col] = df[title_col].replace('Mme.', 'Mrs.')
        # Unify rare titles
        df[title_col] = df[title_col].replace(
            ['Lady.', 'the Countess.', 'Capt.', 'Col.', 'Don.', 'Dr.', 
             'Major.', 'Rev.', 'Sir.', 'Jonkheer.', 'Dona.'], 'Rare'
        )
    return datasets




def calculate_survival_rate_by_title_sex(df, group_cols=['Titles', 'Sex'], target_col='Survived'):
    """
    Groups the DataFrame by specified columns and calculates the mean survival rate.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to group and analyse.
    - group_cols (list of str): The columns to group by. Default is ['Titles', 'Sex'].
    - target_col (str): The column to calculate the mean for. Default is 'Survived'.
    
    Returns:
    - pd.DataFrame: A DataFrame with the mean of the target column for each group.
    """
    return df[group_cols + [target_col]].groupby(group_cols, as_index=False).mean()



def encode_sex_column(datasets, sex_col='Sex', mapping={'female': 1, 'male': 0}):
    """
    Encodes the 'Sex' column in each DataFrame of the provided list using a specified mapping.
    
    Parameters:
    - datasets (list of pd.DataFrame): A list of DataFrames to modify.
    - sex_col (str): The name of the column containing sex values. Default is 'Sex'.
    - mapping (dict): A dictionary specifying how to map the 'Sex' values. Default is {'female': 1, 'male': 0}.
    
    Returns:
    - list of pd.DataFrame: The list of modified DataFrames with the 'Sex' column encoded as integers.
    """
    for df in datasets:
        df[sex_col] = df[sex_col].map(mapping).astype(int)
    return datasets


def split_features_and_target(train_df, valid_df, predictors, target):
    """
    Splits the training and validation DataFrames into feature sets (X) and target arrays (Y).
    
    Parameters:
    - train_df (pd.DataFrame): The training DataFrame.
    - valid_df (pd.DataFrame): The validation DataFrame.
    - predictors (list of str): List of column names to be used as features.
    - target (str): The column name of the target variable.
    
    Returns:
    - tuple: (train_X, train_Y, valid_X, valid_Y)
        - train_X (pd.DataFrame): Features from the training set.
        - train_Y (np.ndarray): Target values from the training set.
        - valid_X (pd.DataFrame): Features from the validation set.
        - valid_Y (np.ndarray): Target values from the validation set.
    """
    train_X = train_df[predictors]
    train_Y = train_df[target].values
    valid_X = valid_df[predictors]
    valid_Y = valid_df[target].values
    
    return train_X, train_Y, valid_X, valid_Y



