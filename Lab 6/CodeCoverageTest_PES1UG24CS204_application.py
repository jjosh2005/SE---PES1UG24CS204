import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# Energy charge tests
def test_domestic_low_usage():
    assert energy_charge(50, "domestic") == 200


def test_commercial_low_usage():
    assert energy_charge(50, "commercial") == 450


def test_domestic_first_slab_boundary():
    assert energy_charge(100, "domestic") == 350


def test_domestic_second_slab():
    assert energy_charge(200, "domestic") == 850


def test_domestic_second_slab_boundary():
    assert energy_charge(300, "domestic") == 1350


def test_domestic_third_slab():
    assert energy_charge(400, "domestic") == 2150


def test_commercial_third_slab():
    assert energy_charge(400, "commercial") == 4350


def test_invalid_connection():
    with pytest.raises(ValueError):
        energy_charge(50, "industrial")


def test_negative_units():
    with pytest.raises(ValueError):
        energy_charge(-10, "domestic")


# Late fee tests
def test_paid_on_time():
    assert late_fee(500, 0) == 0


def test_paid_early():
    assert late_fee(500, -5) == 0


def test_late_payment_within_15_days():
    assert late_fee(500, 10) == 50


def test_late_payment_after_15_days():
    assert late_fee(500, 20) == 100


def test_high_bill_late_payment():
    assert late_fee(2500, 20) == 225


# Subsidy tests
def test_senior_citizen_subsidy():
    assert subsidy(50, True, False) == 50


def test_no_senior_subsidy():
    assert subsidy(50, False, False) == 0


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_senior_and_solar_subsidy():
    assert subsidy(50, True, True) == 150


def test_solar_subsidy_above_300_units():
    assert subsidy(350, False, True) == 0
