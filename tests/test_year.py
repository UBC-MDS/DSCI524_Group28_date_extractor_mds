import pandas as pd
import pytest
from date_extractor_mds.date_extractor_mds import *


def test_extract_year_from_string():
    """Test extracting year from a single ISO 8601 datetime string."""
    iso_date = "2025-01-15T10:20:30"
    result = extract_year(iso_date)
    expected = 2025
    assert result == expected, f"Expected {expected}, but got {result}"


def test_extract_year_from_series():
    """Test extracting year from a Pandas Series of ISO 8601 datetime strings."""
    iso_dates = pd.Series([
        "2025-01-15T10:20:30",
        "2024-12-25T15:45:00",
        "2023-07-16T08:00:00"
    ])
    result = extract_year(iso_dates)
    expected = pd.Series([2025, 2024, 2023], dtype='int64')
    pd.testing.assert_series_equal(result, expected)


def test_invalid_iso_date_string():
    """Test invalid ISO 8601 datetime string."""
    invalid_iso_date = "2025-01-XYZT10:20:30"
    with pytest.raises(ValueError, match="is not in valid ISO 8601 format"):
        extract_year(invalid_iso_date)


def test_invalid_iso_date_series():
    """Test invalid ISO 8601 datetime strings in a Pandas Series."""
    invalid_iso_dates = pd.Series([
        "2025-01-17T10:20:30",
        "2025-02-XYZT15:45:00",
        "invalid-date"
    ])
    with pytest.raises(ValueError, match="One or more elements in the Pandas Series are not in valid ISO 8601 format"):
        extract_year(invalid_iso_dates)


def test_edge_case_start_of_year():
    """Test extracting year from the start of the year."""
    iso_date = "2025-01-01T00:00:00"
    result = extract_year(iso_date)
    expected = 2025
    assert result == expected, f"Expected {expected}, but got {result}"


def test_edge_case_end_of_year():
    """Test extracting year from the end of the year."""
    iso_date = "2025-12-31T23:59:59"
    result = extract_year(iso_date)
    expected = 2025
    assert result == expected, f"Expected {expected}, but got {result}"


def test_empty_string():
    """Test handling of an empty string."""
    iso_date = ""
    with pytest.raises(ValueError, match="is not in valid ISO 8601 format"):
        extract_year(iso_date)


def test_invalid_type():
    """Test invalid input type."""
    invalid_input = 12345  # integer input, not a string or Series
    with pytest.raises(TypeError, match="Input must be either a string or a Pandas Series of strings"):
        extract_year(invalid_input)


def test_empty_series():
    """Test handling of an empty Pandas Series."""
    iso_dates = pd.Series([], dtype="object")
    result = extract_year(iso_dates)
    # Match default dtype for empty Series if not explicitly set
    expected = pd.Series([], dtype="int64") if hasattr(result, 'dtype') and result.dtype == "int64" else pd.Series([], dtype="object")
    pd.testing.assert_series_equal(result, expected)