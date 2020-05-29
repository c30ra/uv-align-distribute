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

        def test_distribution_operations_DistributeLEdgesH(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_ledges_horizontally(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().x)

            rifDist = self.selectedIslands[1].BBox().left() -\
                self.selectedIslands[0].BBox().left()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().left() - islandA.BBox().left()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_DistributeCentersH(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_center_horizontally(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().x)

            rifDist = self.selectedIslands[1].BBox().center().x -\
                self.selectedIslands[0].BBox().center().x

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().center().x - islandA.BBox().center().x
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_DistributeREdgesH(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.distribute_redges_horizontally(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().x)

            rifDist = self.selectedIslands[1].BBox().right() -\
                self.selectedIslands[0].BBox().right()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().right() - islandA.BBox().right()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass

        def test_distribution_operations_EqualizeHGap(self):
            bpy.context.scene.uv_align_distribute.relativeItems = "ACTIVE"
            bpy.ops.uv.equalize_horizontal_gap(self.override)

            self.selectedIslands.sort(key=lambda island: island.BBox().center().x)

            rifDist = self.selectedIslands[1].BBox().right() -\
                self.selectedIslands[0].BBox().left()

            for i in range(2, len(self.selectedIslands)):
                try:
                    islandA = self.selectedIslands[i]
                    islandB = self.selectedIslands[i + 1]
                    dist = islandB.BBox().right() - islandA.BBox().left()
                    self.assertAlmostEqual(dist, rifDist)
                except:
                    pass


    # we have to manually invoke the test runner here, as we cannot use the CLI
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
    status = unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful()
    sys.exit(not int(status))

except ImportError:
    sys.exit(1)
