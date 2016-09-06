from bpy.props import FloatProperty
from . import global_def
from . import templates
from . import utils
from . import make_island

import operator

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
        makeIslands = make_island.MakeIslands()
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
            #selectedIslands.remove(activeIsland)
            for island in selectedIslands:
                utils.snapIsland(activeIsland, self.threshold, island)

        utils.update()
        return{'FINISHED'}
