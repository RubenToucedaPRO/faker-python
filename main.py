import faker as fk

fake = fk.Faker()

usuarios = {}

# Genera lista de 15 usuarios con datos ficticios
for i in range(1, 16):
    codigo = i
    nome = fake.name()
    direccion = fake.street_address()
    correo = fake.email()
    telefono = fake.phone_number()
    usuario = {}
    usuario["nome"] = nome
    usuario["direccion"] = direccion
    usuario["email"] = correo
    usuario["telefono"] = telefono
    usuarios[codigo] = usuario

# Muestra lista de usuarios
for id, usuario in usuarios.items():
    # print(f"ID: {codigo} - Nome: {datos["nome"]}")
    print(f"ID: {id} -> {usuario}")
