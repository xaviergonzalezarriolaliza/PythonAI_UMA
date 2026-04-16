class Libro:
    iva = 10.0  # Porcentaje de IVA compartido por todos los libros

    def __init__(self, autor, titulo, precio_base):
        self.__autor = autor
        self.__titulo = titulo
        self.__precio_base = precio_base

    @property
    def autor(self):
        return self.__autor

    @property
    def titulo(self):
        return self.__titulo

    @property
    def precio_base(self):
        return self.__precio_base

    def precio_final(self):
        return self.__precio_base + self.__precio_base * self.iva / 100

    def __str__(self):
        pf = self.precio_final()
        return f"({self.__autor}; {self.__titulo}; {self.__precio_base:.2f}; {self.iva:.1f}%; {pf:.2f})"

    def __eq__(self, other):
        if isinstance(other, Libro):
            return (self.__autor.lower() == other.__autor.lower() and
                    self.__titulo.lower() == other.__titulo.lower())
        return False