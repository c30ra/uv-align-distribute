import mathutils

# coords in blender start from bottom-right corner as (0.0, 0.0)
# so change accordling


class BoundingBox():
    """BoundingBox rappresentation."""

    def __init__(self, lowest, highest):
        self.__topLeft = mathutils.Vector((lowest.x, highest.y))
        self.__bottomRight = mathutils.Vector((highest.x, lowest.y))

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
        return (self.__topLeft + self.__bottomRight) / 2


class Size():
    """class rappresentation of a size"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
