import flet as ft
from .sidebar import Sidebar

class AppLayout(ft.Row):
    def __init__(self, *args, **kwargs):
        """ アプリのレイアウト生成
        """
        # サイドバー
        self.sidebar = Sidebar(self)
        # サイドバーを折りたたむボタン
        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.icons.ARROW_CIRCLE_RIGHT,  # selectedがTrueの時に表示するアイコン
            on_click=self.toggle_nav_rail
        )
        # メインコンテンツ
        self._active_view :ft.Control = ft.Column(
            controls=[ft.Container(ft.Text("Active View"),margin=10)],
            alignment="center",
            horizontal_alignment="center",
        )
        # AppLayoutへ作成したUI要素を配置
        controls = [
            self.sidebar,                   # サイドバー
            self.toggle_nav_rail_button,    # サイドバー表示・非表示切替
            self._active_view               # メインコンテンツ
        ]
        # UI生成
        super().__init__(
            controls=controls,
            tight=True,
            expand=True,
            vertical_alignment="start",
            **kwargs
        )
        
    @property
    def active_view(self):
        """ _active_view(メインコンテンツ)のゲッター

        Returns:
            _type_: _description_
        """
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        """ _active_view(メインコンテンツ)のセッター ※メインコンテンツ切替処理

        Args:
            view (UI要素): メインコンテンツに配置したいUI要素
        """
        self._active_view = view                # 表示したいメインコンテンツ保持
        self.controls[2] = self._active_view    # メインコンテンツ部分を置き換える
        self.update()   # ページ更新
    
    def toggle_nav_rail(self, e):
        """ サイドバーの表示/非表示の切り替え処理
        Args:
            e (イベント): イベント
        """
        self.sidebar.visible = not self.sidebar.visible     # サイドバー表示/非表示を切り替える
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected # ボタンの表示切替
        self.page.update()  # ページ更新
    
    def side_menu_select(self, menu_num:int=None):
        self.sidebar.menu_select(menu_num)