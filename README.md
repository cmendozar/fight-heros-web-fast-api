# Fight Heroes Toku

Fight Heroes Toku es una aplicación web construida con **FastAPI** que simula batallas entre dos equipos de héroes. Los resultados de la batalla se pueden enviar por correo electrónico a través de Mailgun. Esta aplicación permite a los usuarios ingresar su correo electrónico, simular una batalla, y recibir el resultado por correo.

La puedes probar directamente en el siguiente link [https://simulator-fight-toku-de9854dcc293.herokuapp.com](#)

La dejé levantada en heroku para que pudiesen probar, sin embargo como utilicé  **MailGun**  y es la versión de prueba debo verificar sus correos para que puedan probarla, me contactan y los incluyo para que puedan ver la aplicación funcionar.

Las regla de la pelea finalmente se dejó como pelea 1 a 1 entre los personajes, si un personaje es vencido, pasa el siguiente vivo del otro equipo y así hasta que un equipo sea el ganador.

## Estructura del Proyecto

```plaintext
.
├── README.md
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── sender.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── example.json
├── main.py
├── models
│   ├── __init__.py
│   ├── battle.py
│   ├── character.py
│   └── team.py
├── requirements.txt
└── Procfile
```

## Estructura del Proyecto

- **`app/`**: Contiene la lógica de la aplicación FastAPI.
  - `app.py`: Archivo principal donde se configura la aplicación FastAPI, se definen las rutas y se maneja la lógica de las solicitudes.
  - `sender.py`: Módulo para enviar correos electrónicos con los resultados de la batalla utilizando Mailgun.
  - **`static/`**: Carpeta que contiene archivos estáticos como CSS.
    - `styles.css`: Archivo de estilos CSS para la interfaz de usuario.
  - **`templates/`**: Carpeta que contiene las plantillas HTML utilizadas para renderizar las páginas web.
    - `index.html`: Página principal de la aplicación donde se encuentra el formulario para ingresar el correo electrónico y simular la batalla.
- **`models/`**: Define las clases y la lógica de la simulación de batalla.
  - `battle.py`: Contiene la clase Battle que maneja la simulación de la batalla entre dos equipos.
  - `character.py`: Define la clase Character que representa a un héroe y sus atributos.
  - `team.py`: Define la clase Team que representa un equipo de héroes.
- `main.py`: Archivo que contiene la función principal para ejecutar la simulación de la batalla.
- `example.json`: Archivo JSON de ejemplo con datos de héroes.
- `requirements.txt`: Lista de dependencias del proyecto.
- `Procfile`: Archivo que indica a Heroku cómo ejecutar la aplicación.

## Cómo Ejecutar el Proyecto

1. **Instala python y dependencias**
```bash
   python3 -m venv .venv
   pip install -r requirements.txt
   source .venv/bin/activate
```
2. Ejecuta la aplicación con uvicorn.
```bash
uvicorn app.app:app --reload
```
