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

import operator

from bpy.props import FloatProperty

from . import global_def, make_islands, templates, utils


class SnapIsland(templates.OperatorTemplate):

    """Snap UV Islands by moving their vertex to the closest one"""
    bl_idname = "uv.snap_islands"
    bl_label = "Snap Islands"
    bl_options = {'REGISTER', 'UNDO'}

    threshold = FloatProperty(
        name="Threshold",
        description="Threshold for island matching",
        default=0.1,
        min=0,
        max=1,
        soft_min=0.01,
        soft_max=1,
        step=1,
        precision=2)

    def execute(self, context):
        makeIslands = make_islands.MakeIslands()
        islands = makeIslands.islands
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()
        hiddenIslands = makeIslands.hiddenIslands()

        for island in hiddenIslands:
            islands.remove(island)

        if len(selectedIslands) < 2:
            for island in selectedIslands:
                utils.snapToUnselected(islands, self.threshold, island)

        else:
            if not activeIsland:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
            # selectedIslands.remove(activeIsland)
            for island in selectedIslands:
                utils.snapIsland(activeIsland, island, self.threshold)

        utils.update()
        return{'FINISHED'}
