import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# 1. Energy charge — connection validation
def test_invalid_connection():
    with pytest.raises(ValueError):
        energy_charge(50, "industrial")


def test_negative_units():
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")


# 2. Energy charge — all three slabs
def test_first_slab():
    assert energy_charge(50, "domestic") == 200


def test_first_slab_boundary():
    assert energy_charge(100, "domestic") == 350


def test_second_slab():
    assert energy_charge(200, "domestic") == 850


def test_second_slab_boundary():
    assert energy_charge(300, "domestic") == 1350


def test_third_slab():
    assert energy_charge(400, "domestic") == 2150


# 3. Domestic and commercial branches
def test_commercial_connection():
    assert energy_charge(50, "commercial") == 450


def test_commercial_third_slab():
    assert energy_charge(400, "commercial") == 4350


# 4. Late fee — all decision branches
def test_no_late_fee():
    assert late_fee(500, 0) == 0


def test_negative_late_days():
    assert late_fee(500, -5) == 0


def test_late_within_15_days():
    assert late_fee(500, 10) == 50


def test_late_after_15_days():
    assert late_fee(500, 20) == 100


def test_high_bill_extra_fee():
    assert late_fee(2500, 20) == 225


def test_low_bill_no_extra_fee():
    assert late_fee(1500, 20) == 100


# 5. Subsidy — senior citizen conditions
def test_senior_eligible():
    assert subsidy(50, True, False) == 50


def test_not_senior():
    assert subsidy(50, False, False) == 0


def test_senior_above_100_units():
    assert subsidy(150, True, False) == 0


# 6. Subsidy — solar conditions
def test_solar_eligible():
    assert subsidy(200, False, True) == 100


def test_no_solar():
    assert subsidy(200, False, False) == 0


def test_solar_above_300_units():
    assert subsidy(350, False, True) == 0


def test_senior_and_solar():
    assert subsidy(50, True, True) == 150
