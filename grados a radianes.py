#Conversion de grados a radianes
import math

def convertir_radianes(grados):
  return math.radians(grados)

grados = float(input("Ingrese los grados: "))
radianes = round(convertir_radianes(grados), 2)
print(f"{grados} grados es equivalente a {radianes} radianes")
