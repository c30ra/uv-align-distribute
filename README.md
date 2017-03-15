# [Blender Add-on] uv-align-distribute
This add-on help align and distribute uv island in the uv space


Master Status:  [![Build Status](https://travis-ci.org/c30ra/uv-align-distribute.svg?branch=master)](https://travis-ci.org/c30ra/uv-align-distribute)  
Development Status: [![Build Status](https://travis-ci.org/c30ra/uv-align-distribute.svg?branch=development)](https://travis-ci.org/c30ra/uv-align-distribute)

## Installation:  

  - download the zip file:  [uv_align_distribution](https://github.com/c30ra/uv-align-distribute/releases/latest)  
  - In blender user preference go to Add-ons page  
  - click on install from file  

## Usage:
### Instructions:
Interface/Menu Overview

The panel is subdivided into three sections: Alignment, Distribution and Others. The first section contains a total of 8 operators, the first six perform alignment respectively (from left to right, top to down) on: Left, Vertical, Right, Top, Horizontal, Bottom of the target element. This can be selected through the Relative to menu, and it could be: UV Space, Active Island or 2D cursor.

The seventh operator instead makes the islands point in the same "direction". The last one makes all the selected islands the same "scale" as the active one.

The second section contains all the operators to distribute islands. Distribution is performed from the first element (from left to right, from bottom to top) to the last. So you need at last three islands selected: two are the head and the tail, and the middle one is the island the operator works on.

The last section contains one operator: Match island. This operator makes two similar islands perfectly overlapped.

### Operator/Options Overview

All the operation here described are relative to the Bounding Box of the island.

#### Alignment:

  - Relative To: with this you choose on witch element is performed the alignment, UV space: take the UV space perimeter for alignment so from 0.0 to 1.0 space area; Cursor: use the 2D cursor; Active Island: use the active island to perform alignment

  - Selection as group: with this selected alignment is not performed on single UV island, but all the selected island are treated as a whole object, remember that if "Active" island is selected from "Relative To" menu from the selection is subtracted the active island.

  - Align Left: alignment is performed on the left edge of the target element(UV Space, Active island or curosr).

  - Align VAxis: alignment is performed on the vertical axis(the axis passing from the center) of the target element(UV Space, Active island or curosr).

  - Align Right: alignment is performed on the rightedge of the target element(UV Space, Active island or curosr).

  - Align Top: alignment is performed on the top edge of the target element(UV Space, Active island or curosr)

  - Align HAxis: alignment is performed on the horizontal axis(the axis passing from the center) of the target element(UV Space, Active island or curosr).

  - Align Bottom: alignment is performed on the bottom edge of the target element(UV Space, Active island or curosr)

  - Align Rotation: alignment is performed so the islands point in the same direction of the target element(UV Space, Active island or curosr)

  - Equalize Scale: Equalization is performed so the islands have the same scale of the active island.

#### Distribution:

All this distributions work correctly if the island are partially aligned horizontally..

  - Distribute LEdges: the distribution is performed so all the left edges of the islands are all equidistantly.

  - Distribute HCenters: the distribution is performed so all the centers of the islands are all equidistantly.

  - Distribute REdges: the distribution is performed so all the right edges of the islands are all equidistantly.

  - Equalize HGap: the distribution is performed so the horizontal distance between the islands is the same.

All these distributions work correctly if the islands are partially aligned vertically..

  - Distribute TEdges: the distribution is performed so all the top edges of the islands are all equidistantly.

  - Distribute VCenters: the distribution is performed so all the centers of the islands are all equidistantly.

  - Distribute BEdges: the distribution is performed so all the bottom edges of the islands are all equidistantly.

  - Equalize VGap: the distribution is performed so the vertical distance between the islands is the same.

#### Others:
  - Snap islands: snap vertices of the selected island on the acitve one(if present), or to the nearest one. Use threshold to adjust distance of matched verts.

  - Match Island: this operator makes two or more similar islands (same amount of vertices, similar shape) perfectly overlapped.

## Know Issues:

Sometimes alignment rotation doesn't work correctly, either due to floating point precision or because unwrapping makes some islands flipped or mirrored. You see this if all the islands point in the same direction, but one or more are flipped by 180°. In order to fix this, select those island and mirror them.

## Development
If you are interested in development of this add-on follow this link:  
[Api](docs/build/html/index.html)

## External Links

http://www.blenderartists.org/forum/showthread.php?340206-Add-On-UV-Align-Distribute

## Usage Examples:
https://www.youtube.com/embed/7V2b1G9TpLU  

https://www.youtube.com/embed/clgrf0DUvso

## Special Thanks to Blenderartists users:

**mifth:** for the support, YouTube video(usage example), and ideas for improving this add-on  
**jonim8or:** for part of the code used in this add-on.
