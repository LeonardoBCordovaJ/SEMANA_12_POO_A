from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Servicio que gestiona toda la logica del negocio de la biblioteca digital.

    Decisiones de diseño sobre colecciones:
    - DICCIONARIO (_libros_disponibles): clave = ISBN, valor = Libro.
      Permite busqueda y acceso rapido en O(1) por ISBN.
    - CONJUNTO (_ids_usuarios): almacena IDs unicos de usuarios registrados.
      Garantiza que no haya IDs duplicados y permite verificacion rapida.
    - DICCIONARIO (_usuarios): clave = ID, valor = Usuario.
      Permite acceso rapido al objeto Usuario por su ID.
    """

    def __init__(self):
        # Diccionario de libros disponibles: clave = ISBN, valor = Libro
        self._libros_disponibles: dict[str, Libro] = {}

        # Diccionario de usuarios registrados: clave = ID, valor = Usuario
        self._usuarios: dict[str, Usuario] = {}

        # Conjunto de IDs de usuarios para garantizar unicidad
        self._ids_usuarios: set[str] = set()

    # -------------------------------------------------------
    # GESTION DE LIBROS
    # -------------------------------------------------------

    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un libro al catalogo de la biblioteca.
        Retorna False si el ISBN ya existe.
        """
        if libro.get_isbn() in self._libros_disponibles:
            return False
        self._libros_disponibles[libro.get_isbn()] = libro
        return True

    def quitar_libro(self, isbn: str) -> bool:
        """
        Quita un libro del catalogo por ISBN.
        Retorna False si no se encuentra.
        """
        if isbn not in self._libros_disponibles:
            return False
        del self._libros_disponibles[isbn]
        return True

    def buscar_por_titulo(self, texto: str) -> list[Libro]:
        """Busca libros por coincidencia parcial en el titulo."""
        texto = texto.lower()
        return [l for l in self._libros_disponibles.values()
                if texto in l.get_titulo().lower()]

    def buscar_por_autor(self, texto: str) -> list[Libro]:
        """Busca libros por coincidencia parcial en el autor."""
        texto = texto.lower()
        return [l for l in self._libros_disponibles.values()
                if texto in l.get_autor().lower()]

    def buscar_por_categoria(self, texto: str) -> list[Libro]:
        """Busca libros por coincidencia parcial en la categoria."""
        texto = texto.lower()
        return [l for l in self._libros_disponibles.values()
                if texto in l.get_categoria().lower()]

    def listar_libros(self) -> list[Libro]:
        """Retorna todos los libros disponibles en el catalogo."""
        return list(self._libros_disponibles.values())

    # -------------------------------------------------------
    # GESTION DE USUARIOS
    # -------------------------------------------------------

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un nuevo usuario en el sistema.
        Usa el conjunto para verificar que el ID sea unico.
        Retorna False si el ID ya existe.
        """
        if usuario.get_id() in self._ids_usuarios:
            return False
        self._ids_usuarios.add(usuario.get_id())
        self._usuarios[usuario.get_id()] = usuario
        return True

    def dar_baja_usuario(self, id_usuario: str) -> bool:
        """
        Da de baja a un usuario por ID.
        Retorna False si no se encuentra.
        """
        if id_usuario not in self._ids_usuarios:
            return False
        self._ids_usuarios.discard(id_usuario)
        del self._usuarios[id_usuario]
        return True

    # -------------------------------------------------------
    # GESTION DE PRESTAMOS Y DEVOLUCIONES
    # -------------------------------------------------------

    def prestar_libro(self, id_usuario: str, isbn: str) -> str:
        """
        Presta un libro a un usuario.
        Retorna un mensaje indicando el resultado de la operacion.
        """
        if id_usuario not in self._usuarios:
            return "Error: Usuario no encontrado."

        if isbn not in self._libros_disponibles:
            return "Error: Libro no disponible en el catalogo."

        usuario = self._usuarios[id_usuario]

        if usuario.tiene_libro(isbn):
            return "Error: El usuario ya tiene prestado ese libro."

        libro = self._libros_disponibles[isbn]
        usuario.agregar_libro_prestado(libro)
        del self._libros_disponibles[isbn]
        return f"Libro '{libro.get_titulo()}' prestado a '{usuario.get_nombre()}' correctamente."

    def devolver_libro(self, id_usuario: str, isbn: str) -> str:
        """
        Registra la devolucion de un libro por parte de un usuario.
        Retorna un mensaje indicando el resultado de la operacion.
        """
        if id_usuario not in self._usuarios:
            return "Error: Usuario no encontrado."

        usuario = self._usuarios[id_usuario]

        if not usuario.tiene_libro(isbn):
            return "Error: El usuario no tiene prestado ese libro."

        libro = None
        for l in usuario.get_libros_prestados():
            if l.get_isbn() == isbn:
                libro = l
                break

        usuario.quitar_libro_prestado(isbn)
        self._libros_disponibles[isbn] = libro
        return f"Libro '{libro.get_titulo()}' devuelto correctamente al catalogo."

    def listar_prestamos_usuario(self, id_usuario: str) -> list:
        """
        Retorna la lista de libros prestados a un usuario.
        """
        if id_usuario not in self._usuarios:
            return []
        return self._usuarios[id_usuario].get_libros_prestados()