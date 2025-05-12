import dearpygui.dearpygui as dpg
from funciones import ( #importar funciones de operaciones matriciales
    suma_matriz,
    resta_matriz,
    producto_matrices,
    determinante_matriz,
    inversa_matriz,
    factorizacion_LU,
    resolver_sistema_gauss
)
#crea contexto(contenedor) y ventana principal de la calculadora
dpg.create_context()
dpg.create_viewport(title="Calculadora Matricial", width=720, height=790)

#se define un tema oscuro para la interfaz y lo aplica 
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,  (30,30,30))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg,   (50,50,50))
        dpg.add_theme_color(dpg.mvThemeCol_Button,    (70,70,70))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(90,90,90))
        dpg.add_theme_color(dpg.mvThemeCol_Text,      (200,200,200))
dpg.bind_theme(global_theme)

#crea una ventana para operaciones entre dos matrices
with dpg.window(label="Operaciones entre matrices",
                pos=(10,10), width=330, height=350):
    #agrega campos de textos para ingresar las matrices A y B
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="bin_A", hint="ej: 1 2,3 4")
    dpg.add_text("Matriz B", color=(200,200,200))
    dpg.add_input_text(tag="bin_B", hint="ej: 5 6,7 8")
    dpg.add_spacing(count=1)
    #agrega botones para realizar operaciones entre matrices
    with dpg.group(horizontal=True):
        dpg.add_button(label="Sumar",    tag="btn_sum", width=90)
        dpg.add_button(label="Restar",   tag="btn_sub", width=90)
        dpg.add_button(label="Multiplicar",tag="btn_mul",width=110)
    #agrega un campo de texto para mostrar el resultado
    dpg.add_separator()
    dpg.add_text("Resultado:", color=(200,200,200))
    dpg.add_input_text(tag="out_bin", multiline=True, readonly=True, height=150)

#crea una ventana para operaciones sobre una matriz
with dpg.window(label="Operaciones sobre una matriz",
                pos=(360,10), width=330, height=500):
    #agrega campos de texto para ingresar la matriz A
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="uni_A", hint="ej: 1 2,3 4")
    dpg.add_spacing(count=1)
    #agrega botones para realizar operaciones sobre la matriz A
    with dpg.group(horizontal=True):
        dpg.add_button(label="det(A)",   tag="btn_det", width=90)
        dpg.add_button(label="inv(A)",   tag="btn_inv", width=90)
        dpg.add_button(label="fac LU(A)",tag="btn_LU",  width=110)
    #agrega campos de texto para mostrar los resultados
    dpg.add_separator()
    dpg.add_text("Resultado:", color=(200,200,200))
    dpg.add_input_text(tag="out_uni", multiline=True, readonly=True, height=100)
    dpg.add_text("Factor L:", color=(200,200,200))
    dpg.add_input_text(tag="out_L", multiline=True, readonly=True, height=100)
    dpg.add_text("Factor U:", color=(200,200,200))
    dpg.add_input_text(tag="out_U", multiline=True, readonly=True, height=100)

#crea una ventana para resolver sistemas lineales
with dpg.window(label="Resolución de Sistemas Lineales",
                pos=(10, 380), width=330, height=300):
    #agrega campos de texto para ingresar la matriz A y el vector b
    dpg.add_text("Matriz A (filas separadas por ',')", color=(200,200,200))
    dpg.add_input_text(tag="sys_A", hint="p.ej. 1 2,3 4")
    dpg.add_text("Vector b (entradas separadas por espacios)", color=(200,200,200))
    dpg.add_input_text(tag="sys_b", hint="p.ej. 5 6")
    dpg.add_spacing(count=1)
    #agrega un botón para resolver el sistema y un campo de texto para mostrar la solución
    dpg.add_button(label="Resolver sistema", tag="btn_solve", width=200)
    dpg.add_separator()
    dpg.add_text("Solución x:", color=(200,200,200))
    dpg.add_input_text(tag="out_sys", multiline=True, readonly=True, height=100)

#se define una función para manejar los eventos de los botones
def on_click(sender, app_data):
    try: 
        #para operaciones entre matrices, se obtienen los valores de las matrices
        #se pasan a flotantes y se llama a la función correspondiente
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
            dpg.set_value("out_bin", "\n".join(str(fila) for fila in R)) #se muestra el resultado
            return
        #para operaciones sobre una matriz, se obtienen los valores de la matriz
        if sender in ("btn_det","btn_inv","btn_LU"):
            texto_A = dpg.get_value("uni_A").strip()
            A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]
            #se llama a la función correspondiente según el botón presionado
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
            else:
                L, U = factorizacion_LU(A)
                dpg.set_value("out_uni", "Ver factores L y U")
                dpg.set_value("out_L", "\n".join(" ".join(f"{v:.4g}" for v in fila) for fila in L))
                dpg.set_value("out_U", "\n".join(" ".join(f"{v:.4g}" for v in fila) for fila in U))
            return
        #para resolver sistemas lineales, se obtienen los valores de la matriz A y el vector b
        if sender == "btn_solve":
            texto_A = dpg.get_value("sys_A").strip()
            A = [[float(x) for x in fila.split()] for fila in texto_A.split(",")]
            b = [float(x) for x in dpg.get_value("sys_b").split()]
            x = resolver_sistema_gauss(A, b) #se llama a la función correspondiente
            dpg.set_value("out_sys", "  ".join(f"{xi:.6g}" for xi in x)) #se muestra la solución
            return
    #se hace un manejo de excepciones para mostrar errores en la interfaz
    except Exception as e:
        if sender in ("btn_sum","btn_sub","btn_mul"):
            dpg.set_value("out_bin", f"Error: {e}")
        elif sender in ("btn_solve"):
            dpg.set_value("out_sys", f"Error: {e}")
        else:
            dpg.set_value("out_uni", f"Error: {e}")
            dpg.set_value("out_L","")
            dpg.set_value("out_U","")
#se asigna la función de manejo de eventos a cada botón
for tag in ("btn_sum","btn_sub","btn_mul","btn_det","btn_inv","btn_LU","btn_solve"):
    dpg.set_item_callback(tag, on_click)

#se configura la ventana principal y este se muestra
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
