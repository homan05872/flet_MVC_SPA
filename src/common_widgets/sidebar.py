import flet as ft
 

class Sidebar(ft.Container):
 
    def __init__(self, app_layout):
        super().__init__()
        self.app_layout = app_layout    # アプリレイアウト　※サイドバー&メインコンテンツ
        
        # メニューボタン
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("ページ１"),
                label="ページ１",
                icon=ft.Icon(ft.Icons.MESSAGE_SHARP),
                selected_icon=ft.Icon(ft.Icons.MESSAGE_SHARP)
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("ページ２"),
                label="ページ２",
                icon=ft.Icon(ft.Icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED),
                selected_icon=ft.Icon(ft.Icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED)
            ),
 
        ]
        
        # サイドバーメニュー
        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,    # ←上記で作ったメニューボタン
            bgcolor=ft.colors.BLUE_GREY_300,
            extended=True,
            expand=True
        )
    
    # サイドバー生成
    def build(self):
        self.content = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Menu", size=20),
                ],alignment="center"),
                # 仕切り線
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,      # ←上記で作ったサイドバーメニュー
                # 仕切り線
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220,
                ),
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.colors.BLUE_GREY_300,
        )
 
    def top_nav_change(self, e:ft.ControlEvent):
        self.menu_select(e.control.selected_index)
        if self.top_nav_rail.selected_index == 0:
            self.page.go("/")
        elif self.top_nav_rail.selected_index == 1:
            self.page.go("/page2")
        self.update()
        
    def menu_select(self, menu_num:int=None):
        if 0 <= menu_num < len(self.top_nav_items):
            self.top_nav_rail.selected_index = menu_num
        else:
            self.top_nav_rail.selected_index = None