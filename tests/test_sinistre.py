from src.models.sinistre_vol import SinistreVol


def test_est_frauduleux_true():
    s = SinistreVol("2023-01-01", 12000, "vol")
    assert s.est_frauduleux() is True


def test_est_frauduleux_false():
    s = SinistreVol("2023-01-01", 8000, "vol")
    assert s.est_frauduleux() is False
