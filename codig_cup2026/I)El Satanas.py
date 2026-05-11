s = float(input())

if s <= 644.58:
    li, cuota, p = 0.01, 0.00, 1.92
elif s <= 5470.92:
    li, cuota, p = 644.59, 12.38, 6.40
elif s <= 9614.66:
    li, cuota, p = 5470.93, 321.26, 10.88
elif s <= 11176.62:
    li, cuota, p = 9614.67, 772.10, 16.00
elif s <= 13381.47:
    li, cuota, p = 11176.63, 1022.01, 17.92
elif s <= 26988.50:
    li, cuota, p = 13381.48, 1417.12, 21.36
elif s <= 42537.58:
    li, cuota, p = 26988.51, 4323.58, 23.52
elif s <= 81211.25:
    li, cuota, p = 42537.59, 7980.73, 30.00
elif s <= 108281.67:
    li, cuota, p = 81211.26, 19582.83, 32.00
elif s <= 324845.01:
    li, cuota, p = 108281.68, 28245.36, 34.00
else:
    li, cuota, p = 324845.02, 101876.90, 35.00

isr = cuota + (s - li) * (p / 100)
print(f"{s - isr:.2f}")