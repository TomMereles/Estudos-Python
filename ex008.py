medida = float(input('Uma distância em metros: '))
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f}m corresponde a {}km, {:.0f}cm e {:.0f}mm'.format(medida, km, cm, mm))

