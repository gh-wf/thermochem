import pytest
from thermochem.burcat import Elementdb


def test_enthalpy():
    db = Elementdb()
    oxygen = db.getelementdata("O2 REF ELEMENT")
    enthalpy = oxygen.ho(298.15)
    pytest.approx(enthalpy, 1.94293914332e-05)

def test_enthalpy_n2():
    db = Elementdb()
    nitrogen = db.getelementdata("N2 REF ELEMENT")
    enthalpy = nitrogen.ho(298.15)
    pytest.approx(enthalpy, 4.48429316148e-06)

def test_nio():
    """Test NiO phases"""
    db = Elementdb()
    assert db.search('NiO') == ['NiO  Solid-A', 'NiO  Solid-B', 'NiO  Solid-C', 'NiO  Liquid']
