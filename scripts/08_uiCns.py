import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "08_uiCns"

    def run(self):

        CNSDICT = {
            "leg_L0_end_jnt" : "legUI_L0_ik_cns",
            "leg_R0_end_jnt" : "legUI_R0_ik_cns",
            "arm_L0_end_jnt" : "armUI_L0_ik_cns",
            "arm_R0_end_jnt" : "armUI_R0_ik_cns",
            "neck_C0_head_jnt" : "faceUI_C0_ik_cns",
        }

        CNSLIST = [
            ["spine_C0_0_jnt", "spineUI_C0_ik_cns"],
            ["spine_C0_0_jnt", "visUI_C0_ik_cns",]
        ]

        for tgt, obj in list(CNSDICT.items()) + CNSLIST:
            for axis in "XYZ":
                cmds.setAttr("{}.translate{}".format(obj, axis), l=False)
            cmds.pointConstraint(tgt, obj, mo=True)
        return
