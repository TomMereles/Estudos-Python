#Conversão de medidas
medida = float(input('Uma distância em metros: '))
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida:.1f}m corresponde a {km}km, {cm:.0f}cm e {mm:.0f}mm')

