from bpy.props import FloatProperty
from . import global_def
from . import templates
from . import utils
from . import make_island

import operator

class SnapIsland(templates.OperatorTemplate):

    """Snap UV Islands by moving their vertex to the closest one"""
    bl_idname = "uv.snap_islands"
    bl_label = "Snap Islands"
    bl_options = {'REGISTER', 'UNDO'}

    threshold = FloatProperty(
        name="Threshold",
        description="Threshold for island matching",
        default=0.1,
        min=0,
        max=1,
        soft_min=0.01,
        soft_max=1,
        step=1,
        precision=2)

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        islands = makeIslands.islands
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()
        hiddenIslands = makeIslands.hiddenIslands()
        
        for island in hiddenIslands:
            islands.remove(island)
        
        if len(selectedIslands) < 2:
            for island in selectedIslands:
                utils.snapToUnselected(islands, self.threshold, island)
                
        else:
            if not activeIsland:
                self.report({"ERROR"}, "No active face")             
                return {"CANCELLED"}
            #selectedIslands.remove(activeIsland)
            for island in selectedIslands:
                utils.snapIsland(activeIsland, self.threshold, island)     
                
        utils.update()  
        return{'FINISHED'}
    
    
class MatchIsland(templates.OperatorTemplate):

    """Match UV Island by moving their vertex"""
    bl_idname = "uv.match_islands"
    bl_label = "Match Islands"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        makeIslands = make_island.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()
        
        if not activeIsland:
            self.report({"ERROR"}, "No active face")             
            return {"CANCELLED"}              

        if len(selectedIslands) > 1:
            if(operator.contains(selectedIslands, activeIsland)):
                selectedIslands.remove(activeIsland)
            
            activeIslandVert = 0
           
            for face_id in activeIsland:
                face = global_def.bm.faces[face_id]
                for loop in face.loops:
                    activeIslandVert += 1
            
            for island in selectedIslands:
                selectedIslandVert = 0        
                for face_id in island:
                    face = global_def.bm.faces[face_id]
                    for loop in face.loops:
                        selectedIslandVert += 1
                        
                if activeIslandVert != selectedIslandVert:  
                    self.report({"ERROR"}, "Islands have different number of verts!")             
                    return {"CANCELLED"}  
            
            utils.matchIslands(activeIsland, selectedIslands)      
        else:
            self.report({"ERROR"}, "Only two islands must be selected")             
            return {"CANCELLED"}       
              
                
        utils.update()  
        return{'FINISHED'}