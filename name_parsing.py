import pandas as pd

def parse_names(row):

    try:
        text = row["Name"]
        split_text = text.split(",")
        family_name = split_text[0]
        next_text = split_text[1]
        split_text = next_text.split(".")
        title = (split_text[0] + ".").strip()
        next_text = split_text[1]

        if "(" in next_text:
            split_text = next_text.split("(")
            given_name = split_text[0].strip()
            maiden_name = split_text[1].rstrip(")").strip()
            return pd.Series([family_name, title, given_name, maiden_name])
        else:
            given_name = next_text.strip()
            return pd.Series([family_name, title, given_name, None])
    except Exception as ex:
        print(f"Exception: {ex}")
        return pd.Series([None, None, None, None])


def add_parsed_name_columns(df, parse_func, name_col='Name'):
    """
    Applies a name-parsing function to a DataFrame and adds columns for
    family name, title, given name, and maiden name.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to modify.
    - parse_func (function): The function used to parse the name.
    - name_col (str): The name of the column containing names. Default is 'Name'.
    
    Returns:
    - pd.DataFrame: The DataFrame with added columns for parsed name components.
    """
    # Apply the parsing function and create new columns for parsed names
    df[["Family Name", "Title", "Given Name", "Maiden Name"]] = df.apply(parse_func, axis=1)
    return df