import pytest
import pandas as pd
from datetime import datetime
from date_extractor_mds.date_extractor_mds import *


def test_extract_month_from_string():
    """Test extracting month from a single ISO 8601 date string."""
    iso_date = "2025-01-15T10:20:30"
    result = extract_month(iso_date)
    expected = 1
    assert result == expected, f"Expected {expected}, but got {result}"


def test_extract_month_from_series():
    """Test extracting month from a Pandas Series of ISO 8601 date strings."""
    iso_dates = pd.Series([
        "2025-01-15T10:20:30",
        "2025-02-25T15:45:00",
        "2025-12-31T08:00:00"
    ])
    result = extract_month(iso_dates)
    expected = pd.Series([1, 2, 12], dtype='int64')
    pd.testing.assert_series_equal(result, expected)


def test_invalid_iso_date_string():
    """Test invalid ISO 8601 date string."""
    invalid_iso_date = "2025-01-XYZT10:20:30"
    try:
        extract_month(invalid_iso_date)
        assert False, "Expected ValueError for invalid date"
    except ValueError:
        pass


def test_invalid_iso_date_series():
    """Test invalid ISO 8601 date strings in a Pandas Series."""
    try:
        invalid_iso_dates = pd.Series([
            "2025-01-15T10:20:30",
            "invalid_date",
            "2025-12-31T08:00:00"
        ])
        result = extract_month(invalid_iso_dates)
        expected = pd.Series([1, float('nan'), 12])
        pd.testing.assert_series_equal(result, expected)
    except ValueError:
        pass


def test_empty_string():
    """Test handling of an empty string."""
    iso_date = ""
    try:
        extract_month(iso_date)
        assert False, "Expected ValueError for empty string"
    except ValueError:
        pass


def test_invalid_type():
    """Test invalid input type."""
    invalid_input = 12345  # integer input, not a string or Series
    try:
        extract_month(invalid_input)
        assert False, "Expected ValueError for invalid input type"
    except TypeError:
        pass


def test_edge_case_february_leap_year():
    """Test extracting month for a leap year date."""
    iso_date = "2024-02-29T12:00:00"
    result = extract_month(iso_date)
    expected = 2
    assert result == expected, f"Expected {expected}, but got {result}"


def test_edge_case_february_non_leap_year():
    """Test extracting month for a non-leap year February."""
    iso_date = "2023-02-28T12:00:00"
    result = extract_month(iso_date)
    expected = 2
    assert result == expected, f"Expected {expected}, but got {result}"
