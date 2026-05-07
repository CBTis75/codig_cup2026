import sys

def calcular_neto():
    entrada = sys.stdin.read().strip()
    if not entrada:
        return
    
    sueldo = float(entrada)
    # Estructura: (Límite Inferior, Límite Superior, Cuota Fija, Tasa)
    tarifas = [
        (0.01, 644.58, 0.00, 0.0192),
        (644.59, 5470.92, 12.38, 0.0640),
        (5470.93, 9614.66, 321.26, 0.1088),
        (9614.67, 11176.62, 772.10, 0.16),
        (11176.63, 13381.47, 1022.01, 0.1792),
        (13381.48, 26988.50, 1417.12, 0.2136),
        (26988.51, 42537.58, 4323.58, 0.2352),
        (42537.59, 81211.25, 7980.73, 0.30),
        (81211.26, 108281.67, 19582.83, 0.32),
        (108281.68, 324845.01, 28245.36, 0.34),
        (324845.02, float('inf'), 101876.90, 0.35)
    ]

    for inferior, superior, fija, tasa in tarifas:
        if inferior <= sueldo <= superior:
            impuesto = fija + (sueldo - inferior) * tasa
            resultado = sueldo - impuesto
            print(f"{resultado:.2f}")
            break

if __name__ == "__main__":
    calcular_neto()