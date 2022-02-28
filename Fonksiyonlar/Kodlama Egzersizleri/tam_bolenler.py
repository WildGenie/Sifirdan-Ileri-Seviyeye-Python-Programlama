def tambolenleribulma(sayı):
    return [i for i in range(2,sayı) if (sayı % i == 0)]

while True:

    sayı = input("Sayı:")

    if (sayı == "q"):
        print("Program Sonlandırılıyor")
        break
    else:
        sayı = int(sayı)

        print("Tam bölenler:",tambolenleribulma(sayı))








