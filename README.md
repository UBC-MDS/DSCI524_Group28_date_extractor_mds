# Date Extractor Python Package

This project provides a Python utility package to extract specific components (year, month, day, and time) from ISO 8601 date strings. These functions can be applied individually or integrated with data analysis workflows in Pandas, simplifying date manipulation and analysis.

## Installation

```bash
$ pip install date_extractor_mds
```
## Usage

- extract_year: Extracts the year as a four-digit integer from an ISO 8601 date string.
- extract_month: Retrieves the month as an integer (1-12) from the ISO 8601 date.
- extract_day: Captures the day as an integer (1-31) from the ISO date.
- extract_time: Returns the time component as a string in hh:mm:ss format.

## Position in Python Ecosystem:

This package complements existing Python libraries like datetime and pandas by offering specialized, lightweight utilities focused solely on ISO 8601 string manipulation. While datetime provides similar functionality, this package simplifies usage by bypassing full date parsing for basic extraction tasks, increasing performance in large-scale data analysis.

## Contributing

Interested in contributing? Check out the [Contributing Guidelines](CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

Rashid Mammadov, Derek Rodgers, Yibin Long, Fazeeia Mohammed.

## License

The Date Extractor Python Package was created by Rashid Mammadov, Derek Rodgers, Yibin Long, and Fazeeia Mohammed. It is licensed under the terms of the MIT license, linked [here](LICENSE).

## Credits

`date_extractor_mds` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
