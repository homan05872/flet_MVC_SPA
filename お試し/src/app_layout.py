import flet as ft
from sidebar import Sidebar
from pages import Page1, Page2

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
        self.sidebar = Sidebar(self)
        
        # ページの初期化
        self.page1 = Page1()
        self.page2 = Page2()
        self.page1.app_layout = self
        self.page2.app_layout = self
        
        # メインコンテンツ
        self._active_view = self.page1.build_ui()
        # self._active_view :ft.Control = ft.Column(
        #     controls=[ft.Text("Active View")],
        #     alignment="center",
        #     horizontal_alignment="center",
        #     )
        
        # AppLayoutへ作成したUI要素を配置
        self.controls = [
            self.sidebar,                   # サイドバー
            self.toggle_nav_rail_button,    # サイドバー表示・非表示切替
            self._active_view               # メインコンテンツ
            ]

    def show_page1(self, e=None):
        self._active_view = self.page1.build_ui()
        self.update()

    def show_page2(self, e=None):
        self._active_view = self.page2.build_ui()
        self.update()
    
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