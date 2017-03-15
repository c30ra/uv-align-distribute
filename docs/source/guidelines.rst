.. _guidelines:

Guidelines
==========

If you want to contribute do as follow:

Clone the github repo:

``git clone https://github.com/c30ra/uv-align-distribute.git``

Checkout the development branch

``git checkout development``

When creating a new branch prepend it with feature if you're working on a new feature
or with fix if you want bugfix/improve the code. Example:

``git branch feature_sort_islands``

``git checkout feature_sort_islands``

When you have finished with your changes, commit and send a pull request.

.. note:: All python code should be pep8 conformant

**Note:**


Pull request for new features will be accepted only if code is fully documented
(don't need to document operators) and relative test are present. You don't
need to run sphinx before and edit the resource files, but it would
be appreciated.

Instead for bug fixes and improvements to the code, your code should pass all
test before submitting a pull request.

**Running Tests**
To run test lunch test.py passing the blender executable as arg. So, if blender
is installed in a parent directory of the repo, you can do like this:

``python3 tests.py ../blender/blender``

**How to write tests:**

To write a test create a new directory under tests, and add inside this directory
the python file that execute the test and the relative blender test case.
You must to follow the other tests naming convention: files should have the same name
of the directory and must end with test.(blend for blend files, py for python files)

Version system
==============

From now on UV Align Distribute will follow this guide when versioning:

Each minor version will refer to bug fixes\improvements to code

Each major mean new features as well possible API changes: so from version 4.0 to version 3.0
compatibility in API is not guaranteed.
