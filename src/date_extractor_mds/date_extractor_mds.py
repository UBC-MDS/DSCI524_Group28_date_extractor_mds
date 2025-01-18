import pandas as pd
import re
from datetime import datetime

def validate_datetime(input_value):
    """
    Validates whether the input is either:
    1. A string containing a date in ISO 8601 format (YYYY-MM-DDThh:mm:ss), or
    2. A Pandas Series containing strings in ISO 8601 format (YYYY-MM-DDThh:mm:ss).
    
    If the input does not satisfy these conditions, the function raises:
    - TypeError: If the input is not a string or a Pandas Series.
    - ValueError: If the input string or one or more elements in the Series do not match the ISO 8601 format.
    - ValueError: If the Series contains non-string elements.
    
    Parameters:
    - input_value (str or pandas.Series): The input to validate.
    
    Returns:
    - None: This function does not return a value. It stops execution by raising an exception if validation fails.
    """
    def is_iso8601_compliant(date_str):
        """
        Checks if a single string is in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

        Parameters:
        - date_str (str): The string to check.

        Returns:
        - bool: True if the string matches the ISO 8601 format, False otherwise.
        """
        iso8601_regex = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$"
        return bool(re.match(iso8601_regex, date_str))
    
    if isinstance(input_value, str):
        # If input is a string, validate directly
        if not is_iso8601_compliant(input_value):
            raise ValueError(f"The input string '{input_value}' is not in valid ISO 8601 format.")
    elif isinstance(input_value, pd.Series):
        # If input is a Series, validate each element
        if not all(isinstance(item, str) for item in input_value):
            raise ValueError("All elements of the Pandas Series must be strings.")
        if not input_value.apply(is_iso8601_compliant).all():
            raise ValueError("One or more elements in the Pandas Series are not in valid ISO 8601 format.")
    else:
        # Raise error if input is neither string nor Series
        raise TypeError("Input must be either a string or a Pandas Series of strings.")

def extract_year(iso_date: str) -> int:
    """
    Extract the year from an ISO 8601 date string.

    This function accepts either an individual string, or
    a Pandas Series.

    Parameters
    ----------
    iso_date : str or pandas.Series
        A date string, or Pandas Series containing strings,
        in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    int (if input was string)
        The year as a four-digit integer.
    pandas.Series (if input was pandas.Series)
        A pandas.Series containing years as four-digit integers.

    Examples
    --------
    Extract the year from a single date string:

    >>> extract_year("2023-07-16T12:34:56")
    2023

    Apply the function to a Pandas Series:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> year = extract_year(df['dates'])
    >>> print(year)
    0    2023
    1    2024
    Name: dates, dtype: int64
    """
    validate_datetime(iso_date)
    return int(iso_date.split("-")[0])


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


def extract_day(datetime_input):
    """
    Extract the day from an ISO 8601 date string.

    This function can handle both individual strings and Pandas Series.

    Parameters
    ----------
    iso_date : str or pandas.Series
        A date string, or Pandas Series containing strings,
        in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    int
        The day as an integer (1-31)(if input was string)
        
    pandas.Series (if input was pandas.Series)
        A pandas.Series containing day as two-digit integers.

    Examples
    --------
    >>> extract_day("2023-07-16T12:34:56")
    16
    

    Apply the function to a Pandas Series:

    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> day = extract_day(df['dates'])
    >>> print(day)
    0    2023
    1    2024
    Name: dates, dtype: int64
    """
    # Validate the input if it's a string
    if isinstance(iso_date, str):
        validate_datetime(iso_date)  # Validate fuction
        return int(iso_date[8:10])  # Extract the day  from the string
    
    # If the input is a pandas Series
    elif isinstance(iso_date, pd.Series):
        iso_date.apply(validate_datetime)  # Validate  fuction
        return iso_date.apply(lambda x: int(x[8:10])) 
    
    """
    pass


def extract_time(datetime_input) -> str:
    """
    Extract the time from an ISO 8601 datetime string or a Pandas Series of ISO 8601 datetime strings.
    
    This function accepts either an individual string, or a Pandas Series.

    Parameters
    ----------
    iso_date : str or pandas.Series
        A datetime string, or a Pandas Series containing datetime strings,
        in ISO 8601 format (YYYY-MM-DDThh:mm:ss).

    Returns
    -------
    datetime.time (if input was string)
        The time as a datetime.time object.
    pandas.Series (if input was pandas.Series)
        A pandas.Series containing rows of datetime.time objects.

    Examples
    --------
    Extract the time from a single date string:

    >>> extract_time("2023-07-16T12:34:56")
    datetime.time(12, 34, 56)

    Apply the function to a Pandas DataFrame column:
    
    >>> import pandas as pd
    >>> data = {'dates': ["2023-07-16T12:34:56", "2024-03-25T08:15:30"]}
    >>> df = pd.DataFrame(data)
    >>> times = extract_time(df['dates'])
    >>> print(times)
    0    12:34:56
    1    08:15:30
    Name: dates, dtype: object
    """
    validate_datetime(datetime_input)

    def extract_single_time(datetime_str):
        # Given a valid ISO 8601 format string, return the time as a datetime
        time_string = datetime_str.split('T')[1]
        time_obj = datetime.strptime(time_string, "%H:%M:%S").time()

        return time_obj

    if isinstance(datetime_input, str):
        return extract_single_time(datetime_input)
    elif isinstance(datetime_input, pd.Series):
        return datetime_input.apply(extract_single_time)
    else:
        raise ValueError("Input must be a string or a pandas Series")