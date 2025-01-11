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


def extract_month(iso_date: str) -> int:
    """
    Extract the month from an ISO 8601 date string.
    This function can handle both individual strings and Pandas DataFrame columns via the Pandas `apply` method.

    Parameters
    ----------
    iso_date : str
        A date string in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    int
        The month as an integer (1-12).

    Examples
    --------
    >>> extract_month("2023-07-16T12:34:56")
    7
    Apply the function to a Pandas DataFrame column:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> df['months'] = df['dates'].apply(extract_month)
    >>> print(df)
                     dates  months
    0  2023-07-16T12:34:56       7
    1  2024-03-25T08:15:30       3
    """
    pass


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