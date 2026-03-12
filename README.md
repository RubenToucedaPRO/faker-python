# faker-python
Tarefa 2 - Curso desarrollo de aplicaciones con Python - Entornos y sintaxis en Python

## Descripción
Faker es una biblioteca de Python que permite generar datos falsos de manera sencilla. En esta aplicación se generan los datos aleatorios de 15 usuarios (nombre, dirección, correo electrónico, teléfono) en un diccionario. Se muestran por terminal todos los datos de los usuarios creados. El programa seleccionará aleatoriamente uno de los usuarios el cual se mostrará en terminal.

## Instalación proyecto
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/RubenToucedaPRO/faker-python

    ```
2. Navegar al directorio del proyecto:
   ```bash
   cd faker-python
   ```
3. Crear un entorno virtual:
   - En Windows:
   ```bash
   python -m venv .venv
   ```
    - En macOS/Linux:
    ```bash
    python3 -m venv .venv
    ```
4. Activar el entorno virtual:
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```      
6. Es posible que sea necesario reiniciar vs code para que reconozca el el paquete faker.