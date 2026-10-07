# Philadelphia 311 Streamlit Dashboard

## Project Overview

This project is an interactive Streamlit dashboard for exploring Philadelphia 311 service requests from 2025.

The dashboard allows users to select a date range and filter requests by service type. The charts and summary metrics update based on the selected filters.

## Dashboard Features

### Date Filters

Users can select:

* Start date
* End date

The dashboard only displays requests within the selected period.

### Service Type Filter

Users can select a specific service type or view all service types.

### Summary Metrics

The dashboard displays:

* **Total Requests** — Number of 311 requests in the selected period
* **ZIP Codes** — Number of unique ZIP codes represented
* **Service Types** — Number of unique service types represented

### Visualizations

The dashboard includes three charts:

1. **Top 10 ZIP Codes by 311 Requests**
   Shows which ZIP codes have the highest number of requests.

2. **311 Requests by Hour of Day**
   Shows what times of day have the highest number of requests.

3. **311 Requests by Day of Week**
   Shows how request volume differs across days of the week.

All visualizations respond to the selected date range and service type.

## Project Files

```text
.
├── Notebook_1_Prepare_2025_311_Dashboard_Data.ipynb
├── Notebook_2_Prototype_311_Dashboard.ipynb
├── app.py
├── 311_2025_dashboard.csv
└── README.md
```

### Notebook 1

Prepares the dashboard dataset by:

* Reading the original Philadelphia 311 dataset
* Converting `requested_datetime` to a datetime field
* Filtering records to 2025
* Creating `request_date`
* Creating other useful variables
* Selecting only the columns needed for the dashboard
* Saving the reduced dataset as `311_2025_dashboard.csv`

### Notebook 2

Tests the dashboard logic before building the Streamlit application. It:

* Reads the reduced 2025 dataset
* Allows a start and end date to be selected
* Filters the data
* Tests the dashboard visualizations

### app.py

Contains the final Streamlit dashboard, including the filters, summary metrics, and visualizations.

### 311_2025_dashboard.csv

Reduced 2025 dataset used by the Streamlit application.

## How to Run

### 1. Install the required packages

```bash
pip install streamlit pandas matplotlib
```

### 2. Make sure the following files are in the same folder

```text
app.py
311_2025_dashboard.csv
```

### 3. Start the Streamlit application

From the project folder, run:

```bash
streamlit run app.py
```

The dashboard will open in a web browser.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Streamlit
* Jupyter Notebook

## Data

The dashboard uses Philadelphia 311 service request data for 2025. The full dataset was reduced during the data preparation stage so that the Streamlit application only loads the fields needed for the dashboard.

## Project Goal

The goal of this project is to demonstrate how a prepared dataset can be used to build a simple interactive dashboard. The project follows a three-step process:

```text
Original 311 Dataset
        ↓
Notebook 1: Data Preparation
        ↓
311_2025_dashboard.csv
        ↓
Notebook 2: Dashboard Prototype
        ↓
Streamlit app.py
```
