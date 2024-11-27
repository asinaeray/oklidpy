import math

def oklid_mesafesi(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n = int(input("Kaç çift nokta arasındaki mesafeyi hesaplamak istiyorsunuz? "))

for i in range(n):
    print(f"{i+1}. çift noktayı girin:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    mesafe = oklid_mesafesi(x1, y1, x2, y2)
    print(f"({x1}, {y1}) ve ({x2}, {y2}) noktaları arasındaki Öklid mesafesi: {mesafe:.2f}\n")
