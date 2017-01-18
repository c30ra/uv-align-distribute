import math

import bmesh
import bpy
import mathutils

from . import bounding_box, global_def


class Island:
    def __init__(self, island):
        self.faceList = island

    def __iter__(self):
        for i in self.faceList:
            yield i

    def __len__(self):
        return len(self.faceList)

# properties
    def BBox(self):
        """ return the bounding box of the island. """

        minX = minY = 1000
        maxX = maxY = -1000
        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                u, v = loop[global_def.uvlayer].uv
                minX = min(u, minX)
                minY = min(v, minY)
                maxX = max(u, maxX)
                maxY = max(v, maxY)

        return bounding_box.BoundingBox(mathutils.Vector((minX, minY)),
                                        mathutils.Vector((maxX, maxY)))

    def angle(self):
        """ return the island angle. """

        uvList = []
        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                uv = loop[global_def.bm.loops.layers.uv.active].uv
                uvList.append(uv)

        angle = math.degrees(mathutils.geometry.box_fit_2d(uvList))
        return angle

    def islandSize(self):
        """ return the island size. """

        bbox = bounding_box.BBox()
        sizeX = bbox.bottomRight.x - bbox.topLeft.x
        sizeY = bbox.bottomRight.y - bbox.topLeft.y

        return sizeX, sizeY

# Transformation
    def move(self, vector):
        """ move the island by vector. """

        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                loop[global_def.bm.loops.layers.uv.active].uv += vector

    def rotate(self, angle):
        """ rotate the island on it's center by 'angle(degree)'. """

        rad = math.radians(angle)
        center = bounding_box.BBox().center()

        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                uv_act = global_def.bm.loops.layers.uv.active
                x, y = loop[uv_act].uv
                xt = x - center.x
                yt = y - center.y
                xr = (xt * math.cos(rad)) - (yt * math.sin(rad))
                yr = (xt * math.sin(rad)) + (yt * math.cos(rad))
                # loop[global_def.bm.loops.layers.uv.active].uv = trans
                loop[global_def.bm.loops.layers.uv.active].uv.x = xr + center.x
                loop[global_def.bm.loops.layers.uv.active].uv.y = yr + center.y

    def scale(self, scaleX, scaleY):
        """ scale the island by 'scaleX, scaleY'. """

        center = bounding_box.BBox().center()

        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                x = loop[global_def.bm.loops.layers.uv.active].uv.x
                y = loop[global_def.bm.loops.layers.uv.active].uv.y
                xt = x - center.x
                yt = y - center.y
                xs = xt * scaleX
                ys = yt * scaleY
                loop[global_def.bm.loops.layers.uv.active].uv.x = xs + center.x
                loop[global_def.bm.loops.layers.uv.active].uv.y = ys + center.y
