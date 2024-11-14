import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "02_boneHierarchy"

    def run(self):

        cmds.parent("Ctr_R_HandWpn_F", "JaneDoe__Bip001_Prop2")
        cmds.delete("Bip001_Prop1")

        return
