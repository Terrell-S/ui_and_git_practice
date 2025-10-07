import flet as ft
import random

def main(page: ft.Page):
    page.title = "Sound Localization Robot"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Example state variables
    sound_intensity = ft.Text("73.5 dB", size=28, weight=ft.FontWeight.BOLD)
    sound_direction = ft.Text("42°", size=28, weight=ft.FontWeight.BOLD)
    robot_distance = ft.Text("1.8 m", size=28, weight=ft.FontWeight.BOLD)
    system_status = ft.Text("connection Established", size=28, weight=ft.FontWeight.BOLD)

    # Current mode name
    current_mode_name = ft.Text("Mode: Standby", size=28, weight=ft.FontWeight.BOLD)

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
        if system_status.value == "Active":
            system_status.value = "Idle"
        else:
            system_status.value = "Active"

        sound_intensity.value = f"{random.uniform(60, 90):.1f} dB"
        sound_direction.value = f"{random.randint(0, 360)}°"
        robot_distance.value = f"{random.uniform(1.0, 3.0):.2f} m"
        page.update()

    # Handler for popup menu selection
    def mode_selected(e):
        current_mode_name.value = f"Mode: {e.control.data}"
        page.update()
        # Optional: send command to backend

    # Popup menu button
    mode_popup = ft.PopupMenuButton(
        content=ft.Text("Manual Mode Select"),  # default displayed name
        items=[
            ft.PopupMenuItem(text="Standby", on_click=mode_selected, data="Manual Standby"),
            ft.PopupMenuItem(text="Search", on_click=mode_selected, data="Manual Search"),
            ft.PopupMenuItem(text="Found", on_click=mode_selected, data="Manual Found"),
            ft.PopupMenuItem(text="Return", on_click=mode_selected, data="Manual Return"),
        ],
        clip_behavior = ft.ClipBehavior.ANTI_ALIAS,
        menu_position = ft.PopupMenuPosition.UNDER
    )

    # Layout
    page.add(
        ft.AppBar(title=ft.Text("Sound Localization Robot"), center_title=True),
        ft.Column(
            [
                ft.Container(height=20),
                data_card("Connection Status", system_status),
                data_card("Current Mode",current_mode_name),
                mode_popup,
                ft.Container(height=10),
                data_card("Sound Direction", sound_direction),
                data_card("Distance to Source", robot_distance),
                data_card("Sound Intensity", sound_intensity),
                ft.Container(height=20),
                ft.ElevatedButton(
                    "Refresh Data",
                    icon=ft.Icons.REFRESH,
                    on_click=refresh_data,
                    style=ft.ButtonStyle(
                        padding=20,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
    )

ft.app(target=main)
