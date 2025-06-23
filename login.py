usuarios = {
    "jostin": "1234",
    "jasmany": "abcd",
    "jorge": "pass"
}

print("Sistema de autenticación básico")
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuario in usuarios and usuarios[usuario] == contraseña:
    print("✅ Acceso concedido. ¡Bienvenido!")
else:
    print("❌ Acceso denegado. Usuario o contraseña incorrectos.")
