import flet as ft
from view import create_page1, create_page2

def main(page: ft.Page):
    # 初期ページをセット
    page.views.append(create_page1())
    
    # ページ切り替えのロジック
    def navigate_to(page_name):
        if page_name == "/page1":
            page.views.clear()
            page.views.append(create_page1())
        elif page_name == "/page2":
            page.views.clear()
            page.views.append(create_page2())
        page.update()

    # ナビゲーション用ボタン
    page.controls.append(
        ft.Row(
            controls=[
                ft.ElevatedButton(text="Go to Page 1", on_click=lambda _: navigate_to("page1")),
                ft.ElevatedButton(text="Go to Page 2", on_click=lambda _: navigate_to("page2")),
            ]
        )
    )
    page.update()

ft.app(target=main)