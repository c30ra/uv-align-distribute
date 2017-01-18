import mathutils


class BoundingBox():
    """BoundingBox rappresentation."""

    def __init__(self, topLeft, bottomRight):
        self.__topLeft = topLeft
        self.__bottomRight = bottomRight

    def topLeft(self):
        """ Return the top left corner. """
        return self.__topLeft

    def top(self):
        """ Return the top. """
        return self.__topLeft.y

    def topRight(self):
        """ Return the top. """
        return mathutils.Vector((self.__bottomRight.x, self.__topLeft.y))

    def right(self):
        """ Return the right Edge. """
        return self.__bottomRight.x

    def bottomRight(self):
        """Return the bottom right corner"""
        return self.__bottomRight

    def bottom(self):
        """Return the bottom edge"""
        return self.__bottomRight.y

    def bottomLeft(self):
        """Return the bottom left corner."""
        return mathutils.Vector((self.__topLeft.x, self.__bottomRight.y))

    def left(self):
        """ Return the left edge."""
        return self.__topLeft.x

    def center(self):
        """Return the bounding box center."""
        return self.__topLeft + self.__bottomRight / 2
