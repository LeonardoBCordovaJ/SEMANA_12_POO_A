class Libro:
    """
    Modelo que representa un libro dentro de la biblioteca digital.

    Decisiones de diseño:
    - El titulo y el autor se almacenan en una TUPLA porque son datos
      inmutables: un libro no cambia de titulo ni de autor una vez registrado.
    - El ISBN es el identificador unico del libro.
    - La categoria permite clasificar y buscar libros por genero o tipo.
    """

    def __init__(self, isbn: str, titulo: str, autor: str, categoria: str):
        # Tupla inmutable que almacena titulo y autor juntos
        self._info = (titulo, autor)

        # Identificador unico del libro
        self._isbn = isbn

        # Categoria o genero del libro
        self._categoria = categoria

    # ---- Getters ----

    def get_isbn(self) -> str:
        """Retorna el ISBN del libro."""
        return self._isbn

    def get_titulo(self) -> str:
        """Retorna el titulo del libro desde la tupla."""
        return self._info[0]

    def get_autor(self) -> str:
        """Retorna el autor del libro desde la tupla."""
        return self._info[1]

    def get_categoria(self) -> str:
        """Retorna la categoria del libro."""
        return self._categoria

    def get_info(self) -> tuple:
        """Retorna la tupla completa (titulo, autor)."""
        return self._info

    def __str__(self) -> str:
        return (f"ISBN: {self._isbn} | "
                f"Titulo: {self._info[0]} | "
                f"Autor: {self._info[1]} | "
                f"Categoria: {self._categoria}")