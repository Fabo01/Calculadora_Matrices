import dearpygui.dearpygui as dpg
from funciones import *

# 1) Contexto y ventana
dpg.create_context()
dpg.create_viewport(title="🧮 Calculadora Matricial", width=640, height=480)

# 2) Tema oscuro básico
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,  (30, 30, 30), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg,   (50, 50, 50), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button,    (70, 70, 70), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (90,90,90), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text,      (200, 200, 200), category=dpg.mvThemeCat_Core)
dpg.bind_theme(global_theme)

# 3) Layout principal
with dpg.window(label="Calculadora Matricial", pos=(10,10), width=480, height=420):
    dpg.add_text("Introduce matrices (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(label="Matriz A", tag="input_A", hint="p.ej. 1 2,3 4")
    dpg.add_input_text(label="Matriz B", tag="input_B", hint="p.ej. 5 6,7 8")
    dpg.add_spacing(count=1)

    # Botones de operaciones
    with dpg.group(horizontal=True):
        dpg.add_button(label="Sumar", tag="btn_sum", width=100)
        dpg.add_button(label="Restar", tag="btn_sub", width=100)
        dpg.add_button(label="Multiplicar", tag="btn_mul", width=120)
    dpg.add_spacing(count=1)
    with dpg.group(horizontal=True):
        dpg.add_button(label="det(A)", tag="btn_det", width=100)
        dpg.add_button(label="inv(A)", tag="btn_inv", width=100)
        dpg.add_button(label="fac_LU(A)", tag="btn_LU", width=100)

    dpg.add_separator()
    dpg.add_text("Resultado:", color=(200,200,200))
    dpg.add_input_text(tag="output", multiline=True, readonly=True, height=200)

    dpg.add_text("Factor L:", color=(200,200,200))
    dpg.add_input_text(tag="out_L", multiline=True, readonly=True, height=80)
    dpg.add_text("Factor U:", color=(200,200,200))
    dpg.add_input_text(tag="out_U", multiline=True, readonly=True, height=80)

# 4) Callback de ejemplo (rellena con tus funciones)
def on_click(sender, app_data):
    # parsear A y B...
    texto_A = dpg.get_value("input_A").strip()
    A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]
    texto_B = dpg.get_value("input_B").strip()
    B = [[float(x) for x in fila.split()] for fila in texto_B.split(",")] if texto_B else None

    try:
        # 1) Factorización LU tiene su propio flujo
        if sender == "btn_LU":
            L, U = factorizacion_LU(A)
            lineas_L = [" ".join(f"{v:.4g}" for v in fila) for fila in L]
            lineas_U = [" ".join(f"{v:.4g}" for v in fila) for fila in U]
            dpg.set_value("out_L", "\n".join(lineas_L))
            dpg.set_value("out_U", "\n".join(lineas_U))
            return 

        # 2) Resto de operaciones definen R
        if sender == "btn_sum":
            R = suma_matriz(A, B)
        elif sender == "btn_sub":
            R = resta_matriz(A, B)
        elif sender == "btn_mul":
            R = producto_matrices(A, B)
        elif sender == "btn_det":
            R = [[determinante_matriz(A)]]
        elif sender == "btn_inv":
            R = inversa_matriz(A)
        else:
            return

        # 3) Mostrar R en el output general
        dpg.set_value("output", "\n".join(str(fila) for fila in R))

        # limpiar las salidas de LU
        dpg.set_value("out_L", "")
        dpg.set_value("out_U", "")

    except Exception as e:
        dpg.set_value("output", f"Error: {e}")
        # y opcionalmente limpiar LU
        dpg.set_value("out_L", "")
        dpg.set_value("out_U", "")

# 5) Asociar callbacks
for btn in ("btn_sum","btn_sub","btn_mul","btn_det","btn_inv", "btn_LU"):
    dpg.set_item_callback(btn, on_click)

# 6) Iniciar GUI
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
