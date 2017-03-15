import unittest

import bpy
# import the already loaded addon
from uv_align_distribute import make_islands


class MyTest(unittest.TestCase):
    def setUp(self):
        # setup logic

    def tearDown(self):
        # teardown logic
        #
    def test_my_features(self):
        # test logic here

# this lines must be present at hte end of each test
# we have to manually invoke the test runner here, as we cannot use the CLI
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
unittest.TextTestRunner(verbosity=0).run(suite)
