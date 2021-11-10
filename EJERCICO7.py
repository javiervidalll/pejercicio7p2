nombretelefono = list()
while True:
    nombre = input("nombre:")
    if nombre == "fin":
        break
    telefono = input("numero de telefono")
    cell_1 = {}
    cell_1["nombre:"] = nombre
    cell_1["numero de telefono:"] = telefono
    nombretelefono.append(cell_1)
for cell in nombretelefono:
    print("numero y telefono", cell_1)
#me dijiste que no aprece en github el archivo.