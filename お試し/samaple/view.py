import flet as ft
from custom_view import CustomView


def create_page1():
    return CustomView(
        name="page1",
        content=ft.Column(controls=[ft.Text("This is Page 1")])
    )

def create_page2():
    return CustomView(
        name="page2",
        content=ft.Column(controls=[ft.Text("This is Page 2")])
    )
