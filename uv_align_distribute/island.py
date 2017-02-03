import math

import mathutils

from . import bounding_box, global_def, utils


class Island:
    def __init__(self, island):
        self.faceList = island

    def __iter__(self):
        for i in self.faceList:
            yield i

    def __len__(self):
        return len(self.faceList)

    def __str__(self):
        return str(self.faceList)

    def __repr__(self):
        return repr(self.faceList)

    def __eq__(self, other):
        return self.faceList == other

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

    def size(self):
        """ return the island size. """

        bbox = self.BBox()
        sizeX = bbox.right() - bbox.left()
        sizeY = bbox.bottom() - bbox.top()

        return bounding_box.Size(sizeX, sizeY)

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
        center = self.BBox().center()

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

        center = self.BBox().center()

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

    def snapToUnselected(self, targetIslands, threshold):
        bestMatcherList = []
        # targetIslands.remove(self)
        activeUvLayer = global_def.bm.loops.layers.uv.active

        for face_id in self.faceList:
            face = global_def.bm.faces[face_id]

            for loop in face.loops:
                selectedUVvert = loop[activeUvLayer]
                uvList = []

                for targetIsland in targetIslands:
                    for targetFace_id in targetIsland:
                        targetFace = global_def.bm.faces[targetFace_id]
                        for targetLoop in targetFace.loops:
                            # take the a reference vert
                            targetUvVert = targetLoop[activeUvLayer].uv
                            # get a selected vert and calc it's distance from
                            # the ref
                            # add it to uvList
                            dist = round(
                                utils.vectorDistance(selectedUVvert.uv,
                                                     targetUvVert), 10)
                            uvList.append((dist, targetLoop[activeUvLayer]))

                # for every vert in uvList take the ones with the shortest
                # distnace from ref
                minDist = uvList[0][0]
                bestMatcher = 0

                # 1st pass get lower dist
                for bestDist in uvList:
                    if bestDist[0] <= minDist:
                        minDist = bestDist[0]

                # 2nd pass get the only ones with a match
                for bestVert in uvList:
                    if bestVert[0] <= minDist:
                        bestMatcherList.append((bestVert[0], selectedUVvert,
                                                bestVert[1]))

        for bestMatcher in bestMatcherList:
            if bestMatcher[0] <= threshold:
                bestMatcher[1].uv = bestMatcher[2].uv

    def isIsomorphic(self, other):
        """test for isomorphism"""
        pass
