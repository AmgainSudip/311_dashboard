import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(
    page_title="Philadelphia 311 Dashboard",
    layout="wide"
)

st.title("Philadelphia 311 Dashboard")

st.write(
    "Explore 311 service requests in Philadelphia by date, "
    "ZIP code, service type, and status."
)

# Load data
DATA_FILE = "311_2025_dashboard.csv"

df = pd.read_csv(DATA_FILE)

df["request_date"] = pd.to_datetime(
    df["request_date"],
    errors="coerce"
)

# Date controls
min_date = df["request_date"].min().date()
max_date = df["request_date"].max().date()

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "Start date",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

with col2:
    end_date = st.date_input(
        "End date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

if start_date > end_date:
    st.error("Start date must be on or before end date.")
    st.stop()

# Filter by date
filtered_df = df[
    (df["request_date"].dt.date >= start_date) &
    (df["request_date"].dt.date <= end_date)
].copy()

# Additional filter
service_options = ["All"] + sorted(
    filtered_df["service_name"]
    .dropna()
    .unique()
    .tolist()
)

selected_service = st.selectbox(
    "Service type",
    service_options
)

if selected_service != "All":
    filtered_df = filtered_df[
        filtered_df["service_name"] == selected_service
    ].copy()

# Summary metrics
total_requests = len(filtered_df)

unique_zipcodes = filtered_df["zipcode"].nunique()

unique_services = filtered_df["service_name"].nunique()

m1, m2, m3 = st.columns(3)

m1.metric(
    "Total Requests",
    f"{total_requests:,}"
)

m2.metric(
    "ZIP Codes",
    f"{unique_zipcodes:,}"
)

m3.metric(
    "Service Types",
    f"{unique_services:,}"
)

# CHART 1: Top 10 ZIP Codes
st.subheader("Top 10 ZIP Codes by 311 Requests")

requests_by_zipcode = (
    filtered_df["zipcode"]
    .value_counts()
    .head(10)
    .sort_values()
)

fig1, ax1 = plt.subplots(figsize=(4.5, 2.8))

requests_by_zipcode.plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel(
    "ZIP Code",
    fontsize=8
)

ax1.set_ylabel(
    "Number of Requests",
    fontsize=8
)

ax1.set_title(
    "Top 10 ZIP Codes by 311 Requests",
    fontsize=9
)

ax1.tick_params(
    axis="both",
    labelsize=7
)

plt.tight_layout()
plt.xticks(rotation=45)

st.pyplot(
    fig1,
    width="content"
)

plt.close(fig1)


# CHART 2: Requests by Hour of Day
st.subheader("311 Requests by Hour of Day")

filtered_df["requested_datetime"] = pd.to_datetime(
    filtered_df["requested_datetime"],
    errors="coerce",
    utc=True
)

filtered_df["request_hour"] = (
    filtered_df["requested_datetime"]
    .dt.tz_convert("America/New_York")
    .dt.hour
)

requests_by_hour = (
    filtered_df["request_hour"]
    .value_counts()
    .sort_index()
)

fig2, ax2 = plt.subplots(figsize=(6, 3.5))

requests_by_hour.plot(
    kind="bar",
    ax=ax2
)

ax2.set_xlabel("Hour of Day", fontsize=8)
ax2.set_ylabel("Number of Requests", fontsize=8)
ax2.set_title("311 Requests by Hour of Day", fontsize=9)

ax2.tick_params(
    axis="both",
    labelsize=7
)

ax2.set_xticks(range(24))
ax2.set_xticklabels(
    [f"{h}:00" for h in range(24)],
    rotation=45,
    ha="right"
)

plt.tight_layout()

st.pyplot(
    fig2,
    width="content"
)

plt.close(fig2)

# CHART 3: Requests by Day of Week
st.subheader("311 Requests by Day of Week")

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

requests_by_day = (
    filtered_df["day_of_week"]
    .value_counts()
    .reindex(day_order)
)

fig3, ax3 = plt.subplots(figsize=(5, 3))

requests_by_day.plot(
    kind="bar",
    ax=ax3
)

ax3.set_xlabel("Day of Week", fontsize=8)
ax3.set_ylabel("Number of Requests", fontsize=8)
ax3.set_title("311 Requests by Day of Week", fontsize=9)

ax3.tick_params(
    axis="both",
    labelsize=7
)

plt.xticks(rotation=0)

plt.tight_layout()

st.pyplot(
    fig3,
    width="content"
)

plt.close(fig3)