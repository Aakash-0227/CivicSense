import os
import pandas as pd
from classifier import predict_category
from prioritizer import predict_priority

# Get complaint from user
complaint = input("Enter your complaint: ")

# Predict category and priority
category = predict_category(complaint)
priority = predict_priority(complaint)

# Store the data
new_data = pd.DataFrame({
    "Complaint": [complaint],
    "Category": [category],
    "Priority": [priority]
})

# File path
file_path = "dataset/complaints.csv"

# Save complaint into CSV file
if os.path.exists(file_path):
    new_data.to_csv(
        file_path,
        mode="a",
        header=False,
        index=False
    )
else:
    new_data.to_csv(
        file_path,
        index=False
    )

# Display the result
print("\n========== CivicSense ==========")
print("Category :", category)
print("Priority :", priority)
print("================================")

# Success message
print("\nComplaint saved successfully!")