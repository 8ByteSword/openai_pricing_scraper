# OpenAI Pricing Scraper

This package provides a simple way to fetch and parse the pricing data from the OpenAI pricing page. It can be used as a standalone script or as a module imported into other applications.

## Installation

To install the package, you can either clone the repository and install it locally or install it directly from the source using pip:

```bash
pip install git+https://github.com/8ByteSword/openai_pricing_scraper.git
```

or

```bash
pip install openai_pricing_scraper
```

(Github and pypi versions may differ)

## Usage

### As a module

```python
from openai_pricing_scraper import fetch_pricing_data

pricing_data = fetch_pricing_data()
print(pricing_data)
```

### As a standalone script

Run the `fetch_pricing.py` script directly:

```bash
python fetch_pricing.py
```

## Result

The result will be given as a JSON. At the time of writing would be:

## License

This project is licensed under the [MIT License](LICENSE).
