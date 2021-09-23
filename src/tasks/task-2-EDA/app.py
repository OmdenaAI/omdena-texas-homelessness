import pandas as pd
def wrangle_with_dt(filepath):
    """
    Wrangle function takes an input of a filepath which contains a date-time,
    outputs a cleaned dataframe
    """
    # Reads in DF from filepath using Pandas
    df = pd.read_csv(filepath, parse_dates=['Fiscal Year Start', 'Fiscal Year End'])
    
    # Seperates the categorical columns
    categorical_cols = df.select_dtypes('object').columns
    
    #Creates threshold for how many times you will allow the same value to show up in multiple columns in a row.
    threshold = 50
    
    #Identify high cardinality columns
    high_card_cols = [col for col in categorical_cols 
                      if df[col].nunique() > threshold]
    
    # Drop high cardinality columns
    df.drop(high_card_cols, axis=1, inplace=True)
    
    # Drop columns with a high number of NaN values
    #df.dropna(axis = 1, thresh = 300, inplace = True)
    # Fill NA values with front fill. Replaces with value ahead of it.
    df.fillna(method='ffill', inplace=True)
    
    return df

def wrangle_without_dt(filepath):
    """
    Wrangle function takes an input of a filepath which does not contains a date-time,
    outputs a cleaned dataframe
    """
    # Reads in DF from filepath using Pandas
    df = pd.read_csv(filepath)
    
    # Seperates the categorical columns
    categorical_cols = df.select_dtypes('object').columns
    
    #Creates threshold for how many times you will allow the same value to show up in multiple columns in a row.
    threshold = 50
    
    #Identify high cardinality columns
    high_card_cols = [col for col in categorical_cols 
                      if df[col].nunique() > threshold]
    
    # Drop high cardinality columns
    df.drop(high_card_cols, axis=1, inplace=True)
    
    # Drop columns with a high number of NaN values
    #df.dropna(axis = 1, thresh = 300, inplace = True)
    # Fill NA values with front fill. Replaces with value ahead of it.
    df.fillna(method='ffill', inplace=True)
    
    return df
