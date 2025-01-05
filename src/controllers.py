import flet as ft
from views import Page1View, Page2View
from common_widgets.app_layout import AppLayout
from typing import Any
from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self, page:ft.Page, app_layout:AppLayout, ViewClass, menu_num:int=None) -> None:
        self.page = page    # アプリウィンドウ
        self.app_layout = app_layout    # アプリレイアウト　※サイドバー&メインコンテンツ
        self.ViewClass = ViewClass      # ビュークラス
        self.view = None                # ビューインスタンス
        self.menu_num = menu_num        # サイドバーのメニュー番号(ビューに対応する)
    
    def show(self) -> None:
        # データをビューに送る
        data = self.send_view_data()
        self.view = self.ViewClass(self, data) # 引数で受け取ったビュークラスのインスタンス化(引数でデータを渡す)
        # メインコンテンツを次のページのUI生成
        self.app_layout.active_view = self.view.build_ui()
        # イベント設定
        self.set_view_event()
        # サイドバーメニューの選択
        self.app_layout.side_menu_select(self.menu_num)
        # ページ更新
        self.page.update()
    
    @abstractmethod
    def set_view_event (self) -> None:
        pass
    
    @abstractmethod
    def send_view_data (self) -> dict[str: Any]|None:
        pass
    
class Page1Controller(BaseController):
    def __init__(self, page, app_layout, model, menu_num=None):
        super().__init__(page, app_layout, Page1View, menu_num)
        self.view:Page1View
        self.model = model
    
    def send_view_data(self):
        return {"message": self.model.get_message()}
    
    def set_view_event(self):
        self.view.navigate_button.on_click = lambda _: self.page.go("/page2")
    
class Page2Controller(BaseController):
    def __init__(self, page, app_layout, model, menu_num=None):
        super().__init__(page, app_layout, Page2View, menu_num)
        self.model = model
        self.view:Page2View
        
    def send_view_data(self):
        pass
    
    def set_view_event(self):
        self.view.navigate_button.on_click = lambda _: self.page.go("/")
        self.view.save_button.on_click = self.save_message
    
    def save_message(self, e):
        new_message = self.view.input_field.value
        self.model.set_message(new_message)
        
# class AppController:
#     def __init__(self, model, page:ft.Page, app_layout):
#         self.model = model
#         self.page = page
#         self.app_layout = app_layout
#         self.page1_view = None
#         self.page2_view = None

#     def set_view_event (self):
#         self.page1_view.navigate_button.on_click = lambda _: self.page.go("/page2")
#         self.page2_view.navigate_button.on_click = lambda _: self.page.go("/")
#         self.page2_view.save_button.on_click = self.save_message
        
#     def go_to_page1(self, e):
#         message = self.model.get_message()
#         self.page1_view = Page1View(self, message)
#         self.app_layout.active_view = self.page1_view.build_ui()
#         self.set_view_event()
#         # self.page1_view.update_message(message)

#     def go_to_page2(self, e):
#         self.page2_view = Page2View(self)
#         self.app_layout.active_view = self.page2_view
#         self.set_view_event()

#     def save_message(self, e):
#         new_message = self.page2_view.input_field.value
#         self.model.set_message(new_message)
