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
    "name": "UV Align\\Distribute",
    "author": "Rebellion (Luca Carella)",
    "version": (3, 1),
    "blender": (2, 7, 9),
    "location": "UV\\Image editor > Tool Panel, UV\\Image editor UVs > menu",
    "description": "Set of tools to help UV alignment\\distribution",
    "warning": "",
    "wiki_url": "https://github.com/c30ra/uv-align-distribute",
    "category": "UV"}


if "bpy" in locals():
    import imp
    # imp.reload(align_operations)
    # imp.reload(distribution_operations)
    # imp.reload(ui)
    # imp.reload(snap_islands)
    # imp.reload(match_islands)
    # # imp.reload(pack_islands)
    # imp.reload(global_def)
    imp.reload(operator_manager)
else:
    # from . import align_operations
    # from . import distribution_operations
    # from . import ui
    # from . import snap_islands
    # from . import match_islands
    # from . import pack_islands
    # from . import global_def
    from . import operator_manager

# NOTE: important: must be placed here and not on top as pep8 would, or it give
# import erros...
import bpy
import os

preview_collections = {}


def register():

    # importing icons
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("align_left", os.path.join(my_icons_dir, "al_left_in.png"),
               'IMAGE')
    pcoll.load("align_right", os.path.join(my_icons_dir, "al_right_in.png"),
               'IMAGE')
    pcoll.load("align_top", os.path.join(my_icons_dir, "al_top_in.png"),
               'IMAGE')
    pcoll.load("align_bottom", os.path.join(my_icons_dir, "al_bottom_in.png"),
               'IMAGE')
    pcoll.load("align_center_hor", os.path.join(my_icons_dir,
                                                "al_center_hor.png"), 'IMAGE')
    pcoll.load("align_center_ver", os.path.join(my_icons_dir,
                                                "al_center_ver.png"), 'IMAGE')

    pcoll.load("align_rotation", os.path.join(my_icons_dir,
                                              "ink_transform_rotate.png"),
               'IMAGE')

    pcoll.load("distribute_bottom", os.path.join(my_icons_dir,
                                                 "distribute_bottom.png"),
               'IMAGE')
    pcoll.load("distribute_hcentre", os.path.join(my_icons_dir,
                                                  "distribute_hcentre.png"),
               'IMAGE')
    pcoll.load("distribute_left", os.path.join(my_icons_dir,
                                               "distribute_left.png"),
               'IMAGE')
    pcoll.load("distribute_right", os.path.join(my_icons_dir,
                                                "distribute_right.png"),
               'IMAGE')
    pcoll.load("distribute_top", os.path.join(my_icons_dir,
                                              "distribute_top.png"),
               'IMAGE')
    pcoll.load("distribute_vcentre", os.path.join(my_icons_dir,
                                                  "distribute_vcentre.png"),
               'IMAGE')
    pcoll.load("distribute_hdist", os.path.join(my_icons_dir,
                                                "distribute_hdist.png"),
               'IMAGE')
    pcoll.load("distribute_vdist", os.path.join(my_icons_dir,
                                                "distribute_vdist.png"),
               'IMAGE')

    preview_collections["main"] = pcoll

    class_list = operator_manager.om.classList()
    for c in class_list:
        bpy.utils.register_class(c)


def unregister():

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

    class_list = operator_manager.om.classList()
    for c in class_list:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
