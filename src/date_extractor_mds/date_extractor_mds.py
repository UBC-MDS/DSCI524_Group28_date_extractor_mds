def extract_year(iso_date: str) -> int:
    """
    Extract the year from an ISO 8601 date string.

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
    >>> extract_year("2023-07-16T12:34:56")
    2023
    """
    pass


def extract_month(iso_date: str) -> int:
    """
    Extract the month from an ISO 8601 date string.

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
    """
    pass


def extract_day(iso_date: str) -> int:
    """
    Extract the day from an ISO 8601 date string.

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
    """
    pass


def extract_time(iso_date: str) -> str:
    """
    Extract the time from an ISO 8601 date string.

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
    >>> extract_time("2023-07-16T12:34:56")
    '12:34:56'
    """
    pass