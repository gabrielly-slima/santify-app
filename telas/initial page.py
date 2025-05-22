import flet as ft


def main(page: ft.Page):
    page.title = "Santify App"
    page.vertical_alignment = "top" # Alinha a imagem no topo
    page.horizontal_alignment = "center" # Alinha a imagem no centro

    page.add(
        ft.Image(
            src=r"c:\Users\DELL P75F\Downloads\img-tela-inicial.png",  # Substitua pelo caminho da sua imagem
            width=page.width,  # Define a largura da imagem para a largura da tela
            height=page.height, # Define a altura da imagem para a altura da tela
            fit=ft.ImageFit.COVER  # Define o ajuste da imagem para preencher a tela
        )
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")


