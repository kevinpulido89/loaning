"""Script to find compound interest for given values"""

def calculate_compound_interest(deuda: int, rate: float, time: float) -> float:
    """Calculates compound interest

    Args:
        deuda (float): _description_
        rate (float): _description_
        time (int): _description_

    Returns:
        float: _description_
    """

    pago = deuda * (pow((1 + rate / 100), time))
    return pago - deuda

def compound_interest(deuda: int, rate: float, time: int) -> tuple:
    """ Get monthly fee and interest for the amount of time requested"""
    intereses = []
    base = deuda / time
    saldo = deuda

    for _ in range(time):
        CI = calculate_compound_interest(deuda=saldo, rate=rate, time=1.01)
        intereses.append(CI)
        saldo = saldo - base + CI

    cuota_mensual = (sum(intereses) / time) + base
    intereses_generados = sum(intereses)

    return cuota_mensual, intereses_generados
