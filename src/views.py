import flet as ft


class Page1View(ft.UserControl):
    def __init__(self, data):
        super().__init__()
        self.message_text = ft.Text(data["message"])  # 初期化

    def build_ui(self):
        self.label = ft.Text("Page 1", size=30)
        self.navigate_button = ft.ElevatedButton(
            text="Go to Page 2"
        )
        return ft.Container(
                ft.Column(
                    controls=[
                        self.label,
                        self.message_text,  # message_textをUIに追加
                        self.navigate_button,
                    ],
                    alignment="center",
                ),
        )
    

class Page2View(ft.UserControl):
    def __init__(self, *args):
        super().__init__()

    def build_ui(self):
        self.label = ft.Text("Page 2", size=30)
        self.input_field = ft.TextField(label="Enter a new message")
        self.navigate_button = ft.ElevatedButton(
            text="Go to Page 1",
        )
        self.save_button = ft.ElevatedButton(
            text="Save Message",
        )
        return ft.Container(
                ft.Column(
                    controls=[
                        self.label,
                        self.input_field,
                        self.save_button,
                        self.navigate_button,
                    ],
                    alignment="center",
                ),
        )
    