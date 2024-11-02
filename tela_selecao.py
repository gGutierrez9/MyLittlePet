import flet as ft

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.title = 'MyLittlePet'
    page.bgcolor = '#FFDD78'
    page.window_width = 287.38
    page.window_height = 585
   
    

    page.add(
        ft.CupertinoButton('Login',color='white',bgcolor=ft.colors.BROWN_500,width=200),
        ft.CupertinoButton('Cadastro',color='white',bgcolor=ft.colors.BROWN_500,width=200),

        ft.Row(
            ft.IconButton(  )

        )
    )

    page.update()

ft.app(target=main)