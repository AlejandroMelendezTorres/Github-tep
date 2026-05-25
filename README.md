# Streamlit Seller Analytics Dashboard

A dynamic web application for analyzing vendor performance metrics, built with Streamlit.

## Overview

This application provides an interactive dashboard for viewing seller data with the following features:

- **Dynamic Filtering**: Filter vendors by region
- **Vendor Selection**: Dropdown selector to view individual vendor performance
- **Performance Metrics**: Display key metrics including:
  - Total Income
  - Total Sales
  - Total Sold Units
  - Sales Average
- **Regional Analytics**: Grouped bar chart showing sales performance by region
- **Data Registry**: Comprehensive table view of all vendor data

## Project Structure

```
streamlittesting/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── run.sh              # Shell script to run the application
├── .gitignore          # Git ignore file
├── .venv/              # Python virtual environment
└── Data/               # Data directory
    └── sellers.xlsx    # Seller data file
```

## Requirements

- Python 3.8+
- See `requirements.txt` for package dependencies

## Installation

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Using the shell script (macOS/Linux):
```bash
./run.sh
```

### Using Streamlit directly:
```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.24.0 | Web framework |
| pandas | 2.0.3 | Data manipulation |
| streamlit-dynamic-filters | 0.1.0 | Dynamic filtering |
| plotly | 5.15.0 | Interactive charts |

## Data Format

The application expects an Excel file (`Data/sellers.xlsx`) with the following columns:
- `NAME`: Vendor first name
- `LASTNAME`: Vendor last name
- `REGION`: Region identifier
- `INCOME`: Vendor income
- `SOLD UNITS`: Number of units sold
- `TOTAL SALES`: Total sales amount
- `SALES AVERAGE`: Average sales per transaction

## Features

### Filters
- **Region Filter**: Dynamically filter vendors by their region

### Vendor Profile
- View individual vendor metrics through the dropdown selector
- Display KPIs in metric cards

### Performance Analytics
- Regional sales performance visualization
- Grouped bar chart comparing multiple metrics across regions
- Data registry table with all vendor information

## Layout

The dashboard uses a two-column layout:
- **Left Column**: Controls, filters, and vendor profile metrics
- **Right Column**: Performance analytics charts and data table

## Notes

- The application uses wide layout mode to maximize screen space
- Dynamic filters are applied to the region field
- Vendor names are created by concatenating NAME and LASTNAME fields
- Regional aggregations use sum for units and sales, and mean for sales average
