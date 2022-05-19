def which(df:pd.DataFrame, cond:bool):
    """R which() funciton copycat.  Returns list of indeces 

    Args:
        df (pd.DataFrame): Data Frame or Series object
        cond (bool): conditional expression that we are looking for 'true' answers to

    Returns:
        list: list of indeces where conditional statment is true
        
    Examples:
        atloc = which(df, df.column2 == 'this_string')
        # returns all rows where df.column2 has value 'this_string'
    """
    rows = df[cond].index
    return rows