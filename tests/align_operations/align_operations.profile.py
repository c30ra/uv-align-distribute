import cProfile
from pstats import Stats

import bpy

override = None
for window in bpy.context.window_manager.windows:
    screen = window.screen

    for area in screen.areas:
        if area.type == "IMAGE_EDITOR":
            override = {'window': window, 'screen': screen, 'area': area}
            break

cp = cProfile.Profile()

cp.runcall(bpy.ops.uv.align_left_margin, override)

ps = Stats(cp)
ps.strip_dirs()
ps.sort_stats('cumtime')
ps.print_stats()
