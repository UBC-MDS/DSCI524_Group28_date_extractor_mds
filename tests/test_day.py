import pytest
import pandas as pd
from date_extractor_mds.date_extractor_mds import extract_day

def test_extract_day_from_string():
    """
    Test that the extract_day function correctly extracts the day 
    from a valid ISO 8601 date string.

    The test passes a date string ("2025-01-15T10:20:30") and 
    expects the day to be 15. This ensures the regular use case works

    Raises:
        AssertionError: If the result does not match the expected day.
    """
    iso_date = "2025-01-15T10:20:60"
    result = extract_day(iso_date)
    assert result == 15, f"Expected 15, but got {result}"

def test_extract_day_from_series():
    """
    Test that the extract_day function correctly extracts the day 
    from a Pandas Series of ISO 8601 date strings.

    The test passes a series of valid date strings and expects 
    the function to extract the correct day for each.This ensures the function works on series also. 

    Raises:
        AssertionError: If the extracted days do not match the expected values.
    """
    iso_dates = pd.Series([
        "2025-01-05T10:20:30",
        "2025-02-18T15:45:00",
        "2025-12-25T08:00:00"
    ])
    result = extract_day(iso_dates)
    expected = pd.Series([5, 18, 25])
    pd.testing.assert_series_equal(result, expected)

def test_invalid_iso_date_string():
    """
    Test that the extract_day function raises a ValueError when
    an invalid ISO 8601 date string is provided.

    This test checks for an invalid month in the date string 
    ("2025-01-XYZT10:20:30") to ensure proper error handling.

    Raises:
        ValueError: If the input is an invalid ISO 8601 date string.
    """
    invalid_iso_date = "2025-01-XYZT10:20:30"
    try:
        extract_day(invalid_iso_date)
        assert False, "Expected ValueError for invalid date"
    except ValueError:
        pass

def test_invalid_iso_date_series():
    """
    Test that the extract_day function raises a ValueError when
    a Pandas Series contains invalid ISO 8601 date strings.

    This test checks for an invalid month in one of the date strings 
    ("2025-02-XYZT15:45:00") to ensure proper error handling across the series.

    Raises:
        ValueError: If any element in the Series is an invalid ISO 8601 date string.
    """
    invalid_iso_dates = pd.Series([
        "2025-01-17T10:20:30",
        "2025-02-XYZT15:45:00",
        "2025-12-25T08:00:00"
    ])
    try:
        extract_day(invalid_iso_dates)
        assert False, "Expected ValueError for invalid dates in series"
    except ValueError:
        pass

def test_edge_case_start_of_month():
    """
    Test that the extract_day function correctly handles the edge case 
    for the first day of the month.

    The test passes the date string ("2025-01-01T00:00:00") and expects 
    the day to be 1, which represents the first day of the month.

    Raises:
        AssertionError: If the result does not match the expected day (1).
    """
    iso_date = "2025-01-01T00:00:00"
    result = extract_day(iso_date)
    assert result == 1, f"Expected 1, but got {result}"

def test_edge_case_end_of_month():
    """
    Test that the extract_day function correctly handles the edge case 
    for the last day of the month.

    The test passes the date string ("2025-01-31T23:59:59") and expects 
    the day to be 31, which represents the last day of the month.

    Raises:
        AssertionError: If the result does not match the expected day (31).
    """

    iso_date = "2025-01-31T23:59:59"
    result = extract_day(iso_date)
    assert result == 31, f"Expected 31, but got {result}"

def test_empty_string():
    """
    Test that the extract_day function correctly handles the edge case 
    for an empty string.
    The test passes the date string ("") and expects an error.
    

    Raises:
        Value error for empty string.
    """
    iso_date = ""
    try:
        extract_day(iso_date)
        assert False, "Expected ValueError for empty string"
    except ValueError:
        pass
