"""

Asal Sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.

"""
def asal_mi(sayı):
    if sayı == 1:
        return False

    elif sayı == 2:
        return True

    else:
        return all(sayı % i != 0 for i in range(2, sayı))

while True:
    sayı = input("Sayı:")

    if (sayı == "q"):
        break
    sayı = int(sayı)

    if (asal_mi(sayı)):
        print(sayı,"asal bir sayıdır.")
    else:
        print(sayı,"asal bir sayı değildir.")












