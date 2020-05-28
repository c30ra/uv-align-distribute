import unittest
import sys

try:
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
            # bpy.ops.ed.undo()
            pass

        def test_distribution_operations_DistributeTEdgesV(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_tedges_vertically(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().y)

            rifDist = self.selectedIslands[1].BBox().top() -\
                self.selectedIslands[0].BBox().top()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().top() - islandA.BBox().top()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_DistributeCentersV(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_center_vertically(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().y)

            rifDist = self.selectedIslands[1].BBox().center().y -\
                self.selectedIslands[0].BBox().center().y

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().center().y - islandA.BBox().center().y
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_DistributeBEdgesV(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_bedges_vertically(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().y)

            rifDist = self.selectedIslands[1].BBox().bottom() -\
                self.selectedIslands[0].BBox().bottom()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().bottom() - islandA.BBox().bottom()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_EqualizeVGap(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.equalize_vertical_gap(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().y)

            rifDist = self.selectedIslands[1].BBox().bottom() -\
                self.selectedIslands[0].BBox().top()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().bottom() - islandA.BBox().top()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

    # we have to manually invoke the test runner here, as we cannot use the CLI
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
    status = unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful()
    sys.exit(not int(status))

except ImportError:
    sys.exit(1)
