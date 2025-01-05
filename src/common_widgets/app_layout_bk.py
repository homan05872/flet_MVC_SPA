import flet as ft
from .sidebar import Sidebar

class AppLayout(ft.Row):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        # window提供変数
        # self.page = page
        
        # サイドバーを折りたたむボタン
        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.icons.ARROW_CIRCLE_RIGHT,  # selectedがTrueの時に表示するアイコン
            on_click=self.toggle_nav_rail
        )
        # サイドバー
        self.sidebar = Sidebar()
        
        # メインコンテンツ
        self.message_text = ft.Text("message")  # 初期化
        self.label = ft.Text("Page 1", size=30)
        self.navigate_button = ft.ElevatedButton(
            text="Go to Page 2"
        )
        self._active_view :ft.Control = ft.Column(
            # controls=[ft.Text("Active View")],
            controls=[
                ft.Column(
                    controls=[
                        self.label,
                        self.message_text,  # message_textをUIに追加
                        self.navigate_button,
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            horizontal_alignment="center",
            )
        
        # AppLayoutへ作成したUI要素を配置
        self.controls = [
            self.sidebar,                   # サイドバー
            self.toggle_nav_rail_button,    # サイドバー表示・非表示切替
            self._active_view               # メインコンテンツ
            ]

    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()
    
    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()