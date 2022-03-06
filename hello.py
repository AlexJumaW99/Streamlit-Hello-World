# Imports
# -----------------------------------------------------------
import streamlit as st
import pandas as pd
# -----------------------------------------------------------

# Helper functions
# -----------------------------------------------------------
# Load data from external source
df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/PracticalML-KMeans-Election/master/voters_demo_sample.csv"
)
# -----------------------------------------------------------

# Sidebar
# -----------------------------------------------------------

# -----------------------------------------------------------


# Main
# -----------------------------------------------------------
# Create a title for your app
st.title("Interactive K-Means Clustering")

# A description
st.write("Here is the dataset used in this analysis:")

# Display the dataframe
st.write(df)