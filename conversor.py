n = float(input('Um valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('O valor em quilômetros é {:.3f} km'.format(km))
print('O valor em hectômetros é {:.3f} hm'.format(hm))
print('O valor em decâmetros será {:.3f} dam'.format(dam))
print('O valor em decímetros será {:.3f} dm'.format(dm))
print('O valor em centímetros será {:.3f} cm'.format(cm))
print('O valor em milímetros será {:.3f} mm'.format(mm))

