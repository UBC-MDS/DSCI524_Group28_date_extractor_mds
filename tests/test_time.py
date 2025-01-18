from datetime import time
from date_extractor_mds.date_extractor_mds import *

def test_extract_time_from_string():
    """Test extracting time from a single ISO 8601 datetime string."""
    iso_date = "2025-01-15T10:20:30"
    result = extract_time(iso_date)
    expected = time(10, 20, 30)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_extract_time_from_series():
    """Test extracting time from a Pandas Series of ISO 8601 datetime strings."""
    iso_dates = pd.Series([
        "2025-01-15T10:20:30",
        "2025-02-25T15:45:00",
        "2025-12-31T08:00:00"
    ])
    result = extract_time(iso_dates)
    expected = pd.Series([time(10, 20, 30), time(15, 45, 0), time(8, 0, 0)], dtype='object')
    pd.testing.assert_series_equal(result, expected)


def test_invalid_iso_date_string():
    """Test invalid ISO 8601 datetime string."""
    invalid_iso_date = "2025-01-XYZT10:20:30"
    try:
        extract_time(invalid_iso_date)
        assert False, "Expected ValueError for invalid date"
    except ValueError:
        pass


def test_invalid_iso_date_series():
    """Test invalid ISO 8601 datetime strings in a Pandas Series."""
    invalid_iso_dates = pd.Series([
        "2025-01-17T10:20:30",
        "2025-02-XYZT15:45:00",
        "2025-12-25T08:00:00"
    ])
    try:
        extract_time(invalid_iso_dates)
        assert False, "Expected ValueError for invalid dates in series"
    except ValueError:
        pass


def test_edge_case_start_of_day():
    """Test extracting time from the start of the day."""
    iso_date = "2025-01-01T00:00:00"
    result = extract_time(iso_date)
    expected = time(0, 0, 0)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_edge_case_end_of_day():
    """Test extracting time from the end of the day."""
    iso_date = "2025-01-01T23:59:59"
    result = extract_time(iso_date)
    expected = time(23, 59, 59)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_empty_string():
    """Test handling of an empty string."""
    iso_date = ""
    try:
        extract_time(iso_date)
        assert False, "Expected ValueError for empty string"
    except ValueError:
        pass


def test_invalid_type():
    """Test invalid input type."""
    invalid_input = 12345  # integer input, not a string or Series
    try:
        extract_time(invalid_input)
        assert False, "Expected TypeError for invalid input type"
    except TypeError:
        pass


def test_invalid_iso8601_format():
    """Test invalid ISO 8601 format strings."""
    invalid_dates = [
        "2025-01-01T12:00",   # Missing seconds
        "2025/01/01T12:00:00",  # Invalid separator
        "2025-01-01T25:00:00"   # Invalid hour
    ]
    for date in invalid_dates:
        try:
            extract_time(date)
            assert False, f"Expected ValueError for invalid date format {date}"
        except ValueError:
            pass
