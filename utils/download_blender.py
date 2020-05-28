import os
import re
import time
from pathlib import Path

import requests
import wget
from bs4 import BeautifulSoup

def merge(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2


def writeProgress(size, total, width=80):
    progress_message = "\rDownloading: %d%% [%d / %d] bytes" % (
        size / total * 100,
        size,
        total,
    )
    # print(progress_message, end="")
    pass

print("starting script...")
cwd = Path(os.path.dirname(__file__))
# Set the URL you want to webscrape from
url = "https://builder.blender.org/download/"
# Connect to the URL
response = requests.get(url)
# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

blenderDir = ""
os_name = ""
archive = ""

if os.name == "nt":
    blenderDir = "../blender-win"
    archive = blenderDir + ".zip"
    os_name = "os windows"
elif os.name == "posix":
    blenderDir = "../blender-linux"
    archive = blenderDir + ".tar.xz"
    os_name = "os linux"

li = soup.find_all("li", class_= os_name)[0]
a = li.find_all("a")[0]
downloadLink = merge(url, a["href"])
downloadSize = float(a.find("span", {"class": "size"}).text[:-2]) * 1048576
time.sleep(1)


wget.download(downloadLink, archive, writeProgress)

print("\nExtracting...")
tmpDir = "../tmp/"

if os.name == "nt":
    import zipfile
    with zipfile.ZipFile(archive, "r") as zip_ref:
        zip_ref.extractall(tmpDir)
elif os.name == "posix":
    import tarfile
    with tarfile.TarFile(archive, "r") as tar_ref:
        tar_ref.extractall(tmpDir)

outDir = os.listdir(tmpDir)[0]
os.rename(os.path.abspath(tmpDir + outDir), blenderDir)
os.rmdir(tmpDir)
os.remove(archive)

r = re.compile("[0-9]\.[0-9]{2}")
versionDir = [x for x in os.listdir(blenderDir) if r.match(x)][0]
os.symlink(
    os.path.abspath("uv_align_distribute"),
    "{0}/{1}/scripts/addons/uv_align_distribute".format(blenderDir, versionDir),
)
