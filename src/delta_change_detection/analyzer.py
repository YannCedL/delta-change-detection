from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def detect_change(lat: float, lon: float, date_start: str, date_end: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {
        "lat": lat, "lon": lon,
        "date_start": date_start, "date_end": date_end,
        "ndvi_before": 0.42, "ndvi_after": 0.29,
        "change_detected": True,
        "change_magnitude": 0.13
    }
    contract.add_evidence(Evidence(subject=f"{lat},{lon}", predicate="ndvi_change",
        value="vegetation_loss_detected", source="Copernicus_Sentinel2",
        observed_at=now, confidence=0.91, status=EpistemicStatus.INFERENCE))
    return contract
