equipo = "Los six sevens"
integrantes = ["Samuel","Axel","Luis","Diego","Ruby","Joao"]
print(f"Equipo:{equipo}")
print(f"Integrantes:{','.join(integrantes)}")

contrasenas = ["abcd","1234","tecmilenio1234","pepe","domingo"]
fortalezas = []

def verificar(contrasena: str):
    if len(contrasena) < 6:
        return "Debil"
    if len(contrasena) >= 6 and any(x.isnumeric() for x in contrasena) == False:
        return "Media"
    if len(contrasena) >= 6 and any(x.isnumeric() for x in contrasena):
        return "Fuerte"

for c in contrasenas:
    fortaleza = verificar(c)
    print(f"{c} - {fortaleza}")
    fortalezas.append(fortaleza)

print(f"Debil: {fortalezas.count('Debil')} \nMedia: {fortalezas.count('Media')}\nFuerte: {fortalezas.count('Fuerte')}")