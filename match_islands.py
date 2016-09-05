from . import templates
from . import make_island
from . import utils
from . import global_def

from collections import defaultdict

import operator
import mathutils
import networkx


#####################
#COPY PASTE
#####################

class CopyPasteUV(templates.OperatorTemplate):

    """Match UV Island by moving their vertex"""
    bl_idname = "uv.match_islands"
    bl_label = "Match Islands"
    bl_options = {'REGISTER', 'UNDO'}

    def graphFromIsland(self, island):

        vertexList = set()

        for face_id in island:
            face = global_def.bm.faces[face_id]
            for vert in face.verts:
                vertexList.add(vert)

        vertexList = sorted(vertexList, key=lambda data: data.index)
        numOfVertex = len(vertexList)

        edgeVertex = set()
        for face_id in island:
            face = global_def.bm.faces[face_id]
            for edges in face.edges:
                edgeVert = (edges.verts[0].index, edges.verts[1].index)
                edgeVertex.add(tuple(sorted(edgeVert, key=lambda data: data)))

        g = networkx.Graph(tuple(edgeVertex))

        return g
    def execute(self, context):

        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()

        if not activeIsland:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}

        if len(selectedIslands) > 1:
            if(operator.contains(selectedIslands, activeIsland)):
                selectedIslands.remove(activeIsland)

        activeIslandVert = set()
        for face_id in activeIsland:
            face = global_def.bm.faces[face_id]
            for vert in face.verts:
                activeIslandVert.add(vert.index)

        numOfVertex = len(activeIslandVert)

        #map each uv vert to corresponding vert for selectedIslands
        # uv_to_vert = dict((i, list()) for i in range(len(global_def.bm.verts)))
        uv_to_vert = dict((i, list()) for i in range(len(global_def.bm.verts)))
        perIslandVerts = dict((i, set()) for i in range(len(selectedIslands)))
        # activeIslandUVData = dict((i, list()) for i in range(numOfVertex))
        for island in selectedIslands:
            for face_id in island:
                face = global_def.bm.faces[face_id]
                for loop in face.loops:
                    index = loop.vert.index
                    uv_to_vert[index].append(loop[global_def.uvlayer])
                    perIslandVerts[selectedIslands.index(island)].add(index)


        activeIslandUVData = defaultdict(list)
        for face_id in activeIsland:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                index = loop.vert.index
                activeIslandUVData[index].append(loop[global_def.uvlayer])

        print(perIslandVerts)
        print(activeIslandUVData)

        #build create a edge list
        activeIslandGraph = self.graphFromIsland(activeIsland)
        selectedIslandsGraph = []
        for islands in selectedIslands:
            selectedIslandsGraph.append(self.graphFromIsland(island))

        #now test for isomorphism aginst activeIsland:
        for islandGraph in selectedIslandsGraph:
            iso = networkx.isomorphism
            graphMatcher = iso.GraphMatcher(islandGraph, activeIslandGraph)
            if graphMatcher.is_isomorphic():
                vertexMapping = graphMatcher.mapping
                islandIndex = selectedIslandsGraph.index(islandGraph)
                for vertIndex in perIslandVerts[islandIndex]:
                    mappedVert = vertexMapping[vertIndex]
                    print(vertIndex, mappedVert)

                    for uv_loop in uv_to_vert[vertIndex]:
                        for active_uv_loop in activeIslandUVData[mappedVert]:
                            uv_loop.uv = active_uv_loop.uv


        utils.update()
        return{'FINISHED'}
