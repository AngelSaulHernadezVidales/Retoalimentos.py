https://replit.com/join/jdvkqccztf-angel-saulsaul3

Codigo:
print("Hola, soy Akira, y te ayudaré a evaluar los alimentos que consumas.")
grasa = float(input("Introduce los gramos de grasa por porción. "))
azucar = float(input("Introduce los gramos de azucar por porción. "))
sodio = float(input("Introduce los gramos de sodio por porción. "))
if grasa <= 5 and azucar <= 10 and sodio <= 100:
  print("Alimento bajo en sodio, grasas y azucares.")
elif grasa <= 5 and azucar <= 10:
  print("")
  print("El alimento es bajo en grasas y azucares")
elif sodio <= 100:
  print("")
  print("Alimento bajo en sodio")
else:
  print("")
  print("El alimento puede ser dañino para la salud, favor de considerar advertencias nutrimentales")
