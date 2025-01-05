import flet as ft

class Page(ft.UserControl):
    def build(self):
        raise NotImplementedError("Subclasses must implement the build method")

class Page1(Page):
    def build_ui(self):
        return ft.Column(
            controls=[
                ft.Text("This is Page 1", size=20),
                ft.Button("Go to Page 2", on_click=self.app_layout.show_page2)
            ],
            alignment="center",
            horizontal_alignment="center",
        )

class Page2(Page):
    def build_ui(self):
        return ft.Column(
            controls=[
                ft.Text("This is Page 2", size=20),
                ft.Button("Go to Page 1", on_click=self.app_layout.show_page1)
            ],
            alignment="center",
            horizontal_alignment="center",
        )
