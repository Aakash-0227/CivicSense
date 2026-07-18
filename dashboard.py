import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the complaints file
data = pd.read_csv("dataset/complaints.csv")

# Dashboard title
st.title("CivicSense Dashboard")

# Total complaints
st.subheader("Total Complaints")
st.write(len(data))

# Complaint details
st.subheader("Complaint Details")
st.dataframe(data)

# Complaint categories
st.subheader("Complaint Categories")
st.write(data["Category"].value_counts())

# Priority levels
st.subheader("Priority Levels")
st.write(data["Priority"].value_counts())


# -------------------------
# Bar Chart for Categories
# -------------------------

st.subheader("Category Bar Chart")
st.bar_chart(data["Category"].value_counts())


# -------------------------
# Pie Chart for Priorities
# -------------------------

st.subheader("Priority Pie Chart")

fig, ax = plt.subplots()

data["Priority"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

st.pyplot(fig)


# -------------------------
# High Priority Complaints
# -------------------------

st.subheader("High Priority Complaints")

high_priority = data[data["Priority"] == "High"]

st.dataframe(high_priority)


# -------------------------
# Search Complaint
# -------------------------

st.subheader("Search Complaint")

search = st.text_input("Enter a keyword")

if search:
    result = data[
        data["Complaint"].str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(result)


# -------------------------
# Download Complaint Report
# -------------------------

st.subheader("Download Complaint Report")

csv = data.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="complaints_report.csv",
    mime="text/csv"
)