# test du moteur de détection de changements Delta
from delta_change_detection.analyzer import detect_change

def test_detect_change():
    contract = detect_change(48.8566, 2.3522, "2026-01-01", "2026-05-01")
    assert contract is not None
    assert contract.result["change_detected"] is True
    assert len(contract.result["diff_items"]) >= 1
    assert len(contract.evidence) >= 1
