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

    def test_SnapIslands(self):
    	




# we have to manually invoke the test runner here, as we cannot use the CLI
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
unittest.TextTestRunner(verbosity=2).run(suite)
