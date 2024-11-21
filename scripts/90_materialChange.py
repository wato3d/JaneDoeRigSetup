import mgear.shifter.custom_step as cstp
import maya.cmds as cmds
import maya.mel as mel

class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "90_materialChange"

    def run(self):

        MATERIALDICT = {
            "kami_png_file_JaneDoe" : {
                "kami_mat_JaneDoeSG" : "hair_mat", "kami2_mat_JaneDoeSG" : "napeHair_mat", "hada2_mat_JaneDoeSG" : "finger_mat", 
                "maegami_mat_JaneDoeSG" : "bangsHair_mat", "karada2_mat_JaneDoeSG" : "accessories_mat", 
            },
            "spa_h_png_file_JaneDoe" : {
                "kami__mat_JaneDoeSG" : "hair2_mat"
            },
            "__png_file_JaneDoe" : {
                "mayu_mat_JaneDoeSG" : "eyebrow_mat", "_2_mat_JaneDoeSG" : "mouth_mat", "mekage_mat_JaneDoeSG" : "eyeShadow_mat",
                "__mat_JaneDoeSG" : "face_mat", "__mat_JaneDoe1SG" : "teeth_mat", "me_mat_JaneDoeSG" : "eye_mat", "kuchi__mat_JaneDoeSG" : "mouth2_mat", 
                "matsuge_mat_JaneDoeSG" : "eyelash_mat", "nijuu_mat_JaneDoeSG" : "eyebrow2_mat", "shirome_mat_JaneDoeSG" : "whiteEyes_mat", "kouzetsu_mat_JaneDoeSG" : "insideMouth_mat", 
            },
            "karada_png_file_JaneDoe" : {
                "karada_mat_JaneDoeSG" : "jacketBoots_mat", "o_mat_JaneDoeSG" : "tail_mat", "hada_mat_JaneDoeSG" : "leg_mat",
            },
            "buki_png_file_JaneDoe_" : {
                "MAT_JaneDoe_Weapon_mat_JaneDoe_SG" : "Weapon_mat"
            },
        }

        file_path = cmds.fileDialog2(
            fileMode=1,
            caption="Select a MayaToonOutline",
            fileFilter="FX file (*.fx)",
        )
        
        for png, materials in MATERIALDICT.items():
            if png in ["kami_png_file_JaneDoe", "spa_h_png_file_JaneDoe"]:
                text="Select a Hair Texture File"
            elif png == "__png_file_JaneDoe":
                text="Select a Face Texture File"
            elif png == "karada_png_file_JaneDoe":
                text="Select a Body Texture File"
            elif png == "buki_png_file_JaneDoe_":
                text="Select a Weapon Texture File"
            png_path = cmds.fileDialog2(
                fileMode=1,
                caption=text,
                fileFilter="PNG image (*.png)",
            )
            for shading, matName in materials.items():
                dxShader = cmds.shadingNode("dx11Shader", asShader=True, n=matName)
                cmds.setAttr(dxShader + ".shader", file_path[0], type="string")
                cmds.setAttr(dxShader + ".xBaseColorMapUv", 1)
                cmds.connectAttr(png + ".outColor", dxShader + ".xBaseColorMap")
                if matName in ["bangsHair_mat", "insideMouth_mat", "eyelash_mat", "mouth2_mat", "teeth_mat", "whiteEyes_mat", "eyeShadow_mat",]:
                    cmds.setAttr(dxShader + ".technique", "Toon", type="string")
                    if matName in ["eyeShadow_mat"]:
                        cmds.setAttr(dxShader + ".xOpacity", 0.4)
                self.replace_material(shading, dxShader)
            cmds.setAttr(png + ".fileTextureName", png_path[0], type="string")

        mel.eval('MLdeleteUnused;')
        cmds.colorManagementPrefs(edit=True, viewName="Un-tone-mapped")

        return
    
    def replace_material(self, shading_group, new_material):
        current_material = cmds.listConnections(shading_group + ".surfaceShader", source=True)
        if current_material:
            current_material = current_material[0]
            cmds.disconnectAttr(current_material + ".outColor", shading_group + ".surfaceShader")
        cmds.connectAttr(new_material + ".outColor", shading_group + ".surfaceShader", force=True)