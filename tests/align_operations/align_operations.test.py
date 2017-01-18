import unittest

import bpy

# import the already loaded addon
from uv_align_distribute import make_islands


class TestAddon(unittest.TestCase):
    def setUp(self):
        self.override = None
        for window in bpy.context.window_manager.windows:
            screen = window.screen

            for area in screen.areas:
                if area.type == "IMAGE_EDITOR":
                    self.override = {'window': window, 'screen': screen,
                                     'area': area}
                    break
        self.make_island = make_islands.MakeIslands()
        self.selectedIslands = self.make_island.selectedIslands()
        self.activeIsland = self.make_island.activeIsland()

    def tearDown(self):
        bpy.ops.ed.undo()

    def test_align_operations_AlignSXMargin_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_left_margin(self.override)
        activeIsland_left = self.activeIsland.BBox().left()
        for i in self.selectedIslands:
            self.assertEqual(i.BBox().left(), activeIsland_left)

    def test_align_operations_AlignSXMargin_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_left_margin(self.override
        uv_left_border = 0.0
        for i in self.selectedIslands:
            self.assertEqual(i.BBox().left(), uv_left_border)

    def test_align_operations_AlignSXMargin_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_left_margin(self.override)
        cursor_x = 0.75
        for i in self.selectedIslands:
            self.assertEqual(i.BBox().left(), cursor_x)


# we have to manually invoke the test runner here, as we cannot use the CLI
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
unittest.TextTestRunner(verbosity=2).run(suite)
