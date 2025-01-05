import flet as ft
from models import AppModel
from controllers import Page1Controller, Page2Controller
from common_widgets.app_layout import AppLayout

def main(page: ft.Page):    
    # 共通で使用するレイアウト定義
    app_layout = AppLayout(page) # アプリレイアウト　※ヘッダー&サイドバー&メインコンテンツ
    
    # アプリレイアウト(app_layout)をアプリウィンドウに配置
    page.add(app_layout)
    
    # Model, Controllerの初期化 ※ViewはAppController内で行う
    model = AppModel()
    # URL設定
    route_settings = {
        "/": Page1Controller(page, app_layout, model, menu_num=0),
        "/page2": Page2Controller(page, app_layout, model, menu_num=1),
    }
    
    # ページ遷移メソッド設定
    def route_change(e: ft.RouteChangeEvent):
        route_settings[page.route].show()   
    page.on_route_change = route_change
    
    # 初期ページを表示
    page.go("/")

ft.app(target=main)
