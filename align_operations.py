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

from . import templates
from . import make_island
from . import utils

import mathutils
#####################
# ALIGN
#####################


class AlignSXMargin(templates.OperatorTemplate):

    """Align left margin"""
    bl_idname = "uv.align_left_margin"
    bl_label = "Align left margin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}

        if context.scene.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement[0].x - groupBox[0].x,
                                           0.0))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (targetElement[0].x - utils.BBox(island)[0].x, 0.0))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


class AlignRxMargin(templates.OperatorTemplate):

    """Align right margin"""
    bl_idname = "uv.align_right_margin"
    bl_label = "Align right margin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}

        if context.scene.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement[1].x - groupBox[1].x,
                                           0.0))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (targetElement[1].x - utils.BBox(island)[1].x, 0.0))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


class AlignVAxis(templates.OperatorTemplate):

    """Align vertical axis"""
    bl_idname = "uv.align_vertical_axis"
    bl_label = "Align vertical axis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}
        targetCenter = (targetElement[0] + targetElement[1]) / 2
        if context.scene.selectionAsGroup:
            groupBoxCenter = utils.GBBoxCenter(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (targetCenter.x - groupBoxCenter.x, 0.0))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (targetCenter.x - utils.BBoxCenter(island).x, 0.0))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


##################################################
class AlignTopMargin(templates.OperatorTemplate):

    """Align top margin"""
    bl_idname = "uv.align_top_margin"
    bl_label = "Align top margin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}
        if context.scene.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetElement[1].y - groupBox[1].y))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetElement[1].y - utils.BBox(island)[1].y))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


class AlignLowMargin(templates.OperatorTemplate):

    """Align low margin"""
    bl_idname = "uv.align_low_margin"
    bl_label = "Align low margin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}
        if context.scene.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetElement[0].y - groupBox[0].y))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetElement[0].y - utils.BBox(island)[0].y))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


class AlignHAxis(templates.OperatorTemplate):

    """Align horizontal axis"""
    bl_idname = "uv.align_horizontal_axis"
    bl_label = "Align horizontal axis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = utils.getTargetPoint(context, makeIslands)
        if not targetElement:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}
        targetCenter = (targetElement[0] + targetElement[1]) / 2

        if context.scene.selectionAsGroup:
            groupBoxCenter = utils.GBBoxCenter(selectedIslands)
            if context.scene.relativeItems == 'ACTIVE':
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetCenter.y - groupBoxCenter.y))
                utils.moveIslands(vector, island)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetCenter.y - utils.BBoxCenter(island).y))
                utils.moveIslands(vector, island)

        utils.update()
        return {'FINISHED'}


#########################################
class AlignRotation(templates.OperatorTemplate):

    """Align island rotation """
    bl_idname = "uv.align_rotation"
    bl_label = "Align island rotation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()
        if not activeIsland:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}
        activeAngle = utils.islandAngle(activeIsland)

        for island in selectedIslands:
            uvAngle = utils.islandAngle(island)
            deltaAngle = activeAngle - uvAngle
            deltaAngle = round(-deltaAngle, 5)
            utils.rotateIsland(island, deltaAngle)

        utils.update()
        return {'FINISHED'}
