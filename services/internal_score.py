def compute_internal_score(applicant, config):
    score = 0

    if applicant.get("employment_type") == "salaried":
        score += 60

    if applicant.get("emi_to_income", 100) < 40:
        score += 30

    return min(score, 100)
