from utils.yaml_loader import load_yaml

CONFIG_PATH = "nbfc-credit-visibility-demo/config/nbfc-credit-visibility-config.yaml"

def run_credit_flow():
    config = load_yaml(CONFIG_PATH)

    # mock scores (demo-safe)
    bureau_score = 720
    internal_score = 680

    score = int(
        config["composite_risk_score"]["bureau_weight"] * bureau_score +
        config["composite_risk_score"]["internal_weight"] * internal_score
    )

    for band in config["visualization_rules"]["score_bands"]:
        if band["min"] <= score <= band["max"]:
            return {
                "score": score,
                "label": band["label"],
                "color": band["color"]
            }

    return {"score": score, "label": "Unknown", "color": "#999999"}
