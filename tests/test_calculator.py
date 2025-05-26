import pytest
from calculator import calculate_compound_interest, compound_interest, generate_random_string


def test_calculate_compound_interest():
    # Test with known values
    deuda = 1000
    rate = 10
    time = 2
    expected_interest = 1000 * ((1 + 0.1) ** 2) - 1000
    assert pytest.approx(calculate_compound_interest(deuda, rate, time), 0.01) == expected_interest

    # Test with zero rate
    assert calculate_compound_interest(1000, 0, 5) == 0

    # Test with zero time
    assert calculate_compound_interest(1000, 10, 0) == 0


def test_compound_interest():
    deuda = 1200
    rate = 12
    time = 12
    cuota_mensual, intereses_generados = compound_interest(deuda, rate, time)
    # Check that the monthly fee is positive and reasonable
    assert cuota_mensual > 0
    assert intereses_generados > 0
    # The sum of all payments should be greater than the original debt
    assert cuota_mensual * time > deuda

    # Test with 1 month (should be similar to calculate_compound_interest)
    cuota_mensual, intereses_generados = compound_interest(1000, 10, 1)
    assert pytest.approx(intereses_generados, 0.01) == calculate_compound_interest(1000, 10, 1.01)


def test_generate_random_string():
    s = generate_random_string()
    assert isinstance(s, str)
    assert len(s) == 4
    # Should be alphanumeric
    assert all(c.isalnum() for c in s)
    # Should be random: generate multiple and check for uniqueness
    results = {generate_random_string() for _ in range(100)}
    assert len(results) > 90  # High probability of uniqueness 