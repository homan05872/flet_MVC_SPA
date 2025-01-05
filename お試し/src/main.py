import flet as ft
from app_layout import AppLayout

class TrelloApp(AppLayout):
    def __init__(self, page:ft.Page):
        # アプリウィンドウを保持
        self.page = page
        
        # ヘッダーに配置するメニュー
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(), # divider
            ft.PopupMenuItem(text="Settings"),
        ]
        
        # ヘッダー
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Trolli", size=32, text_align="start"),
            toolbar_height=75,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ]
        )
        
        # ヘッダー配置
        self.page.appbar = self.appbar
        # self.page.update()
        
        # AppLayoutの生成
        super().__init__(
            self,
            tight=True,
            expand=True,
            vertical_alignment="start",
        )

if __name__  == "__main__":
    
    def main(page: ft.Page):
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = ft.colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        
    ft.app(main, view=ft.WEB_BROWSER)