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

    """Copy and paste UV"""
    bl_idname = "uv.copy_paste_uv"
    bl_label = "Copy paste UV"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()

        if not activeIsland:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}


        activeIslandVert = set()
        for face_id in activeIsland:
            face = global_def.bm.faces[face_id]
            for vert in face.verts:
                activeIslandVert.add(vert.index)

        numOfVertex = len(activeIslandVert)

        #map each uv vert to corresponding vert for selectedIslands
        # uv_to_vert = dict((i, list()) for i in range(len(global_def.bm.verts)))
        uv_to_vert = dict((i, list()) for i in range(len(global_def.bm.verts)))
        perIslandVerts = dict((i, set()) for i in range(len(selectedIslands) - 1))
        # activeIslandUVData = dict((i, list()) for i in range(numOfVertex))
        activeIslandUVData = defaultdict(list)
        for island in selectedIslands:
            for face_id in island:
                face = global_def.bm.faces[face_id]
                for loop in face.loops:
                    index = loop.vert.index
                    if island == activeIsland:
                        activeIslandUVData[index].append(loop[global_def.uvlayer])
                    else:
                        uv_to_vert[index].append(loop[global_def.uvlayer])
                        perIslandVerts[selectedIslands.index(island) - 1].add(index)

        if len(selectedIslands) > 1:
            if(operator.contains(selectedIslands, activeIsland)):
                selectedIslands.remove(activeIsland)

        #build create a edge list
        activeIslandGraph = utils.graphFromIsland(activeIsland)
        print(activeIslandGraph.edges())
        selectedIslandsGraph = []
        for islands in selectedIslands:
            selectedIslandsGraph.append(utils.graphFromIsland(island))

        #now test for isomorphism aginst activeIsland:
        for islandGraph in selectedIslandsGraph:
            iso = networkx.isomorphism
            graphMatcher = iso.GraphMatcher(islandGraph, activeIslandGraph)
            if graphMatcher.is_isomorphic():
                vertexMapping = graphMatcher.mapping
                print(vertexMapping)
                islandIndex = selectedIslandsGraph.index(islandGraph)
                for vertIndex in perIslandVerts[islandIndex]:
                    print(vertIndex, perIslandVerts)
                    mappedVert = vertexMapping[vertIndex]
                    for uv_loop in uv_to_vert[vertIndex]:
                        for active_uv_loop in activeIslandUVData[mappedVert]:
                            uv_loop.uv = active_uv_loop.uv


        utils.update()
        return{'FINISHED'}
