def predict_priority(complaint):

    complaint = complaint.lower()

    if "accident" in complaint or "fire" in complaint or "flood" in complaint:
        priority = "High"

    elif "garbage" in complaint or "water leakage" in complaint:
        priority = "Medium"

    else:
        priority = "Low"

    return priority
