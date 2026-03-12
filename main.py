import faker as fk
import random
import unicodedata


def preparar_nome_para_correo(nome):
    """Elimina espacios e tildes e mantén as ñ"""
    nome = nome.replace("ñ", "#").replace(" ", "").lower()
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode("ascii")
    nome = nome.replace("#", "ñ")
    return nome


fake = fk.Faker("es_ES")

usuarios = {}

# Xenera lista de 15 usuarios con datos ficticios
for i in range(1, 16):
    codigo = i
    nome = fake.name()
    direccion = fake.street_address() + " " + fake.city()
    correo = preparar_nome_para_correo(nome) + "@" + fake.free_email_domain()
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
