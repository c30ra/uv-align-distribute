# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2
#  of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from collections import defaultdict

# from global_def import *
from . import global_def, island, utils


class MakeIslands:

    def __init__(self):
        utils.InitBMesh()
        self.__islands = []
        self.__bm = global_def.bm
        self.__uvlayer = global_def.uvlayer

        self.__face_to_verts = defaultdict(set)
        self.__vert_to_faces = defaultdict(set)
        self.__selectedIslands = set()
        self.__hiddenFaces = set()

        for face in self.__bm.faces:
            for loop in face.loops:
                vertID = loop[self.__uvlayer].uv.to_tuple(5), loop.vert.index
                self.__face_to_verts[face.index].add(vertID)
                self.__vert_to_faces[vertID].add(face.index)

                if face.select:
                    if loop[self.__uvlayer].select:
                        self.__selectedIslands.add(face.index)
                else:
                    self.__hiddenFaces.add(face.index)

        self.__faces_left = set(self.__face_to_verts.keys())

        while len(self.__faces_left) > 0:
            face_id = list(self.__faces_left)[0]
            current_island = []
            self.__addToIsland(face_id, current_island)
            self.__islands.append(island.Island(current_island))

    def __addToIsland(self, face_id, current_island):
        if face_id in self.__faces_left:
            # add the face itself
            current_island.append(face_id)
            self.__faces_left.remove(face_id)
            # and add all faces that share uvs with this face
            verts = self.__face_to_verts[face_id]
            for vert in verts:
                connected_faces = self.__vert_to_faces[vert]
                if connected_faces:
                    for face in connected_faces:
                        self.__addToIsland(face, current_island)

    def getIslands(self):
        """ return all the uv islands """

        return self.__islands

    def activeIsland(self):
        """ return the active island(the island containing the active face) """

        for _island in self.__islands:
            try:
                if self.__bm.faces.active.index in _island:
                    return island.Island(_island)
            except:
                return None

    def selectedIslands(self):
        """ return a list of selected islands """

        selectedIslands = []
        for _island in self.__islands:
            if not self.__selectedIslands.isdisjoint(_island):
                selectedIslands.append(island.Island(_island))
        return selectedIslands

    def hiddenIslands(self):
        """ return a list of hidden islands """

        _hiddenIslands = []
        for _island in self.__islands:
            if not self.__hiddenFaces.isdisjoint(_island):
                _hiddenIslands.append(island.Island(_island))
        return _hiddenIslands
