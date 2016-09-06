import bpy
import bmesh
from . import global_def
import mathutils
import math

def InitBMesh():


    global_def.bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
    global_def.bm.faces.ensure_lookup_table()
    #uvlayer = bm.loops.layers.uv.active

    global_def.uvlayer = global_def.bm.loops.layers.uv.verify()
    global_def.bm.faces.layers.tex.verify()  # currently blender needs both layers.


def update():
    bmesh.update_edit_mesh(bpy.context.edit_object.data, False, False)
    # bm.to_mesh(bpy.context.object.data)
    # bm.free()

def GBBox(islands):
    minX = minY = 1000
    maxX = maxY = -1000
    for island in islands:
        for face_id in island:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                u, v = loop[global_def.uvlayer].uv
                minX = min(u, minX)
                minY = min(v, minY)
                maxX = max(u, maxX)
                maxY = max(v, maxY)

    return mathutils.Vector((minX, minY)), mathutils.Vector((maxX, maxY))


def GBBoxCenter(islands):
    minX = minY = 1000
    maxX = maxY = -1000
    for island in islands:
        for face_id in island:
            face = global_def.bm.faces[face_id]
            for loop in face.loops:
                u, v = loop[global_def.uvlayer].uv
                minX = min(u, minX)
                minY = min(v, minY)
                maxX = max(u, maxX)
                maxY = max(v, maxY)

    return (mathutils.Vector((minX, minY)) +
            mathutils.Vector((maxX, maxY))) / 2


def BBox(island):
    minX = minY = 1000
    maxX = maxY = -1000
    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            u, v = loop[global_def.uvlayer].uv
            minX = min(u, minX)
            minY = min(v, minY)
            maxX = max(u, maxX)
            maxY = max(v, maxY)

    return mathutils.Vector((minX, minY)), mathutils.Vector((maxX, maxY))


def BBoxCenter(island):
    minX = minY = 1000
    maxX = maxY = -1000
    # for island in islands:
    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            u, v = loop[global_def.uvlayer].uv
            minX = min(u, minX)
            minY = min(v, minY)
            maxX = max(u, maxX)
            maxY = max(v, maxY)

    return (mathutils.Vector((minX, minY)) +
            mathutils.Vector((maxX, maxY))) / 2


def islandAngle(island):
    uvList = []
    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            uv = loop[global_def.bm.loops.layers.uv.active].uv
            uvList.append(uv)

    angle = math.degrees(mathutils.geometry.box_fit_2d(uvList))
    return angle


def moveIslands(vector, island):
    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            loop[global_def.bm.loops.layers.uv.active].uv += vector


def rotateIsland(island, angle):
    rad = math.radians(angle)
    center = BBoxCenter(island)

    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            uv_act = global_def.bm.loops.layers.uv.active
            x, y = loop[uv_act].uv
            xt = x - center.x
            yt = y - center.y
            xr = (xt * math.cos(rad)) - (yt * math.sin(rad))
            yr = (xt * math.sin(rad)) + (yt * math.cos(rad))
            # loop[global_def.bm.loops.layers.uv.active].uv = trans
            loop[global_def.bm.loops.layers.uv.active].uv.x = xr + center.x
            loop[global_def.bm.loops.layers.uv.active].uv.y = yr + center.y


def scaleIsland(island, scaleX, scaleY):
    center = BBoxCenter(island)

    for face_id in island:
        face = global_def.bm.faces[face_id]
        for loop in face.loops:
            x = loop[global_def.bm.loops.layers.uv.active].uv.x
            y = loop[global_def.bm.loops.layers.uv.active].uv.y
            xt = x - center.x
            yt = y - center.y
            xs = xt * scaleX
            ys = yt * scaleY
            loop[global_def.bm.loops.layers.uv.active].uv.x = xs + center.x
            loop[global_def.bm.loops.layers.uv.active].uv.y = ys + center.y


def vectorDistance(vector1, vector2):
    return math.sqrt(
        math.pow((vector2.x - vector1.x), 2) +
        math.pow((vector2.y - vector1.y), 2))


def snapIsland(active, threshold, selectedIslands):
    bestMatcherList = []
    for face_id in selectedIslands:
        face = global_def.bm.faces[face_id]

        for loop in face.loops:
            selectedUVvert = loop[global_def.bm.loops.layers.uv.active]
            uvList = []

            for active_face_id in active:
                active_face = global_def.bm.faces[active_face_id]

                for active_loop in active_face.loops:
                    activeUVvert = active_loop[global_def.bm.loops.layers.uv.active].uv

                    dist = vectorDistance(selectedUVvert.uv, activeUVvert)
                    uvList.append((dist, active_loop[global_def.bm.loops.layers.uv.active]))

            #for every vert in uvList take the ones with the shortest distnace from ref
            minDist = uvList[0][0]
            bestMatcher = 0

            #1st pass get lower dist
            for bestDist in uvList:
                if bestDist[0] <= minDist:
                    minDist = bestDist[0]

            #2nd pass get the only ones with a match
            for bestVert in uvList:
                if bestVert[0] <= minDist:
                    bestMatcherList.append((bestVert[0], selectedUVvert, bestVert[1].uv))

    for bestMatcher in bestMatcherList:
        if bestMatcher[0] <= threshold:
            bestMatcher[1].uv = bestMatcher[2]

