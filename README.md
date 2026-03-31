Unidad 2: Componentes y Librerías

2.1 Definición conceptual de componentes, paquetes y librerías
 Componente: Es una unidad de software independiente y reutilizable que cumple una función específica (ej. un botón en una interfaz).
 Paquete: Es una carpeta que contiene varios módulos (archivos .py) relacionados, permitiendo organizar el código de forma jerárquica.
 Librería (Biblioteca): Conjunto de paquetes y módulos diseñados para solucionar problemas comunes (ej. flet, math, os).

 2.2 Uso de librerías proporcionadas por el lenguaje
Python incluye la Standard Library. Un ejemplo común es el uso de math para operaciones complejas o datetime para el manejo de fechas.

python
import math

 Ejemplo: Cálculo de área
radio = 5
area = math.pi * math.pow(radio, 2)
print(f"Área: {area}")


2.3 Creación de componentes (visuales y no visuales) definidos por el usuario
Un componente definido por el usuario permite encapsular lógica y diseño para reutilizarlo en diferentes partes de una aplicación.

 Ejemplo: Componente Visual (Flet)
python
import flet as ft

class BotonPersonalizado(ft.ElevatedButton):
    def __init__(self, texto, color_fondo="blue"):
        super().__init__()
        self.text = texto
        self.bgcolor = color_fondo
        self.color = "white"

def main(page: ft.Page):
     Uso del componente definido por el usuario
    btn = BotonPersonalizado("Enviar Datos", "green")
    page.add(btn)

 ft.app(target=main)


 2.4 Creación y uso de paquetes/librerías definidas por el usuario
Para crear tu propia librería, organizas tus archivos en una estructura de carpetas con un archivo __init__.py.

Estructura de archivos:
text
mi_proyecto/
│
├── utilidades/          <-- Paquete del usuario
│   ├── __init__.py
│   └── calculos.py      <-- Módulo con lógica
└── main.py              <-- Uso del paquete


Contenido de calculos.py:
python
def validar_usuario(nombre):
    return len(nombre) > 3


Uso en main.py:
python
from utilidades.calculos import validar_usuario

if validar_usuario("Nadia"):
    print("Usuario válido")


Bibliografía (Formato APA)

 Python Software Foundation. (2026). The Python Standard Library. Recuperado de [https://docs.python.org/3/library/](https://docs.python.org/3/library/)
 Flet Dev. (2026). Flet Controls: Custom Components. Recuperado de [https://flet.dev/docs/controls/](https://flet.dev/docs/controls/)
 Sommerville, I. (2011). Software Engineering. Addison-Wesley.

 
