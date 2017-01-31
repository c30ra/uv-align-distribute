import glob
import subprocess
import sys

blenderExecutable = 'blender'

# allow override of blender executable (important for CI!)
if len(sys.argv) > 1:
    blenderExecutable = sys.argv[1]

# iterate over each *.test.blend file in the "tests" directory
# and open up blender with the .test.blend file
# and the corresponding .test.py python script.

print("start testing...")
gl = glob.glob('./tests/**/*.test.blend')
print("found %s tests: " % len(gl))

for file in gl:
    # print("executing:", file)
    subprocess.call([blenderExecutable, '--addons', 'uv_align_distribute',
                     '--factory-startup', '-noaudio', '-b', file, '--python',
                     file.replace('.blend', '.py')], stdout=subprocess.DEVNULL) 
