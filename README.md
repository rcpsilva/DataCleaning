# DataCleaning

![GitHub](https://img.shields.io/github/license/rcpsilva/MLBenchmarks)
![GitHub last commit](https://img.shields.io/github/last-commit/rcpsilva/MLBenchmarks)
![GitHub stars](https://img.shields.io/github/stars/rcpsilva/MLBenchmarks?style=social)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```bash
pip install git+https://github.com/rcpsilva/DataCleaning@main
```

## Usage

```python
from DataCleaning.datacleaner import DataCleaner
import pandas as pd

# Sample DataFrame
data = {'col1': [1, 2, None, 4], 'col2': [0.24, None, 0.15, 0.18]}
df = pd.DataFrame(data)

# Using the API
cleaner = DataCleaner(df)
cleaner.fill_missing_values(method='mean')
cleaner.remove_duplicates()
cleaner.normalize_data(['col1'])
print(cleaner.df)
```

## License

This project is licensed under the [MIT license](LICENSE). You are free to use, modify, and distribute this code as per the terms of the license.
