import pandas as pd

from datetime import datetime

def extract_year(iso_date: str) -> int:
    """
    Extract the year from an ISO 8601 date string.

    This function can be applied to individual strings or used on Pandas 
    DataFrame columns via the Pandas `apply` method.

    Parameters
    ----------
    iso_date : str
        A date string in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    int
        The year as a four-digit integer.

    Examples
    --------
    Extract the year from a single date string:

    >>> extract_year("2023-07-16T12:34:56")
    2023

    Apply the function to a Pandas DataFrame column:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> df['years'] = df['dates'].apply(extract_year)
    >>> print(df)
                     dates  years
    0  2023-07-16T12:34:56   2023
    1  2024-03-25T08:15:30   2024
    """
    pass


def extract_month(input_data) -> str:
    """
    Extract the month from an ISO 8601 date string or a DataFrame column.

    This function accepts either an individual string, or a Pandas Series.

    Parameters
    ----------
    input_data : str or pandas.Series
        A single ISO 8601 date string (YYYY-MM-DDThh:mm:ss) or a Pandas Series 
        containing a column with such date strings.

    Returns
    -------
    int or pandas.Series
        If input is a string, returns the month as an integer (1-12).
        If input is a pandas.Series, returns a Pandas Series with the extracted months.

    Examples
    --------
    Extract the month from a single ISO 8601 string:
    
    >>> extract_month("2023-07-16T12:34:56")
    7

    Process a Pandas Series column containing ISO 8601 strings:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T12:34:56"]}
    >>> df = pd.DataFrame(data)
    >>> months = extract_month(df["dates"])
    >>> print(months)
    0    7.0
    1    3.0
    dtype: float64
    """
    # Validate the datetime input
    validate_datetime(input_data)

    # Define function to extract a single datetime string
    def extract_single_month(datetime_str):
        # Given a valid ISO 8601 format string, return the time as a datetime
        time_obj = datetime.strptime(datetime_str.split('T')[0], "%Y-%m-%d")

        return time_obj.month

    if isinstance(input_data, str):
        return extract_single_month(input_data)
    elif isinstance(input_data, pd.Series):
        return input_data.apply(extract_single_month)
    else:
        raise ValueError("Input must be a string or a pandas Series")


def extract_day(iso_date: str) -> int:
    """
    Extract the day from an ISO 8601 date string.
    This function can handle both individual strings and Pandas DataFrame columns via the Pandas `apply` method.

    Parameters
    ----------
    iso_date : str
        A date string in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    int
        The day as an integer (1-31).

    Examples
    --------
    >>> extract_day("2023-07-16T12:34:56")
    16
    Apply the function to a Pandas DataFrame column:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> df['days'] = df['dates'].apply(extract_day)
    >>> print(df)
                     dates  days
    0  2023-07-16T12:34:56    16
    1  2024-03-25T08:15:30    25
    """
    pass


def extract_time(iso_date: str) -> str:
    """
    Extract the time from an ISO 8601 date string.
    
    This function can be applied to individual strings or used on Pandas 
    DataFrame columns via the Pandas `apply` method.


    This function can be applied to individual strings or used on Pandas 
    DataFrame columns via the Pandas `apply` method.

    Parameters
    ----------
    iso_date : str
        A date string in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    str
        The time as a string in the format hh:mm:ss.

      Examples
    --------
    Extract the time from a single date string:

    >>> extract_time("2023-07-16T12:34:56")
    '12:34:56'

    Apply the function to a Pandas DataFrame column:
    
    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> df['time'] = df['dates'].apply(extract_time)
    >>> print(df)
                     dates      time
    0  2023-07-16T12:34:56  12:34:56
    1  2024-03-25T08:15:30  08:15:30
    """

    pass

    