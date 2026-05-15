import flet as ft


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorites = []

    # ── Виджеты приветствия ──────────────────────────────────────────
    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', expand=False)

    # ── История ──────────────────────────────────────────────────────
    history_list = ft.Column(spacing=2)
    greeting_text = ft.Text('История приветствий:', weight=ft.FontWeight.BOLD)

    # ── Избранное ────────────────────────────────────────────────────
    favorites_title = ft.Text('⭐ Любимые имена:', weight=ft.FontWeight.BOLD)
    favorites_list = ft.Column(spacing=2)
    no_favorites_hint = ft.Text(
        'Пока пусто — добавьте имя из истории',
        italic=True,
        color=ft.Colors.GREY_500,
        size=12,
    )

    def rebuild_history():
        history_list.controls.clear()
        for name in reversed(greeting_history):
            is_fav = name in favorites

            def make_add(n):
                def add(e):
                    add_to_favorites(n)
                return add

            row = ft.Row(
                controls=[
                    ft.Text(f'• {name}', expand=True),
                    ft.IconButton(
                        icon=ft.Icons.STAR if is_fav else ft.Icons.STAR_BORDER,
                        icon_color=ft.Colors.AMBER if is_fav else ft.Colors.GREY_400,
                        tooltip='Уже в избранном' if is_fav else 'Добавить в избранное',
                        on_click=make_add(name),
                        disabled=is_fav,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            history_list.controls.append(row)

    def rebuild_favorites():
        favorites_list.controls.clear()
        if not favorites:
            favorites_list.controls.append(no_favorites_hint)
            return
        for name in favorites:
            def make_remove(n):
                def remove(e):
                    favorites.remove(n)
                    rebuild_history()
                    rebuild_favorites()
                    page.update()
                return remove

            chip = ft.Chip(
                label=ft.Text(name),
                leading=ft.Icon(ft.Icons.STAR, color=ft.Colors.AMBER),
                delete_icon=ft.Icon(ft.Icons.CLOSE, size=16),
                on_delete=make_remove(name),
                bgcolor=ft.Colors.AMBER_50,
            )
            favorites_list.controls.append(chip)

    def add_to_favorites(name: str):
        if name and name not in favorites:
            favorites.append(name)
            rebuild_history()
            rebuild_favorites()
            page.update()

    def text_name(e):
        name = text_input.value.strip()
        if name:
            text_hello.value = f'Привет! {name}'
            text_hello.color = ft.Colors.BLUE
            text_input.value = ''
            greeting_history.append(name)
            rebuild_history()
            rebuild_favorites()
        else:
            text_hello.value = 'Введите корректное имя!'
            text_hello.color = ft.Colors.RED_900
        page.update()

    text_input.on_submit = text_name

    def clear_history(e):
        greeting_history.clear()
        rebuild_history()
        page.update()

    def thememode(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        page.update()

    # ── Кнопки управления ────────────────────────────────────────────
    btn = ft.ElevatedButton('Отправить', icon=ft.Icons.SEND, on_click=text_name)
    clear_button = ft.IconButton(
        icon=ft.Icons.DELETE_OUTLINE,
        tooltip='Очистить историю',
        on_click=clear_history,
    )
    theme_btn = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_6,
        tooltip='Сменить тему',
        on_click=thememode,
    )

    input_row = ft.Row(
        controls=[text_input, btn, clear_button, theme_btn],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # ── Колонки истории и избранного рядом ───────────────────────────
    rebuild_favorites()  # показать подсказку сразу

    history_card = ft.Container(
        content=ft.Column(
            controls=[greeting_text, history_list],
            spacing=6,
            scroll=ft.ScrollMode.AUTO,
        ),
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=12,
        padding=12,
        expand=True,
        height=250,
    )

    favorites_card = ft.Container(
        content=ft.Column(
            controls=[favorites_title, favorites_list],
            spacing=6,
            scroll=ft.ScrollMode.AUTO,
        ),
        border=ft.border.all(1, ft.Colors.AMBER_200),
        border_radius=12,
        padding=12,
        expand=True,
        height=250,
        bgcolor=ft.Colors.AMBER_50,
    )

    two_columns = ft.Row(
        controls=[history_card, favorites_card],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
    )

    page.add(
        text_hello,
        input_row,
        ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
        two_columns,
    )


ft.app(main_page, view=ft.AppView.WEB_BROWSER)
