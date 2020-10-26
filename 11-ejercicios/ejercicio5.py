

tabla = [
	{
		"categoria": "Aventura",
		"juegos": ["Assasins Creed", "Crysis", "Prince of Persia"]
	},
	{
		"categoria": "Deportes",
		"juegos": ["FIFA 21", "Moto GP", "PES 21"]
	},
	{
		"categoria": "Acción",
		"juegos": ["Call of Duty", "PGB", "XY"]
	}

]

print(tabla)
print("----")

for categoria in tabla:
	print(f"--- {categoria['categoria']} ---")

	for juego in  categoria['juegos']:
		print(f"¨{juego}")