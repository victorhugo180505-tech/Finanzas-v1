import flet as ft
import flet_charts as ftc

# import logica as lg  # Descomenta cuando tengas estos módulos
# import archivos as f


def main(page: ft.Page):
    page.title = "Financial Projector Papu Edition :V"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # ==========================================
    # 0. ESTADOS GLOBALES (MEMORIA TEMPORAL)
    # ==========================================
    ruta_archivo_db = "./libro1.json"
    movimientos_registrados = []

    # Controles que se usan en callbacks
    nombre_input = ft.TextField(label="Name")
    monto_input = ft.TextField(label="Amount", prefix="$")
    tipo_input = ft.Dropdown(
        label="Type",
        options=[
            ft.DropdownOption("ingreso"),
            ft.DropdownOption("gasto"),
            ft.DropdownOption("deuda"),
        ],
    )
    fecha_input = ft.TextField(label="Date (YYYY-MM-DD)")
    input_ruta_db = ft.TextField(label="DB Path", value=ruta_archivo_db, width=400)

    # ==========================================
    # 1. LÓGICA AUXILIAR
    # ==========================================
    def refrescar_tabla():
        nonlocal movimientos_registrados

        # movimientos_registrados = f.obtenerMovimientos()  # Lógica real
        movimientos_registrados = [
            {"id": 1, "nombre": "Sueldo", "tipo": "ingreso", "monto": 500, "fecha": "2026-05-08", "estado": "activo", "porc_penalizacion": 0},
            {"id": 2, "nombre": "Renta", "tipo": "gasto", "monto": 300, "fecha": "2026-05-10", "estado": "activo", "porc_penalizacion": 0},
        ]

        tabla_movimientos.rows.clear()
        for mov in movimientos_registrados:
            tabla_movimientos.rows.append(crear_fila_movimiento(mov))

        page.update()

    def eliminar_mov(id_mov):
        # f.eliminarMovimiento(id_mov)
        refrescar_tabla()

    def cerrar_dialogo():
        page.pop_dialog()
        page.update()

    # ==========================================
    # 2. PESTAÑA MOVIMIENTOS (TAB 1)
    # ==========================================
    def crear_fila_movimiento(mov):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Checkbox(value=mov["estado"] == "activo")),
                ft.DataCell(ft.Text(mov["nombre"])),
                ft.DataCell(ft.Text(mov["tipo"])),
                ft.DataCell(ft.Text(f"${mov['monto']}")),
                ft.DataCell(ft.Text(f"{mov['porc_penalizacion']}%" if mov["tipo"] == "deuda" else "N/A")),
                ft.DataCell(
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=lambda e, id_mov=mov["id"]: eliminar_mov(id_mov),
                    )
                ),
            ]
        )

    tabla_movimientos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Active/Disabled")),
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Type")),
            ft.DataColumn(ft.Text("Amount")),
            ft.DataColumn(ft.Text("Penalization")),
            ft.DataColumn(ft.Text("Actions")),
        ],
        rows=[],
    )

    def guardar_nuevo_movimiento(e):
        # lg.Movimiento(...)  / f.insertarMovimiento(...)
        page.pop_dialog()
        refrescar_tabla()

    dlg_add_mov = ft.AlertDialog(
        title=ft.Text("Add Movement"),
        content=ft.Container(
            content=ft.Column(
                [nombre_input, tipo_input, monto_input, fecha_input],
                height=300,
                width=420,
                tight=True,
            )
        ),
        actions=[
            ft.TextButton("Save", on_click=guardar_nuevo_movimiento),
            ft.TextButton("Cancel", on_click=lambda e: cerrar_dialogo()),
        ],
        modal=True,
    )

    def abrir_dialogo_add(e):
        page.show_dialog(dlg_add_mov)
        page.update()

    vista_movimientos = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Movements Manager", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[tabla_movimientos],
                    scroll=ft.ScrollMode.AUTO,
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.ADD,
                    on_click=abrir_dialogo_add,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        padding=20,
        expand=True,
    )

    refrescar_tabla()

    # ==========================================
    # 3. PESTAÑA PROYECCIÓN (TAB 2)
    # ==========================================
    chart_data = [
        ftc.LineChartDataPoint(0, 1000),
        ftc.LineChartDataPoint(2, 1000),
        ftc.LineChartDataPoint(4, 1500),
        ftc.LineChartDataPoint(6, 1200),
        ftc.LineChartDataPoint(10, 1200),
    ]

    grafica_proyeccion = ftc.LineChart(
        data_series=[
            ftc.LineChartData(
                points=chart_data,
                stroke_width=4,
                curved=True,
                color=ft.Colors.CYAN,
            )
        ],
        border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE)),
        left_axis=ftc.ChartAxis(label_size=40),
        bottom_axis=ftc.ChartAxis(label_size=40),
        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLACK),
        expand=True,
    )

    vista_proyeccion = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cash Flow Projection", size=20, weight=ft.FontWeight.BOLD),
                ft.Row([ft.Text("< 2026-05-06 to 2026-05-19 >")]),
                ft.Container(content=grafica_proyeccion, height=300, padding=20),
                ft.Text("Pushed Deudas (Not Paid):", weight=ft.FontWeight.BOLD),
                ft.Text("Pending: 1320.0 for 2026-06-06", color=ft.Colors.RED_300),
            ]
        ),
        padding=20,
        expand=True,
    )

    # ==========================================
    # 4. PESTAÑA CONFIGURACIÓN (TAB 3)
    # ==========================================
    radio_metodo = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="snowball", label="Snowball"),
                ft.Radio(value="avalanche", label="Avalanche"),
                ft.Radio(value="smartmode", label="Smart mode (Default)"),
            ]
        )
    )

    radio_tema = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="dark", label="Dark (Default)"),
                ft.Radio(value="light", label="Light"),
                ft.Radio(value="darker", label="Darker"),
            ]
        )
    )

    def cambiar_tema(e):
        if radio_tema.value == "light":
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def reset_movements_click(e):
        # f.reiniciarDB()
        refrescar_tabla()
        print("Movements reset called.")

    vista_settings = ft.Container(
        content=ft.Column(
            [
                ft.Text("Application Settings", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Column([ft.Text("Payment Method", weight=ft.FontWeight.BOLD), radio_metodo]),
                        ft.VerticalDivider(width=40),
                        ft.Column(
                            [
                                ft.Text("Theme Options", weight=ft.FontWeight.BOLD),
                                radio_tema,
                                ft.Button(content=ft.Text("Apply Theme"), on_click=cambiar_tema),
                            ]
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Divider(height=40),
                ft.Button(
                    content=ft.Row(
                        [ft.Icon(ft.Icons.WARNING), ft.Text("Reset movements", color=ft.Colors.RED_300)],
                        tight=True,
                    ),
                    on_click=reset_movements_click,
                ),
            ]
        ),
        padding=20,
        expand=True,
    )

    # ==========================================
    # 5. ESTRUCTURA PRINCIPAL (TABS)
    # ==========================================
    main_tabs = ft.Tabs(          # FIX: asignar a variable
        length=3,
        selected_index=0,
        animation_duration=300,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="Movements", icon=ft.Icons.LIST_ALT),
                        ft.Tab(label="Projection", icon=ft.Icons.SHOW_CHART),
                        ft.Tab(label="Settings",   icon=ft.Icons.SETTINGS),
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        vista_movimientos,
                        vista_proyeccion,
                        vista_settings,
                    ],
                ),
            ],
        ),
    )

    # ==========================================
    # 6. MODAL DE BIENVENIDA
    # ==========================================
    def continuar_session(e):
        print(f"Opening DB: {input_ruta_db.value}")
        page.pop_dialog()
        refrescar_tabla()

    dlg_welcome = ft.AlertDialog(
        title=ft.Text("Welcome to Financial Proyector!"),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Confirm or replace the route below:"),
                    input_ruta_db,
                    ft.Text("(Optional)", italic=True, size=12),
                ],
                height=200,
                width=460,
                tight=True,
            )
        ),
        actions=[
            ft.Button(
                content=ft.Row(                        # FIX: content= recibe Control, no string
                    [ft.Icon(ft.Icons.PLAY_ARROW_ROUNDED), ft.Text("Continue")],
                    tight=True,
                ),
                on_click=continuar_session,
            )
        ],
        modal=True,
    )

    # FIX: pasar la instancia main_tabs, no la clase ft.Tabs
    page.add(main_tabs)
    


if __name__ == "__main__":
    ft.run(main)
