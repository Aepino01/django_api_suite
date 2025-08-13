import firebase_admin
from firebase_admin import credentials, db

try:
    # Carga la clave
    cred = credentials.Certificate("secrets/landing-key.json")

    # Inicializa Firebase
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://landingpage-d3fe2-default-rtdb.firebaseio.com/'
    })

    print("✅ Conexión exitosa a Firebase")

    # Lee algo de la base de datos (por ejemplo, raíz)
    ref = db.reference('landing_entries')
    result = ref.get()
    print("📦 Contenido actual:", result)

except Exception as e:
    print("❌ Error al conectar con Firebase:")
    print(e)
