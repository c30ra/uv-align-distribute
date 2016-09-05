# Globals:
import bpy
from bpy.props import EnumProperty, BoolProperty


bpy.types.Scene.relativeItems = EnumProperty(
    items=[
        ('UV_SPACE', 'Uv Space', 'Align to UV space'),
        ('ACTIVE', 'Active Face', 'Align to active face\island'),
        ('CURSOR', 'Cursor', 'Align to cursor')],
    name="Relative to")

bpy.types.Scene.selectionAsGroup = BoolProperty(
    name="Selection as group",
    description="Treat selection as group",
    default=False)

bm = None
uvlayer = None

preview_collections = {}
