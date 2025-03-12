# PubMed-Paper-Fetcher

# PubMed Paper Fetcher

## Overview

This Python program fetches research papers from PubMed based on a user-specified query. It filters papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Code Organization

- `pubmed_fetcher.py`: Contains the `PubMedFetcher` class to interact with the PubMed API and filter results.
- `get_papers_list.py`: Command-line interface to use the `PubMedFetcher` class.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage

To fetch papers based on a query and save results to a CSV file:
```sh
poetry run get-papers-list "cancer research" -f results.csv
```

For help and additional options:
```sh
poetry run get-papers-list --help
```

## Tools Used

- [Poetry](https://python-poetry.org/): Dependency management and packaging.
- [Requests](https://docs.python-requests.org/en/latest/): HTTP library for making API calls.
