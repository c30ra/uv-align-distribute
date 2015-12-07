from . import global_def
#from global_def import *
from . import utils

from collections import defaultdict

class MakeIslands():
    
    bm = None
    uvlayer = None
    islands = []
    
    def __init__(self):
        utils.InitBMesh()
        self.islands = []
        self.bm = global_def.bm
        self.uvlayer = global_def.uvlayer
        
        self.face_to_verts = defaultdict(set)
        self.vert_to_faces = defaultdict(set)
        self.selectedIsland = set()
        self.hiddenIsland = set()
        
        for face in self.bm.faces:
            for loop in face.loops:
                vertID = loop[self.uvlayer].uv.to_tuple(5), loop.vert.index
                self.face_to_verts[face.index].add(vertID)
                self.vert_to_faces[vertID].add(face.index)
                
                if face.select:
                    if loop[self.uvlayer].select:
                        self.selectedIsland.add(face.index)
                else:
                    self.hiddenIsland.add(face.index)
         
        self.faces_left = set(self.face_to_verts.keys())
        while len(self.faces_left) > 0:
            face_id = list(self.faces_left)[0]
            self.current_island = []
            self.addToIsland(face_id)
            self.islands.append(self.current_island)
                       
    def addToIsland(self, face_id):
        if face_id in self.faces_left:
            # add the face itself
            self.current_island.append(face_id)
            self.faces_left.remove(face_id)
            # and add all faces that share uvs with this face
            verts = self.face_to_verts[face_id]
            for vert in verts:
                # print('looking at vert {}'.format(vert))
                connected_faces = self.vert_to_faces[vert]
                if connected_faces:
                    for face in connected_faces:
                        self.addToIsland(face)

    def activeIsland(self):
        for island in self.islands:
            try:
                if self.bm.faces.active.index in island:
                    return island
            except:
                return None

    def selectedIslands(self):
        _selectedIslands = []
        for island in self.islands:
            if not self.selectedIsland.isdisjoint(island):
                _selectedIslands.append(island)
        return _selectedIslands
    
    def hiddenIslands(self):
        _hiddenIslands = []
        for island in self.islands:
            if not self.hiddenIsland.isdisjoint(island):
                _hiddenIslands.append(island)
        return _hiddenIslands