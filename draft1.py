import flet as ft


def main(page: ft.Page):
    page.title = "Sound Localization Robot"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Example state variables
    sound_intensity = ft.Text("73.5 dB", size=28, weight=ft.FontWeight.BOLD)
    sound_direction = ft.Text("Connection Established", size=28, weight=ft.FontWeight.BOLD)
    robot_distance = ft.Text("1.8 m", size=28, weight=ft.FontWeight.BOLD)
    system_status = ft.Text("Standby", size=28, weight=ft.FontWeight.BOLD)

    # Current mode
    selected_mode_text = ft.Text("Current Mode: Standby", size=20)

    # Helper: Data card widget
    def data_card(title, value_widget):
        return ft.Card(
            elevation=6,
            content=ft.Container(
                padding=20,
                border_radius=15,
                content=ft.Column(
                    [
                        ft.Text(title, size=18, color=ft.Colors.GREY_400),
                        ft.Container(height=6),
                        value_widget,
                    ]
                ),
            ),
        )

    # Refresh button action
    def refresh_data(e):
        # simple example: simulate changing data
        if system_status.value == "Active":
            system_status.value = "Idle"
        else:
            system_status.value = "Active"

        # update text values
        import random
        sound_intensity.value = f"{random.uniform(60, 90):.1f} dB"
        sound_direction.value = f"{random.randint(0, 360)}°"
        robot_distance.value = f"{random.uniform(1.0, 3.0):.2f} m"

        page.update()

    # Mode selection handler
    def mode_changed(e):
        selected_mode_text.value = f"Current Mode: {e.control.value}"
        page.update()

    # Mode selection handler
    def mode_changed(e):
        selected_mode_text.value = f"Current Mode: {e.control.value}"
        page.update()
        # Optional: send command to robot backend here

    # Dropdown menu for robot modes
    mode_dropdown = ft.Dropdown(
        width=200,
        value="Standby",
        options=[
            ft.dropdown.Option("Standby"),
            ft.dropdown.Option("Search"),
            ft.dropdown.Option("Found"),
            ft.dropdown.Option("Return"),
        ],
        on_change=mode_changed
    )

    # Layout
    page.add(
        ft.AppBar(title=ft.Text("Sound Localization Robot"), center_title=True),
        ft.Column(
            [
                ft.Container(height=20),
                data_card("Connection Status", sound_direction),
                data_card("System Mode", selected_mode_text),
                mode_dropdown,
                ft.Container(height=10),
                data_card("Distance to Source", robot_distance),
                data_card("Sound Intensity", sound_intensity),
                ft.Container(height=20),
                ft.ElevatedButton(
                    "Refresh Data",
                    icon=ft.Icons.REFRESH,
                    on_click=refresh_data,
                    style=ft.ButtonStyle(padding=20, shape=ft.RoundedRectangleBorder(radius=10)),
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            #horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
    )


# Run the app
ft.app(target=main)
