def compute_composite(bureau, internal_score, rule):
    composite = (
        rule["bureau_weight"] * bureau["normalized_bureau_score"] +
        rule["internal_weight"] * (internal_score * 6)
    )
    return round(composite / 5) * 5
