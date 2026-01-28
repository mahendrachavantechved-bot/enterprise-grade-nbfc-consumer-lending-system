def map_risk_band(score, bands):
    for band in bands:
        if band["min"] <= score <= band["max"]:
            return band
    return {"label": "Unknown"}
