from delta_change_detection import detect_change

def test_detect_change():
    c = detect_change(48.8566, 2.3522, "2024-01-01", "2024-06-01")
    assert c.result["change_detected"] is True
    assert c.confidence > 0.8