def snapToUnselected(islands, threshold, selectedIslands):
    bestMatcherList = []
    islands.remove(selectedIslands)

    for face_id in selectedIslands:
        face = global_def.bm.faces[face_id]

        for loop in face.loops:
            selectedUVvert = loop[global_def.bm.loops.layers.uv.active]
            uvList = []

            for targetIsland in islands:
                for targetFace_id in targetIsland:
                    targetFace = global_def.bm.faces[targetFace_id]
                    for targetLoop in targetFace.loops:
                        #take the a reference vert
                        targetUvVert = targetLoop[global_def.bm.loops.layers.uv.active].uv
                        #get a selected vert and calc it's distance from the ref
                        #add it to uvList
                        dist = round(vectorDistance(selectedUVvert.uv, targetUvVert), 10)
                        uvList.append((dist, targetLoop[global_def.bm.loops.layers.uv.active]))

            #for every vert in uvList take the ones with the shortest distnace from ref
            minDist = uvList[0][0]
            bestMatcher = 0

            #1st pass get lower dist
            for bestDist in uvList:
                if bestDist[0] <= minDist:
                    minDist = bestDist[0]

            #2nd pass get the only ones with a match
            for bestVert in uvList:
                if bestVert[0] <= minDist:
                    bestMatcherList.append((bestVert[0], selectedUVvert, bestVert[1].uv))

    for bestMatcher in bestMatcherList:
        if bestMatcher[0] <= threshold:
            bestMatcher[1].uv = bestMatcher[2]

def _sortCenter(list):

    scambio  = True
    n = len(list)
    while scambio:
        scambio = False
        for i in range(0, n-1):
            if (list[i][0].x <= list[i+1][0].x) and (list[i][0].y > list[i+1][0].y):
                list[i], list[i+1] = list[i+1], list[i]

                scambio = True
    return list

def _sortVertex(vertexList, BBCenter):

    anglesList = []
    for v in vertexList:
        #atan2(P[i].y - M.y, P[i].x - M.x)
        angle = math.atan2(v.uv.y - BBCenter.y, v.uv.x - BBCenter.x )
        anglesList.append((v, angle))

    vertsAngle = sorted(anglesList, key=lambda coords: coords[0].uv)
    #vertsAngle = sorted(anglesList, key=lambda angle: angle[1])
    newList = []
    for i in vertsAngle:
        newList.append(i[0])

    return newList

def sortFaces(faceList):
    anglesList = []
    for f in faceList:
        faceCenter = f[0]
        perFaceVertsAngle = []
        for v in f[1]:
            #atan2(P[i].y - M.y, P[i].x - M.x)
            angle = math.atan2(v.uv.y - faceCenter.y, v.uv.x - faceCenter.x )
            perFaceVertsAngle.append((v, angle))

        perFaceVertsAngle2 = sorted(perFaceVertsAngle, key=lambda angle: angle[1])

        anglesList.append(perFaceVertsAngle2)

    newList = []
    for data in anglesList:
        for vert in data:
            newList.append(vert[0])

    return newList

def islandVertexOrder(island):
    uvData = []
    faceData = []
    for face_id in island:
        face = global_def.bm.faces[face_id]
        uvList = []
        for loop in face.loops:

            loopData = loop[global_def.bm.loops.layers.uv.active]
            uvData.append(loopData)
            uvList.append(loopData)

        faceCenter = 0
        vX = 0
        vY = 0
        for uv in uvList:
            vX += uv.uv.x
            vY += uv.uv.y
        vertNum = len(uvList)
        faceCenter = mathutils.Vector((vX / vertNum, vY / vertNum))
        uvList = sorted(uvList, key=lambda data: data.uv)
        #uvList = sorted(uvList, key=lambda data: round(data.uv.y, 2), reverse=True)
        #uvList = _sortVertex(uvList)
        faceData.append((faceCenter, uvList))

    faceData2 = sortFaces(faceData)
    #faceData = _sortCenter(faceData)
    counter = 0

    return faceData2

def getTargetPoint(context, islands):
    if context.scene.relativeItems == 'UV_SPACE':
        return mathutils.Vector((0.0, 0.0)), mathutils.Vector((1.0, 1.0))
    elif context.scene.relativeItems == 'ACTIVE':
        activeIsland = islands.activeIsland()
        if not activeIsland:
            return None
        else:
            return BBox(activeIsland)
    elif context.scene.relativeItems == 'CURSOR':
        return context.space_data.cursor_location,\
            context.space_data.cursor_location


def IslandSpatialSortX(islands):
    spatialSort = []
    for island in islands:
        spatialSort.append((BBoxCenter(island).x, island))
    spatialSort.sort()
    return spatialSort


def IslandSpatialSortY(islands):
    spatialSort = []
    for island in islands:
        spatialSort.append((BBoxCenter(island).y, island))
    spatialSort.sort()
    return spatialSort


def averageIslandDist(islands):
    distX = 0
    distY = 0
    counter = 0

    for i in range(len(islands)):
        elem1 = BBox(islands[i][1])[1]
        try:
            elem2 = BBox(islands[i + 1][1])[0]
            counter += 1
        except:
            break

        distX += elem2.x - elem1.x
        distY += elem2.y - elem1.y

    avgDistX = distX / counter
    avgDistY = distY / counter
    return mathutils.Vector((avgDistX, avgDistY))


def islandSize(island):
    bbox = BBox(island)
    sizeX = bbox[1].x - bbox[0].x
    sizeY = bbox[1].y - bbox[0].y

    return sizeX, sizeY

def determinant(vec1, vec2):
    return vec1.x * vec2.y - vec1.y * vec2.x;

def edgeIntersection(vec_a, vec_b, vec_c, vec_d):
    #one edge is a-b, the other is c-d
    det = determinant(vec_b - vec_a, vec_c - vec_d);
    t   = determinant(vec_c - vec_a, vec_c - vec_d) / det;
    u   = determinant(vec_b - vec_a, vec_c - vec_a) / det;
    if ((t < 0) or (u < 0) or (t > 1) or (u > 1)):
        return False
    else:
        return True
