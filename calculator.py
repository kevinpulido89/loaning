"""
script to find compound interest for given values.
"""


def calculate_compound_interest(deuda: float, rate: float, time: float) -> float:
    """
    Calculates compound interest

    Args:
        deuda (float): _description_
        rate (float): _description_
        time (int): _description_

    Returns:
        float: _description_
    """

    pago = deuda * (pow((1 + rate / 100), time))
    return round(pago - deuda)


def compound_interest(deuda, rate, time):
    """doc"""
    intereses = []
    base = deuda / time
    saldo = deuda
    for _ in range(time):
        CI = calculate_compound_interest(deuda=saldo, rate=rate, time=1.01)
        intereses.append(CI)
        saldo = saldo - base + CI

    print(f"intereses op1= {sum(intereses)}")

    op1 = (sum(intereses) / time) + base

    print(f"Couta mensual op1 = {op1}")
    print(f"ganancia_final = {op1*time}")


kwargs = {"deuda": 500_000, "rate": 6.3, "time": 3}

compound_interest(**kwargs)

# print(f"\nintereses op2= {calculate_compound_interest(**kwargs)}")
# op2 = calculate_compound_interest(**kwargs) / kwargs["time"] + kwargs["deuda"] / kwargs["time"]

# print(f"Cuota mensual op2 = {op2}")
# print(f"ganancia_final = {op2*kwargs['time']}")
