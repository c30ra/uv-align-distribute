import unittest
import sys
# import the already loaded addon
#
try:
    import uv_align_distribute

    class TestAddon(unittest.TestCase):
        def test_addon_enabled(self):
            # test if addon got loaded correctly
            # every addon must provide the "bl_info" dict
            self.assertIsNotNone(uv_align_distribute.bl_info)


    # we have to manually invoke the test runner here, as we cannot use the CLI
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
    unittest.TextTestRunner(verbosity=0).run(suite)

except ImportError:
    sys.exit(1)
