import unittest

import bpy
# import the already loaded addon
from uv_align_distribute import make_islands


class TestAddon(unittest.TestCase):
    def setUp(self):
        # bpy.ops.object.mode_set(mode='EDIT')
        # bpy.context.area.type = 'IMAGE_EDITOR'
        self.make_island = make_islands.MakeIslands()

    def test_make_islands_total_islands(self):
        self.assertEqual(len(self.make_island.getIslands()), 2)

    def test_make_islands_number_of_selected_islands(self):
        self.assertEqual(len(self.make_island.selectedIslands()), 1)

    def test_make_islands_active_island(self):
        self.assertIsNotNone(self.make_island.activeIsland)
        self.assertEqual(len(self.make_island.activeIsland()), 1)


# we have to manually invoke the test runner here, as we cannot use the CLI
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
unittest.TextTestRunner(verbosity=2).run(suite)
