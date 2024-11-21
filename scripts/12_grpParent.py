import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):


    def setup(self):

        self.name = "12_grpParent"

    def run(self):

        cmds.group(["JaneDoe_subetenooya","JaneDoe_sousachuushin","JaneDoe__Bip001_Prop2"], n="bind_jnt_org")
        cmds.parent("bind_jnt_org", "JaneDoeRig")
        cmds.group(["JaneDoe","JaneDoe_"], n="geo_org")
        cmds.parent("geo_org", "JaneDoeRig")

        return