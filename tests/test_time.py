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
