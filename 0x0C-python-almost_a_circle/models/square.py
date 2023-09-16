#!/usr/bin/python3
""" A method that inherates a rectangle class and creates a squre """


from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing a square instance.

        Args:
            size (int): The size of the square (width and height)
            x (int, optional): The x-coordinate of the square.
            y (int, optional): The y-coordinate of the square.
            id (int, optional): The ID for the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a formatted string representation of the Square instance.

        Returns:
            str: The formatted string.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Return a dictionary representation of the square instance.

        Returns:
            dict: A dictionary containing the attributes of a square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
