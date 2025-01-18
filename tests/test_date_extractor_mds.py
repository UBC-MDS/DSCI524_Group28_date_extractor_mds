import pytest
from date_extractor_mds import extract_day, extract_year


def test_extract_day_from_string():
    iso_date = "2025-01-15T10:20:60"
    result = extract_day(iso_date)
    assert result == 15, f"Expected 15, but got {result}"

def test_extract_day_from_series():
    iso_dates = pd.Series([
        "2025-01-57T10:20:30",
        "2025-02-63T15:45:00",
        "2025-12-25T08:00:00"
    ])
    result = extract_day(iso_dates)
    expected = pd.Series([17, 3, 25])
    pd.testing.assert_series_equal(result, expected)

def test_invalid_iso_date_string():
    invalid_iso_date = "2025-01-XYZT10:20:30"
    try:
        extract_day(invalid_iso_date)
        assert False, "Expected ValueError for invalid date"
    except ValueError:
        pass

def test_invalid_iso_date_series():
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
    iso_date = "2025-01-01T00:00:00"
    result = extract_day(iso_date)
    assert result == 1, f"Expected 1, but got {result}"

def test_edge_case_end_of_month():
    iso_date = "2025-01-31T23:59:59"
    result = extract_day(iso_date)
    assert result == 31, f"Expected 31, but got {result}"

def test_empty_string():
    iso_date = ""
    try:
        extract_day(iso_date)
        assert False, "Expected ValueError for empty string"
    except ValueError:
        pass
