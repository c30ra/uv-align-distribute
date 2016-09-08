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

from bpy.props import BoolProperty

from . import templates
from . import make_island
from . import utils

import mathutils
############################
# DISTRIBUTION
############################


class DistributeLEdgesH(templates.OperatorTemplate):

    """Distribute left edges equidistantly horizontally"""
    bl_idname = "uv.distribute_ledges_horizontally"
    bl_label = "Distribute Left Edges Horizontally"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortX(selectedIslands)
        uvFirstX = utils.BBox(islandSpatialSort[0][1])[0].x
        uvLastX = utils.BBox(islandSpatialSort[-1][1])[0].x

        distX = uvLastX - uvFirstX

        deltaDist = distX / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirstX + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((pos - utils.BBox(island[1])[0].x, 0.0))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class DistributeCentersH(templates.OperatorTemplate):

    """Distribute centers equidistantly horizontally"""
    bl_idname = "uv.distribute_center_horizontally"
    bl_label = "Distribute Centers Horizontally"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortX(selectedIslands)
        uvFirstX = min(islandSpatialSort)
        uvLastX = max(islandSpatialSort)

        distX = uvLastX[0] - uvFirstX[0]

        deltaDist = distX / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirstX[0] + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((pos - utils.BBoxCenter(island[1]).x, 0.0))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class DistributeREdgesH(templates.OperatorTemplate):

    """Distribute right edges equidistantly horizontally"""
    bl_idname = "uv.distribute_redges_horizontally"
    bl_label = "Distribute Right Edges Horizontally"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortX(selectedIslands)
        uvFirstX = utils.BBox(islandSpatialSort[0][1])[1].x
        uvLastX = utils.BBox(islandSpatialSort[-1][1])[1].x

        distX = uvLastX - uvFirstX

        deltaDist = distX / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirstX + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((pos - utils.BBox(island[1])[1].x, 0.0))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class DistributeTEdgesV(templates.OperatorTemplate):

    """Distribute top edges equidistantly vertically"""
    bl_idname = "uv.distribute_tedges_vertically"
    bl_label = "Distribute Top Edges Vertically"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortY(selectedIslands)
        uvFirstX = utils.BBox(islandSpatialSort[0][1])[1].y
        uvLastX = utils.BBox(islandSpatialSort[-1][1])[1].y

        distX = uvLastX - uvFirstX

        deltaDist = distX / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirstX + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((0.0, pos - utils.BBox(island[1])[1].y))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class DistributeCentersV(templates.OperatorTemplate):

    """Distribute centers equidistantly vertically"""
    bl_idname = "uv.distribute_center_vertically"
    bl_label = "Distribute Centers Vertically"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortY(selectedIslands)
        uvFirst = utils.BBoxCenter(islandSpatialSort[0][1]).y
        uvLast = utils.BBoxCenter(islandSpatialSort[-1][1]).y

        dist = uvLast - uvFirst

        deltaDist = dist / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirst + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((0.0, pos - utils.BBoxCenter(island[1]).y))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class DistributeBEdgesV(templates.OperatorTemplate):

    """Distribute bottom edges equidistantly vertically"""
    bl_idname = "uv.distribute_bedges_vertically"
    bl_label = "Distribute Bottom Edges Vertically"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortY(selectedIslands)
        uvFirst = utils.BBox(islandSpatialSort[0][1])[0].y
        uvLast = utils.BBox(islandSpatialSort[-1][1])[0].y

        dist = uvLast - uvFirst

        deltaDist = dist / (len(selectedIslands) - 1)

        islandSpatialSort.pop(0)
        islandSpatialSort.pop(-1)

        pos = uvFirst + deltaDist

        for island in islandSpatialSort:
            vec = mathutils.Vector((0.0, pos - utils.BBox(island[1])[0].y))
            pos += deltaDist
            utils.moveIslands(vec, island[1])
        utils.update()
        return {"FINISHED"}


class RemoveOverlaps(templates.OperatorTemplate):

    """Remove overlaps on islands"""
    bl_idname = "uv.remove_overlaps"
    bl_label = "Remove Overlaps"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        islands = makeIslands.getIslands()

        islandEdges = []
        uvData = []
        for island in islands:
            edges = []

            for face_id in island:
                face = bm.faces[face_id]

                for loop in face.loops:
                    edgeVert1 = loop.edge.verts[0].index
                    edgeVert2 = loop.edge.verts[1].index
                    edges.append((edgeVert1, edgeVert2))
                    uv = loop[bm.loops.layers.uv.active].uv
                    vertIndex = loop.vert.index
                    uvData.append((vertIndex, uv))
            islandEdges.append(edges)
        return {"FINISHED"}


class EqualizeHGap(templates.OperatorTemplate):

    """Equalize horizontal gap between island"""
    bl_idname = "uv.equalize_horizontal_gap"
    bl_label = "Equalize Horizontal Gap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortX(selectedIslands)

        averageDist = utils.averageIslandDist(islandSpatialSort)

        for i in range(len(islandSpatialSort)):
            if islandSpatialSort.index(islandSpatialSort[i + 1]) == \
                    islandSpatialSort.index(islandSpatialSort[-1]):
                break
            elem1 = utils.BBox(islandSpatialSort[i][1])[1].x
            elem2 = utils.BBox(islandSpatialSort[i + 1][1])[0].x

            dist = elem2 - elem1
            increment = averageDist.x - dist

            vec = mathutils.Vector((increment, 0.0))
            utils.moveIslands(vec, islandSpatialSort[i + 1][1])
        utils.update()
        return {"FINISHED"}


class EqualizeVGap(templates.OperatorTemplate):

    """Equalize vertical gap between island"""
    bl_idname = "uv.equalize_vertical_gap"
    bl_label = "Equalize Vertical Gap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        if len(selectedIslands) < 3:
            return {'CANCELLED'}

        islandSpatialSort = utils.IslandSpatialSortY(selectedIslands)

        averageDist = utils.averageIslandDist(islandSpatialSort)

        for i in range(len(islandSpatialSort)):
            if islandSpatialSort.index(islandSpatialSort[i + 1]) ==\
                    islandSpatialSort.index(islandSpatialSort[-1]):
                break
            elem1 = utils.BBox(islandSpatialSort[i][1])[1].y
            elem2 = utils.BBox(islandSpatialSort[i + 1][1])[0].y

            dist = elem2 - elem1

            increment = averageDist.y - dist

            vec = mathutils.Vector((0.0, increment))

            utils.moveIslands(vec, islandSpatialSort[i + 1][1])
        utils.update()
        return {"FINISHED"}


class EqualizeScale(templates.OperatorTemplate):

    """Equalize the islands scale to the active one"""
    bl_idname = "uv.equalize_scale"
    bl_label = "Equalize Scale"
    bl_options = {'REGISTER', 'UNDO'}

    keepProportions = BoolProperty(
        name="Keep Proportions",
        description="Mantain proportions during scaling",
        default=False)

    useYaxis = BoolProperty(
        name="Use Y axis",
        description="Use y axis as scale reference, default is x",
        default=False)

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()

        if not activeIsland:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}

        activeSize = utils.islandSize(activeIsland)
        selectedIslands.remove(activeIsland)

        for island in selectedIslands:
            size = utils.islandSize(island)
            scaleX = activeSize[0] / size[0]
            scaleY = activeSize[1] / size[1]

            if self.keepProportions:
                if self.useYaxis:
                    scaleX = scaleY
                else:
                    scaleY = scaleX

            utils.scaleIsland(island, scaleX, scaleY)

        utils.update()
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "keepProportions")
        if self.keepProportions:
            layout.prop(self, "useYaxis")
