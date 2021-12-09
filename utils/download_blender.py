import os
import re
import tarfile
import time

import requests
import wget
from bs4 import BeautifulSoup
from operator import itemgetter
from pathlib import Path


def merge(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2


def writeProgress(size, total, width=80):
    progress_message = "\rDownloading: %d%% [%d / %d] bytes" % (size / total * 100, size, total,)
    print(progress_message, end="")
    pass


print("Downloading blender...")
# Set the URL you want to webscrape from
url = "https://builder.blender.org/download/"
# Connect to the URL
response = requests.get(url)
# Parse HTML and save to BeautifulSoup object
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

downloadlink = None
li = soup.find_all("li", class_=os_name, style="")
downloadLink = ""
downloadSize = 0
# iterate all <li> elem
elements = []
for elem in li:
    # if not elem.span.text.contain("Candidate"):
    #     continue
    # get the content and remove unused text,now remain only version
    version = elem.a.div.contents[0][8:-3]
    maj, min_ = [int(x) for x in version.split(".")][:2]  # take only major and minor

    downloadSize = float(elem.a.div.text.split(" - ")[-1][:-2]) * 1048576
    downloadLink = elem.a["href"]
    elements.append((maj, min_, downloadLink, downloadSize))

major_ver = max(elements, key=itemgetter(0))[0]
elements = list(filter(lambda x: x[0] == major_ver, elements))
minor_ver = max(elements, key=itemgetter(1))[1]
elements = list(filter(lambda x: x[1] == minor_ver, elements))

element = list(elements)[0]
print(f"version: {element[0]}.{element[1]} - {element[3]}MB")
print(downloadLink)

# downloadSize = float(a.find("span", {"class": "size"}).text[:-2]) * 1048576
# downloadLink = merge(url, a["href"])
time.sleep(1)

tmpDir = "../tmp/"
if not Path(archive).exists():
    wget.download(downloadLink, archive, writeProgress)


print("\nExtracting...")

if os.name == "nt":
    import zipfile

    with zipfile.ZipFile(archive, "r") as zip_ref:
        zip_ref.extractall(tmpDir)
elif os.name == "posix":
    import tarfile

    with tarfile.open(archive, "r") as tar_ref:
        tar_ref.extractall(tmpDir)

outDir = os.listdir(tmpDir)[0]
os.rename(os.path.abspath(tmpDir + outDir), blenderDir)
os.rmdir(tmpDir)
os.remove(archive)

r = re.compile(r"[0-9]\.[0-9]+")
versionDir = ""
for path in os.listdir(blenderDir):
    if r.match(path):
        versionDir = path
        break

os.symlink(
    os.path.abspath("uv_align_distribute"),
    "{0}/{1}/scripts/addons/uv_align_distribute".format(blenderDir, versionDir),
)
