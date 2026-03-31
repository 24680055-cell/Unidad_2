import flet as ft

class BotonPersonalizado(ft.ElevatedButton):
    def __init__(self, texto, color_fondo="blue"):
        super().__init__()
        self.text = texto
        self.bgcolor = color_fondo
        self.color = "white"

def main(page: ft.Page):
    # Uso del componente definido por el usuario
    btn = BotonPersonalizado("Enviar Datos", "green")
    page.add(btn)

# ft.app(target=main) 
