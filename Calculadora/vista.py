import dearpygui.dearpygui as dpg
from funciones import (
    suma_matriz,
    resta_matriz,
    producto_matrices,
    determinante_matriz,
    inversa_matriz,
    factorizacion_LU,
    resolver_sistema_gauss
)

# 1) Contexto y viewport
dpg.create_context()
dpg.create_viewport(title="Calculadora Matricial", width=720, height=790)

# 2) Tema oscuro
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,  (30,30,30))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg,   (50,50,50))
        dpg.add_theme_color(dpg.mvThemeCol_Button,    (70,70,70))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(90,90,90))
        dpg.add_theme_color(dpg.mvThemeCol_Text,      (200,200,200))
dpg.bind_theme(global_theme)

# 3) Ventana binaria: A <op> B
with dpg.window(label="Operaciones entre matrices",
                pos=(10,10), width=330, height=350):
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="bin_A", hint="ej: 1 2,3 4")
    dpg.add_text("Matriz B", color=(200,200,200))
    dpg.add_input_text(tag="bin_B", hint="ej: 5 6,7 8")
    dpg.add_spacing(count=1)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Sumar",    tag="btn_sum", width=90)
        dpg.add_button(label="Restar",   tag="btn_sub", width=90)
        dpg.add_button(label="Multiplicar",tag="btn_mul",width=110)
    dpg.add_separator()
    dpg.add_text("Resultado:", color=(200,200,200))
    dpg.add_input_text(tag="out_bin", multiline=True, readonly=True, height=150)

# 4) Ventana unaria: operaciones sobre A
with dpg.window(label="Operaciones sobre una matriz",
                pos=(360,10), width=330, height=500):
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="uni_A", hint="ej: 1 2,3 4")
    dpg.add_spacing(count=1)
    with dpg.group(horizontal=True):
        dpg.add_button(label="det(A)",   tag="btn_det", width=90)
        dpg.add_button(label="inv(A)",   tag="btn_inv", width=90)
        dpg.add_button(label="fac LU(A)",tag="btn_LU",  width=110)
    dpg.add_separator()
    dpg.add_text("Resultado:", color=(200,200,200))
    dpg.add_input_text(tag="out_uni", multiline=True, readonly=True, height=100)
    dpg.add_text("Factor L:", color=(200,200,200))
    dpg.add_input_text(tag="out_L", multiline=True, readonly=True, height=100)
    dpg.add_text("Factor U:", color=(200,200,200))
    dpg.add_input_text(tag="out_U", multiline=True, readonly=True, height=100)

# — Ventana 3: Resolver sistemas A·x = b —
with dpg.window(label="Resolución de Sistemas Lineales",
                pos=(10, 380), width=330, height=300):
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="sys_A", hint="p.ej. 1 2,3 4")
    dpg.add_text("Vector b (entradas separadas por espacios)", color=(200,200,200))
    dpg.add_input_text(tag="sys_b", hint="p.ej. 5 6")
    dpg.add_spacing(count=1)
    dpg.add_button(label="Resolver sistema", tag="btn_solve", width=200)
    dpg.add_separator()
    dpg.add_text("Solución x:", color=(200,200,200))
    dpg.add_input_text(tag="out_sys", multiline=True, readonly=True, height=100)


# 5) Callback unificado
def on_click(sender, app_data):
    try:
        # — operaciones binarias —
        if sender in ("btn_sum","btn_sub","btn_mul"):
            texto_A = dpg.get_value("bin_A").strip()
            texto_B = dpg.get_value("bin_B").strip()
            A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]
            B = [[float(x) for x in fila.split()] for fila in texto_B.split(",")]
            if sender == "btn_sum":
                R = suma_matriz(A, B)
            elif sender == "btn_sub":
                R = resta_matriz(A, B)
            else:
                R = producto_matrices(A, B)
            # volcamos en ventana binaria
            dpg.set_value("out_bin", "\n".join(str(fila) for fila in R))
            return

        # — operaciones unarias —
        if sender in ("btn_det","btn_inv","btn_LU"):
            texto_A = dpg.get_value("uni_A").strip()
            A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]

            if sender == "btn_det":
                val = determinante_matriz(A)
                dpg.set_value("out_uni", str(val))
                dpg.set_value("out_L","")
                dpg.set_value("out_U","")
            elif sender == "btn_inv":
                invA = inversa_matriz(A)
                dpg.set_value("out_uni", "\n".join(str(fila) for fila in invA))
                dpg.set_value("out_L","")
                dpg.set_value("out_U","")
            else:  # fac LU
                L, U = factorizacion_LU(A)
                dpg.set_value("out_uni", "Ver factores L y U")
                dpg.set_value("out_L", "\n".join(" ".join(f"{v:.4g}" for v in fila) for fila in L))
                dpg.set_value("out_U", "\n".join(" ".join(f"{v:.4g}" for v in fila) for fila in U))
            return
        
                # — Resolver sistema por Gauss —
        if sender == "btn_solve":
            # parsear A
            texto_A = dpg.get_value("sys_A").strip()
            A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]
            # parsear b
            b = [float(x) for x in dpg.get_value("sys_b").split()]
            # resolver
            x = resolver_sistema_gauss(A, b)
            # mostrar
            dpg.set_value("out_sys", "  ".join(f"{xi:.6g}" for xi in x))
            return


    except Exception as e:
        # Difusión de error en la ventana correspondiente
        if sender in ("btn_sum","btn_sub","btn_mul"):
            dpg.set_value("out_bin", f"Error: {e}")
        else:
            dpg.set_value("out_uni", f"Error: {e}")
            dpg.set_value("out_L","")
            dpg.set_value("out_U","")

# 6) Asignar callbacks
for tag in ("btn_sum","btn_sub","btn_mul","btn_det","btn_inv","btn_LU","btn_solve"):
    dpg.set_item_callback(tag, on_click)

# 7) Ejecutar GUI
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
