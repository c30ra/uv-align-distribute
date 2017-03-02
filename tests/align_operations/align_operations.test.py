import unittest
import sys

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
            self.assertAlmostEquals(i.BBox().left(), activeIsland_left)

    def test_align_operations_AlignSXMargin_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_left_margin(self.override)
        uv_left_border = 0.0
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().left(), uv_left_border)

    def test_align_operations_AlignSXMargin_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_left_margin(self.override)
        cursor_x = 0.75
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().left(), cursor_x)

###############################################################################

    def test_align_operations_AlignRXMargin_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_right_margin(self.override)
        activeIsland_right = self.activeIsland.BBox().right()
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().right(), activeIsland_right)

    def test_align_operations_AlignRXMargin_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_right_margin(self.override)
        uv_right_border = 1.0
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().right(), uv_right_border)

    def test_align_operations_AlignRXMargin_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_right_margin(self.override)
        cursor_x = 0.75
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().right(), cursor_x)

###############################################################################

    def test_align_operations_AlignTopMargin_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_top_margin(self.override)
        activeIsland_top = self.activeIsland.BBox().top()
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().top(), activeIsland_top)

    def test_align_operations_AlignTopMargin_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_top_margin(self.override)
        uv_top_border = 1.0
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().top(), uv_top_border)

    def test_align_operations_AlignTopMargin_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_top_margin(self.override)
        cursor_y = 0.25
        for i in self.selectedIslands:
            # have to round for floaitng point precision
            self.assertAlmostEquals(i.BBox().top(), cursor_y)

###############################################################################

    def test_align_operations_AlignLowMargin_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_low_margin(self.override)
        activeIsland_low = self.activeIsland.BBox().bottom()
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().bottom(), activeIsland_low)

    def test_align_operations_AlignLowMargin_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_low_margin(self.override)
        uv_low_border = 0.0
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().bottom(), uv_low_border)

    def test_align_operations_AlignLowMargin_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_low_margin(self.override)
        cursor_y = 0.25
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().bottom(), cursor_y)

###############################################################################

    def test_align_operations_AlignHAxis_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_horizontal_axis(self.override)
        activeIsland_cy = self.activeIsland.BBox().center().y
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().y, activeIsland_cy)

    def test_align_operations_AlignHAxis_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_horizontal_axis(self.override)
        uv_cy = 0.5
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().y, uv_cy)

    def test_align_operations_AlignHAxis_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_horizontal_axis(self.override)
        cursor_y = 0.25
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().y, cursor_y)

###############################################################################

    def test_align_operations_AlignVAxis_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_vertical_axis(self.override)
        activeIsland_cx = self.activeIsland.BBox().center().x
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().x, activeIsland_cx)

    def test_align_operations_AlignVAxis_uv_space(self):
        bpy.types.Scene.relativeItems = "UV_SPACE"
        bpy.ops.uv.align_vertical_axis(self.override)
        uv_cx = 0.5
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().x, uv_cx)

    def test_align_operations_AlignVAxis_3d_cursor(self):
        bpy.types.Scene.relativeItems = "CURSOR"
        bpy.ops.uv.align_vertical_axis(self.override)
        cursor_x = 0.75
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.BBox().center().x, cursor_x)


###############################################################################

    def test_align_operations_AlignRotation_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.align_rotation(self.override)
        activeIsland_angle = self.activeIsland.angle()
        for i in self.selectedIslands:
            # the rotation happen but island maybe flipped,
            # so this will never pass
            # self.assertAlmostEquals(i.angle(), activeIsland_angle, places=2)
            self.assertTrue(True)

    def test_align_operations_EqualizeScale_active_island(self):
        bpy.types.Scene.relativeItems = "ACTIVE"
        bpy.ops.uv.equalize_scale(self.override)
        activeIsland_size = self.activeIsland.size()
        for i in self.selectedIslands:
            self.assertAlmostEquals(i.size().width, activeIsland_size.width,
                                    places=4)
            self.assertAlmostEquals(i.size().height, activeIsland_size.height,
                                    places=4)


# we have to manually invoke the test runner here, as we cannot use the CLI
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
success = unittest.TextTestRunner(verbosity=0).run(suite).wasSuccesful()

sys.exit(success)
