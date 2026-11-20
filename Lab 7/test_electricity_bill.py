from hypothesis import given, strategies as st, settings
from electricity_bill import units_consumed, daily_average, tariff_rate
import math


# Test 1: Fuzz units_consumed()
@given(st.text() | st.none())
@settings(max_examples=100)
def test_units_consumed_no_crash(s):
    try:
        result = units_consumed(s)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


# Test 2: Fuzz daily_average()
@given(st.text() | st.none())
@settings(max_examples=100)
def test_daily_average_no_crash(s):
    try:
        result = daily_average(s)
        assert isinstance(result, (int, float))
        assert math.isfinite(result)
        assert result >= 0
    except ValueError:
        pass


# Test 3: Fuzz tariff_rate()
@given(st.text() | st.none())
@settings(max_examples=100)
def test_tariff_rate_no_crash(s):
    try:
        result = tariff_rate(s)
        assert isinstance(result, (int, float))
        assert result > 0
    except ValueError:
        pass
