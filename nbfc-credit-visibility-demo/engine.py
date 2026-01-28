import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from utils.yaml_loader import load_yaml
from services.bureau_mock import pull_bureau
from services.internal_score import compute_internal_score
from services.composite_score import compute_composite
from services.visualization import map_risk_band

def run_credit_flow(applicant):
    config = load_yaml(os.path.join(BASE_DIR, "config/credit_visibility.yaml"))

    bureau = pull_bureau(applicant, config)
    internal = compute_internal_score(applicant, config)

    composite_score = compute_composite(
        bureau,
        internal,
        config["composite_risk_score"]
    )

    band = map_risk_band(
        composite_score,
        config["visualization_rules"]["score_bands"]
    )

    return {
        "bureau_score": bureau,
        "internal_score": internal,
        "composite_score": composite_score,
        "risk_band": band
    }
