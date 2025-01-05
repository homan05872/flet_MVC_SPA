import flet as ft

class Header(ft.AppBar):
    def __init__(self, page:ft.Page):
        self.page = page
        
        # ヘッダーに配置するメニュー
        appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(), # divider
            ft.PopupMenuItem(text="Settings"),
        ]
        
        super().__init__(
            # デザイン設定
            # leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),         # アイコン
            leading=ft.Container(ft.Icon(ft.Icons.ANDROID, size=35,color=ft.colors.WHITE), margin=ft.margin.only(left=10)),         # アイコン
            leading_width=80,                                          # アイコン配置エリア幅
            title=ft.Text("Flet MVC Sample", size=25, color=ft.colors.WHITE, text_align="start"),
            toolbar_height=65,
            bgcolor=ft.colors.BLACK87,
            # actions=[
            #     ft.Container(
            #         content=ft.PopupMenuButton(
            #             items=appbar_items
            #         ),
            #         margin=ft.margin.only(left=50, right=25)
            #     )
            # ]
        )