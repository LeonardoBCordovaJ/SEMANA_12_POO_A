from modelos.libro import Libro


class Usuario:
    """
    Modelo que representa un usuario registrado en la biblioteca digital.

    Decisiones de diseño:
    - Los libros prestados se almacenan en una LISTA porque es una
      coleccion ordenada y mutable: los libros se agregan y se quitan
      conforme el usuario realiza prestamos y devoluciones.
    - El ID de usuario es unico y no cambia una vez registrado.
    """

    def __init__(self, id_usuario: str, nombre: str):
        # Identificador unico del usuario
        self._id = id_usuario

        # Nombre del usuario
        self._nombre = nombre

        # Lista de objetos Libro actualmente prestados al usuario
        self._libros_prestados: list[Libro] = []

    # ---- Getters ----

    def get_id(self) -> str:
        """Retorna el ID del usuario."""
        return self._id

    def get_nombre(self) -> str:
        """Retorna el nombre del usuario."""
        return self._nombre

    def get_libros_prestados(self) -> list:
        """Retorna la lista de libros actualmente prestados."""
        return self._libros_prestados

    # ---- Metodos de gestion de prestamos ----

    def agregar_libro_prestado(self, libro: Libro) -> None:
        """Agrega un libro a la lista de prestamos del usuario."""
        self._libros_prestados.append(libro)

    def quitar_libro_prestado(self, isbn: str) -> bool:
        """
        Quita un libro de la lista de prestamos por ISBN.
        Retorna True si se encontro y quito, False si no estaba.
        """
        for libro in self._libros_prestados:
            if libro.get_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return True
        return False

    def tiene_libro(self, isbn: str) -> bool:
        """Verifica si el usuario tiene prestado un libro por ISBN."""
        return any(libro.get_isbn() == isbn for libro in self._libros_prestados)

    def __str__(self) -> str:
        return (f"ID: {self._id} | "
                f"Nombre: {self._nombre} | "
                f"Libros prestados: {len(self._libros_prestados)}")