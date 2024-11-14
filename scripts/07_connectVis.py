import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "07_connectVis"

    def run(self):

        target = "visUI_C0_ctl"

        UIDICT = {
            "L Arm UI Vis" : {
                "l_armUI_vis" : "armUI_L0_ctl"
                },
            "R Arm UI Vis" : {
                "r_armUI_vis" : "armUI_R0_ctl"
                },
            "L Leg UI Vis" : {
                "l_legUI_vis" : "legUI_L0_ctl"
                },
            "R Leg UI Vis" : {
                "r_legUI_vis" : "legUI_R0_ctl"
                },
            "Facial UI Vis" : {
                "facialUI_vis" : "faceUI_C0_ctl"
                },
            "Spine UI Vis" : {
                "spineUI_vis" : "spineUI_C0_ctl"
                },
        }

        CTLDICT = {
            "Hair Ctl Vis" : {
                "hairCtl_vis" : ["F_C0_fk0_ctl", "BangsRoot_C0_ctl", "Hair_C0_fk0_ctl",]
                },
            "BackHair Ctl Vis" : {
                "backHairCtl_vis" : "F_C0_fk0_ctl"
                },
            "Facial Ctl Vis" : {
                "facialCtl_vis" : "kuchi_C0_ctl",
                },
            "Collar Ctl Vis" : "collarCtl_vis",
            "Jacket Ctl Vis" : {
                "jacketCtl_vis" : ["tie_C0_fk0_ctl", "jacket_C0_fk0_ctl"]
                },
            "Tail Ctl Vis" : {
                "tailCtl_vis" : "tail_C0_fk0_ctl"
                },
            "Boots Ctl Vis" : "bootsCtl_vis",
            "Weapon Ctl Vis" : "weaponCtl_vis",
        }

        SIDEDICT = {"L", "R"}

        cmds.addAttr(target, ln="uivis", nn="__________", at="enum", en="ui vis", k=True)
        for nc, val in UIDICT.items():
            for long, ctlName in val.items():
                cmds.addAttr(target, ln=long, nn=nc, at="bool", dv=True, k=True)
                cmds.setAttr(ctlName + ".visibility", l=False)
                cmds.connectAttr(target + "." + long, ctlName + ".visibility", f=True)

        cmds.addAttr(target, ln="ctlvis", nn="__________", at="enum", en="ctl vis", k=True)
        for nc, val in CTLDICT.items():
            if isinstance(val, dict):
                for long, ctlName in val.items():
                    cmds.addAttr(target, ln=long, nn=nc, at="bool", dv=True, k=True)
                    if isinstance(ctlName, list):
                        if long == "hairCtl_vis":
                            for side in SIDEDICT:
                                HairDICT = [
                                    "BangsMain_"+side+"4_fk0_ctl",
                                    "BangsMain_"+side+"3_ctl",
                                    "BangsMain_"+side+"2_ctl",
                                    "BangsMain_"+side+"1_fk0_ctl",
                                    "BangsMain_"+side+"0_fk0_ctl",
                                    "EarHair_"+side+"0_ctl",
                                    "Hair_"+side+"1_fk0_ctl",
                                    "Hair_"+side+"2_fk0_ctl",
                                    "Hair_"+side+"3_fk0_ctl",
                                ]
                                for ctl in HairDICT:
                                    cmds.setAttr(ctl + ".visibility", l=False)
                                    cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                            for ctl in ctlName:
                                cmds.setAttr(ctl + ".visibility", l=False)
                                cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                        elif long == "jacketCtl_vis":
                            for side in SIDEDICT:
                                JACKETDICT = [
                                    "jacket_"+side+"1_fk0_ctl",
                                    "jacket_"+side+"2_fk0_ctl",
                                    "jacket_"+side+"3_fk0_ctl",
                                    "muneue_"+side+"0_ctl",
                                ]
                                for ctl in JACKETDICT:
                                    cmds.setAttr(ctl + ".visibility", l=False)
                                    cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                            for ctl in ctlName:
                                cmds.setAttr(ctl + ".visibility", l=False)
                                cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                    else:
                        if long == "backHairCtl_vis":
                            for i in range(1, 7):
                                cmds.setAttr("F_C0_ik" + str(i) + "_ctl" + ".visibility", l=False)
                                cmds.connectAttr(target + "." + long, "F_C0_ik" + str(i) + "_ctl" + ".visibility", f=True)
                        elif long == "tailCtl_vis":
                            for i in range(1, 8):
                                cmds.setAttr("tail_C0_ik" + str(i) + "_ctl" + ".visibility", l=False)
                                cmds.connectAttr(target + "." + long, "tail_C0_ik" + str(i) + "_ctl" + ".visibility", f=True)
                        elif long == "facialCtl_vis":
                            for side in SIDEDICT:
                                FACIALDICT = [
                                    "kuchi_"+side+"0_ctl",
                                    "mayu_"+side+"0_ctl",
                                    "mayu_"+side+"1_ctl",
                                    "mayu_"+side+"2_ctl",
                                ]
                                for ctl in FACIALDICT:
                                    cmds.setAttr(ctl + ".visibility", l=False)
                                    cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                        cmds.setAttr(ctlName + ".visibility", l=False)
                        cmds.connectAttr(target + "." + long, ctlName + ".visibility", f=True)
            else:
                long=val
                cmds.addAttr(target, ln=long, nn=nc, at="bool", dv=True, k=True)
                if val == "bootsCtl_vis":
                    for side in SIDEDICT:
                        BOOTSDICT = [
                            "Boots_"+side+"0_fk0_ctl",
                            "Boots_"+side+"1_fk0_ctl",
                            "Boots_"+side+"2_fk0_ctl",
                            "Boots_"+side+"3_fk0_ctl",
                            "Boots_"+side+"4_fk0_ctl",
                        ]
                        for ctl in BOOTSDICT:
                            cmds.setAttr(ctl + ".visibility", l=False)
                            cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                elif val == "collarCtl_vis":
                    for side in SIDEDICT:
                        COLLAERDICT = [
                            "collar_"+side+"1_fk0_ctl",
                            "collar_"+side+"3_fk0_ctl",
                        ]
                        for ctl in COLLAERDICT:
                            cmds.setAttr(ctl + ".visibility", l=False)
                            cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
                elif val == "weaponCtl_vis":
                    for side in SIDEDICT:
                        WEAPONDICT = [
                            "HandWpn_"+side+"0_ctl",
                        ]
                        for ctl in WEAPONDICT:
                            cmds.setAttr(ctl + ".visibility", l=False)
                            cmds.connectAttr(target + "." + long, ctl + ".visibility", f=True)
        return
