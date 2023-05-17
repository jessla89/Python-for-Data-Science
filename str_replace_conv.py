import pandas as pd


def str_replace_conv(data, replace_col):
    """
    Given a dataframe, a column, return a dataframe for which the
    column values are converted from string with special characters
    to floating point and the value is divided by 1000000 to give
    the per million value when the function is applied.

    Parameters
    ----------
    data: pandas.core.frame.Dataframe
          The dataframe to sample from
    replace_col: str
          The column whose str data is to be convereted to floating
          point value and the value also is divided by 1000000 to give
          per million value

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe with the replace column value replaced to floating
        point value

    Raises
    ------
    TypeError
        If the input argument data is not of the type
        pandas.core.frame.DataFrame
    AssertError
        If the input argument replace_col is not in the data columns

    Examples
    --------
    str_replace_conv(helper_data,'income')
        name	job	 income
    0	ella	teacher	10.0
    1	emma	doctor	20.0
    2	estel	programmer	30.0
    """

    # checks if a dataframe is the type of the object being passed
    # into the data argument
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of the the type DataFrame")

    # checks if the replace_column exists in the DataFrame
    assert (
        replace_col in data.columns
    ), "The replacing columns does not exist in the DataFrame"

    # The characters that are to be replaced in the replace_column
    # are '$' and ',' and is given as a str

    replace_chars = "$,"

    # Using the for loop for replacing characters by iterating
    # through each character is string
    for replace_char in replace_chars:
        data.loc[:, replace_col] = data.loc[:, replace_col].str.replace(
            replace_char, "", regex=True
        )

    # Obtained string without special characters is converted to float
    data.loc[:, replace_col] = data.loc[:, replace_col].astype(float)

    # Obtained value is converted to per million value for further analysis

    data.loc[:, replace_col] = data.loc[:, replace_col] / 1000000
