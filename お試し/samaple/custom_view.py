# from flet import View, AppBar, Column, Container, Row, Page, alignment, ElevatedButton
import flet as ft

class CustomView(ft.View):
    def __init__(self, name, content, sidebar=None, appbar=None, bottombar=None):
        super().__init__(route=name)
        
        # AppBar
        self.appbar = appbar or ft.AppBar(title=ft.Text("Default AppBar"))
        
        # Sidebar
        self.sidebar = sidebar or ft.Container(
            content=ft.Column(
                controls=[ft.ElevatedButton(text="Menu 1"), ft.ElevatedButton(text="Menu 2")],
                alignment="start",
                expand=True,
            ),
            width=200,
            bgcolor="lightgray",
        )
        
        # BottomBar
        self.bottombar = bottombar or ft.Container(
            content=ft.Row(
                controls=[ft.ElevatedButton(text="Home"), ft.ElevatedButton(text="Settings")],
                alignment="spaceAround",
            ),
            height=50,
            bgcolor="lightblue",
        )
        
        # メインコンテンツ
        self.content = content
        
        # レイアウトを組み立てる
        self.controls = [
            self.appbar,
            ft.Row(
                controls=[
                    self.sidebar,
                    ft.Container(content=self.content, expand=True),
                ],
                expand=True,
            ),
            self.bottombar,
        ]
