import unittest
import sys

try:
    import mathutils

    # import the already loaded addon
    from uv_align_distribute import make_islands

    class TestAddon(unittest.TestCase):
        def setUp(self):
            self.make_island = make_islands.MakeIslands()
            self.selectedIslands = self.make_island.selectedIslands()
            self.activeIsland = self.make_island.activeIsland()

        def test_Rectangle_FromIsland(self):
            self.assertEqual(self.activeIsland.BBox().topLeft(),
                             mathutils.Vector((0.0, 1.0)))

    # we have to manually invoke the test runner here, as we cannot use the CLI
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
    unittest.TextTestRunner(verbosity=0).run(suite)

except ImportError:
    sys.exit(1)
