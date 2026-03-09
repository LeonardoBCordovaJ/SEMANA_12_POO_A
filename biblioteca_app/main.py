from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("\n======= BIBLIOTECA DIGITAL =======")
    print("--- Libros ---")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Listar todos los libros")
    print("4. Buscar libro por titulo")
    print("5. Buscar libro por autor")
    print("6. Buscar libro por categoria")
    print("--- Usuarios ---")
    print("7. Registrar usuario")
    print("8. Dar de baja usuario")
    print("--- Prestamos ---")
    print("9.  Prestar libro")
    print("10. Devolver libro")
    print("11. Ver libros prestados a un usuario")
    print("0.  Salir")
    print("===================================")


def opcion_agregar_libro(biblioteca: BibliotecaServicio):
    print("\n--- Agregar Libro ---")
    isbn = input("ISBN: ").strip()
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    categoria = input("Categoria: ").strip()
    libro = Libro(isbn, titulo, autor, categoria)
    if biblioteca.agregar_libro(libro):
        print(f"Libro '{titulo}' agregado correctamente.")
    else:
        print(f"Error: Ya existe un libro con ISBN '{isbn}'.")


def opcion_quitar_libro(biblioteca: BibliotecaServicio):
    print("\n--- Quitar Libro ---")
    isbn = input("ISBN del libro a quitar: ").strip()
    if biblioteca.quitar_libro(isbn):
        print(f"Libro con ISBN '{isbn}' eliminado del catalogo.")
    else:
        print(f"Error: No se encontro un libro con ISBN '{isbn}'.")


def opcion_listar_libros(biblioteca: BibliotecaServicio):
    print("\n--- Catalogo Completo ---")
    libros = biblioteca.listar_libros()
    if not libros:
        print("No hay libros en el catalogo.")
    else:
        print(f"{len(libros)} libro(s) disponible(s):")
        for libro in libros:
            print(" -", libro)


def opcion_buscar(biblioteca: BibliotecaServicio, tipo: str):
    print(f"\n--- Buscar por {tipo} ---")
    texto = input(f"Ingresa el {tipo}: ").strip()
    if tipo == "titulo":
        resultados = biblioteca.buscar_por_titulo(texto)
    elif tipo == "autor":
        resultados = biblioteca.buscar_por_autor(texto)
    else:
        resultados = biblioteca.buscar_por_categoria(texto)

    if not resultados:
        print("No se encontraron libros.")
    else:
        print(f"{len(resultados)} resultado(s):")
        for libro in resultados:
            print(" -", libro)


def opcion_registrar_usuario(biblioteca: BibliotecaServicio):
    print("\n--- Registrar Usuario ---")
    id_u = input("ID de usuario: ").strip()
    nombre = input("Nombre: ").strip()
    usuario = Usuario(id_u, nombre)
    if biblioteca.registrar_usuario(usuario):
        print(f"Usuario '{nombre}' registrado correctamente.")
    else:
        print(f"Error: Ya existe un usuario con ID '{id_u}'.")


def opcion_baja_usuario(biblioteca: BibliotecaServicio):
    print("\n--- Dar de Baja Usuario ---")
    id_u = input("ID del usuario: ").strip()
    if biblioteca.dar_baja_usuario(id_u):
        print(f"Usuario con ID '{id_u}' dado de baja correctamente.")
    else:
        print(f"Error: No se encontro un usuario con ID '{id_u}'.")


def opcion_prestar(biblioteca: BibliotecaServicio):
    print("\n--- Prestar Libro ---")
    id_u = input("ID del usuario: ").strip()
    isbn = input("ISBN del libro: ").strip()
    print(biblioteca.prestar_libro(id_u, isbn))


def opcion_devolver(biblioteca: BibliotecaServicio):
    print("\n--- Devolver Libro ---")
    id_u = input("ID del usuario: ").strip()
    isbn = input("ISBN del libro: ").strip()
    print(biblioteca.devolver_libro(id_u, isbn))


def opcion_ver_prestamos(biblioteca: BibliotecaServicio):
    print("\n--- Libros Prestados a Usuario ---")
    id_u = input("ID del usuario: ").strip()
    libros = biblioteca.listar_prestamos_usuario(id_u)
    if not libros:
        print("El usuario no tiene libros prestados o no existe.")
    else:
        print(f"{len(libros)} libro(s) prestado(s):")
        for libro in libros:
            print(" -", libro)


def main():
    print("Iniciando Sistema de Gestion de Biblioteca Digital...")
    biblioteca = BibliotecaServicio()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            opcion_agregar_libro(biblioteca)
        elif opcion == "2":
            opcion_quitar_libro(biblioteca)
        elif opcion == "3":
            opcion_listar_libros(biblioteca)
        elif opcion == "4":
            opcion_buscar(biblioteca, "titulo")
        elif opcion == "5":
            opcion_buscar(biblioteca, "autor")
        elif opcion == "6":
            opcion_buscar(biblioteca, "categoria")
        elif opcion == "7":
            opcion_registrar_usuario(biblioteca)
        elif opcion == "8":
            opcion_baja_usuario(biblioteca)
        elif opcion == "9":
            opcion_prestar(biblioteca)
        elif opcion == "10":
            opcion_devolver(biblioteca)
        elif opcion == "11":
            opcion_ver_prestamos(biblioteca)
        elif opcion == "0":
            print("Saliendo del sistema. Hasta luego.")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()