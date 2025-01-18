import pandas as pd
import pytest
from date_extractor_mds.date_extractor_mds import *


def test_valid_iso_date_string():
    """Test valid ISO 8601 datetime string."""
    valid_iso_date = "2025-01-15T10:20:30"
    try:
        validate_datetime(valid_iso_date)  # Should pass without exceptions
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


def test_valid_iso_date_series():
    """Test valid ISO 8601 datetime strings in a Pandas Series."""
    valid_iso_dates = pd.Series([
        "2025-01-15T10:20:30",
        "2024-12-25T15:45:00",
        "2023-07-16T08:00:00"
    ])
    try:
        validate_datetime(valid_iso_dates)  # Should pass without exceptions
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


def test_invalid_iso_date_string_format():
    """Test invalid ISO 8601 datetime string format."""
    invalid_iso_date = "2025/01/01T10:20:30"  # Invalid separator
    with pytest.raises(ValueError, match="is not in valid ISO 8601 format"):
        validate_datetime(invalid_iso_date)


def test_invalid_iso_date_string_content():
    """Test ISO 8601 datetime string with invalid content."""
    invalid_iso_date = "2025-01-XYZT10:20:30"  # Invalid date component
    with pytest.raises(ValueError, match="is not in valid ISO 8601 format"):
        validate_datetime(invalid_iso_date)


def test_invalid_iso_date_series_format():
    """Test invalid ISO 8601 datetime strings in a Pandas Series."""
    invalid_iso_dates = pd.Series([
        "2025-01-15T10:20:30",  # Valid
        "invalid-date",          # Completely invalid
        "2024/12/25T15:45:00"    # Invalid separator
    ])
    with pytest.raises(ValueError, match="One or more elements in the Pandas Series are not in valid ISO 8601 format"):
        validate_datetime(invalid_iso_dates)


def test_non_string_in_series():
    """Test a Pandas Series containing non-string elements."""
    invalid_iso_dates = pd.Series([
        "2025-01-15T10:20:30",  # Valid
        12345,                   # Invalid: non-string
        "2024-12-25T15:45:00"    # Valid
    ])
    with pytest.raises(ValueError, match="All elements of the Pandas Series must be strings"):
        validate_datetime(invalid_iso_dates)


def test_empty_string():
    """Test handling of an empty string."""
    invalid_iso_date = ""
    with pytest.raises(ValueError, match="is not in valid ISO 8601 format"):
        validate_datetime(invalid_iso_date)


def test_empty_series():
    """Test handling of an empty Pandas Series."""
    empty_series = pd.Series([], dtype="object")
    try:
        validate_datetime(empty_series)  # Should pass without exceptions
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


def test_invalid_type():
    """Test invalid input type."""
    invalid_input = 12345  # Integer input, not a string or Series
    with pytest.raises(TypeError, match="Input must be either a string or a Pandas Series of strings"):
        validate_datetime(invalid_input)