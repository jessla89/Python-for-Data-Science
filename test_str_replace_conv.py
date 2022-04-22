"""
The following function creates a helper data to test the str_replace_conv
script for the Programming in python for Data Science project
"""

import pandas as pd
from str_replace_conv import str_replace_conv


def test_str_replace_conv():

    # creating an helper data set to tests for the function

    data_dict = {
        "name": ["jesla", "jesma", "jessal"],
        "job": ["teacher", "doctor", "programmer"],
        "income": ["$10,000,000", "$20,000,000", "$30,000,000"],
    }
    helper_data = pd.DataFrame.from_dict(data_dict)

    str_replace_conv(helper_data, "income")

    # Tests the number of rows and columns are correct
    assert helper_data.shape == (3, 3), "incorrect shape for the output"

    # Tests the datatype of the replaced colum is of float64
    assert (
        helper_data["income"].dtype == "float64"
    ), "incorrect data type for the output"
