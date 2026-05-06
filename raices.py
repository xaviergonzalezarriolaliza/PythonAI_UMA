import math

def resuelve_ecuacion(a, b, c):
    """
    Resuelve una ecuacion de segundo grado a x^2 + bx + c = 0.

    Parameters
    ----------
    a : float
        Coeficiente de segundo grado. No puede ser cero.
    b : float
        Coeficiente de primer grado.
    c : float
        Término independiente.

    Returns
    -------
    Una tupla con las raíces reales.

    Raises
    ------
    ValueError si no hay dos soluciones reales o a es cero.
    """
    if a == 0:
        raise ValueError("error: la ecuación no es de segundo grado (a = 0)")

    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        raise ValueError("error: las raíces son complejas (discriminante negativo)")

    raiz_discriminante = math.sqrt(discriminante)
    raices = ((-b + raiz_discriminante) / (2 * a),
              (-b - raiz_discriminante) / (2 * a))
    return raices

a = float(input("dame el coeficiente a: "))
b = float(input("dame el coeficiente b: "))
c = float(input("dame el coeficiente c: "))

try:
    r1, r2 = resuelve_ecuacion(a, b, c)
    print("las raíces son", r1, r2)
except ValueError as e:
    print(e)