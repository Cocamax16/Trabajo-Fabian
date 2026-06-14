from django.contrib.auth import get_user_model

User = get_user_model()

def crear_admin():
    usuario = "admin"
    password = "Admin123456"
    email = "admin@admin.com"

    if not User.objects.filter(username=usuario).exists():
        User.objects.create_superuser(
            username=usuario,
            email=email,
            password=password
        )
        print("Superusuario creado correctamente")
