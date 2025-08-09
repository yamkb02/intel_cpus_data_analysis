# Intel CPUs Data Analysis Dashboard

A data analysis and visualization dashboard for Intel processors, featuring webscraping, data cleaning, and interactive charts. This project helps users explore trends, pricing, and technical specifications of Intel CPUs.

## Features

- Automated webscraping of Intel CPU data
- Data cleaning and preprocessing pipeline
- Interactive dashboard with charts (pie, bar, scatter, box, heatmap)
- Cookbook page explaining dataset choices and cleaning steps
- Regression analysis for price prediction

## Tech Stack

- Python (pandas, numpy, scikit-learn, seaborn, matplotlib)
- Streamlit (dashboard UI)
- Plotly (interactive charts)
- BeautifulSoup, Selenium (webscraping)

## Installation & Usage

```bash
git clone <repo_url>
cd intel_cpus_data_analysis
pip install -r requirements.txt
streamlit run app_dashboard.py
```

If running webscraping, set up Chrome WebDriver and required environment variables.

Create `.env` file if needed for:

- GOOGLE_CHROME_BIN (path to Chrome binary)

## Status

MVP complete. Dashboard and data cleaning pipeline are functional. Future improvements: add AMD/other CPU datasets, more advanced analytics.

## License

Copyright (c) 2023 Mark Kenneth S. Badilla
