kir, ari, ser = map(int, input('Введите рекорды: ').split())
if ari > kir > ser:
    print(ari)
elif kir > ari > ser:
    print(kir)
else:
    print(ser)

