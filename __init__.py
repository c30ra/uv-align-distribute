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

bl_info = {
    "name": "UV Align/Distribute",
    "author": "Rebellion (Luca Carella)",
    "version": (2, 1),
    "blender": (2, 7, 7),
    "location": "UV/Image editor > Tool Panel, UV/Image editor UVs > menu",
    "description": "Set of tools to help UV alignment\distribution",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/UV/UV_Align_Distribution",
    "category": "UV"}

if "bpy" in locals():
    import imp
    imp.reload(align_operations)
    imp.reload(distribution_operations)
    imp.reload(ui)
    imp.reload(snap_islands)
    imp.reload(match_islands)

else:
    from . import align_operations
    from . import distribution_operations
    from . import ui
    from . import snap_islands
    from . import match_islands

import bpy
#from . import debug
#for d in sys.path:
    #print(d)


# classes = (
#     IMAGE_PT_align_distribute,
#     AlignSXMargin,
#     AlignRxMargin,
#     AlignVAxis,
#     AlignTopMargin,
#     AlignLowMargin,
#     AlignHAxis,
#     AlignRotation,
#     DistributeLEdgesH,
#     DistributeCentersH,
#     DistributeREdgesH,
#     DistributeTEdgesV,
#     DistributeCentersV,
#     DistributeBEdgesV,
#     #RemoveOverlaps,
#     EqualizeHGap,
#     EqualizeVGap,
#     EqualizeScale,
#     SnapIsland,
#     MatchIsland)


def register():
    #for item in classes:
        bpy.utils.register_module(__name__)
    # bpy.utils.register_manual_map(add_object_manual_map)
    # bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
    #for item in classes:
        bpy.utils.unregister_module(__name__)
    # bpy.utils.unregister_manual_map(add_object_manual_map)
    # bpy.types.INFO_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()
