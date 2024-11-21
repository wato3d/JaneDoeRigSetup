import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "21_addBS"

    def run(self):
        
        target = "faceUI_C0_ctl"
        source = "bs_JaneDoe"

        cmds.addAttr(target, ln="facialAttr", niceName="__________", attributeType="enum", enumName="facial", keyable=True)

        attrName = [
            "majime",
            "komaru",
            "ikari",
            "ue",
            "shita",
            "uinku2",
            "uinku2migi",
            "uinkumigi",
            "uinku",
            "bikkurimigi",
            "bikkurihidari",
            "jitome",
            "ikarime2",
            "kanashimu",
            "shitameue",
            "a",
            "i",
            "u",
            "e",
            "o",
        ]

        for atr in attrName:
            cmds.addAttr(target, ln=atr, attributeType="float", min=0, max=10, dv=0, keyable=True)
            md = cmds.createNode("multiplyDivide")
            cmds.setAttr(md + ".input1X", 0.1)
            cmds.connectAttr(target + "." + atr, md + ".input2X", f=True)
            cmds.connectAttr(md + ".outputX", source + "." + atr, f=True)
      
        return
