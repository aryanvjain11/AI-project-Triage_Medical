import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import app2


def test_extract_clinical_keywords_catches_breathing_phrases():
    keywords = app2.extract_clinical_keywords("I have difficulty breathing and chest pressure")
    assert any("dyspnea" in keyword or "respiratory distress" in keyword for keyword in keywords)
