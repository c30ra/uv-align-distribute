
import bpy


##############
#   UI
##############
class IMAGE_PT_align_distribute(bpy.types.Panel):
    bl_label = "Align\Distribute"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and \
            not (context.tool_settings.use_uv_sculpt
                 or context.scene.tool_settings.use_uv_select_sync)

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        layout.prop(scn, "relativeItems")
        layout.prop(scn, "selectionAsGroup")

        layout.separator()
        layout.label(text="Align:")

        box = layout.box()
        row = box.row(True)
        row.operator("uv.align_left_margin", "Left")
        row.operator("uv.align_vertical_axis", "VAxis")
        row.operator("uv.align_right_margin", "Right")
        row = box.row(True)
        row.operator("uv.align_top_margin", "Top")
        row.operator("uv.align_horizontal_axis", "HAxis")
        row.operator("uv.align_low_margin", "Low")

        row = layout.row()
        row.operator("uv.align_rotation", "Rotation")
        row.operator("uv.equalize_scale", "Eq. Scale")

        layout.separator()
        # Another Panel??
        layout.label(text="Distribute:")

        box = layout.box()

        row = box.row(True)
        row.operator("uv.distribute_ledges_horizontally", "LEdges")

        row.operator("uv.distribute_center_horizontally",
                     "HCenters")

        row.operator("uv.distribute_redges_horizontally",
                     "RCenters")

        row = box.row(True)
        row.operator("uv.distribute_tedges_vertically", "TEdges")
        row.operator("uv.distribute_center_vertically", "VCenters")
        row.operator("uv.distribute_bedges_vertically", "BEdges")

        row = layout.row(True)
        row.operator("uv.equalize_horizontal_gap", "Eq. HGap")
        row.operator("uv.equalize_vertical_gap", "Eq. VGap")

        #wip
        #row = layout.row(True)
        #row.operator("uv.remove_overlaps", "Remove Overlaps")

        #TODO organize these
        layout.separator()
        layout.label("Others:")
        row = layout.row()
        layout.operator("uv.snap_islands")
        row = layout.row()
        layout.operator("uv.match_islands")
