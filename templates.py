# #####################
# OPERATOR
# #####################
import bpy

class OperatorTemplate(bpy.types.Operator):
    bl_label = "Class Template"
    @classmethod
    def poll(cls, context):
        return not (context.scene.tool_settings.use_uv_select_sync)
