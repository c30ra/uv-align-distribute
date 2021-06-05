import bpy
import sys
import os

def ensure_site_packages(packages):
    """ `packages`: list of tuples (<import name>, <pip name>) """

    if not packages:
        return

    import site
    import importlib
    import importlib.util

    user_site_packages = site.getusersitepackages()
    os.makedirs(user_site_packages, exist_ok = True)
    sys.path.append(user_site_packages)

    modules_to_install = [module[1] for module in packages if not importlib.util.find_spec(module[0])]

    if modules_to_install:
        import subprocess

        if bpy.app.version < (2,91,0):
            python_binary = bpy.app.binary_path_python
        else:
            python_binary = sys.executable

        subprocess.run([python_binary, '-m', 'ensurepip'], check=True)
        subprocess.run([python_binary, '-m', 'pip', 'install', *modules_to_install, "--user"], check=True)
