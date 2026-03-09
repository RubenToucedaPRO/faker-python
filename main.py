import faker as fk
import random

fake = fk.Faker()

usuarios = {}

# Xenera lista de 15 usuarios con datos ficticios
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

# Mostra lista de usuarios
for id, usuario in usuarios.items():
    print(f"ID: {id} -> {usuario}")

# Seleccion aleatoria usuario
id_usuario_selecciondo = random.choice(list(usuarios.keys()))
nome = usuarios[id_usuario_selecciondo]["nome"]
print(f"O usuario chamado {nome} foi o afortunado")
