import mgear.shifter.custom_step as cstp
import maya.cmds as cmds

class CustomShifterStep(cstp.customShifterMainStep):


    def setup(self):

        self.name = "04_mmdParent"

    def run(self):

        CENTERDICT={
            "hip_C0_0_jnt" : "koshi",
            "spine_C0_1_jnt" : "jouhanshin1",
            "spine_C0_2_jnt" : "jouhanshin2",
            "neck_C0_0_jnt" : "kubi",
            "neck_C0_head_jnt" : "atama",

            # 揺れものジョイント接続
            "tail_C0_0_jnt" : "o_0_1",
            "tail_C0_1_jnt" : "o_1_1",
            "tail_C0_2_jnt" : "o_2_1",
            "tail_C0_3_jnt" : "o_3_1",
            "tail_C0_4_jnt" : "o_4_1",
            "tail_C0_5_jnt" : "o_5_1",
            "tail_C0_6_jnt" : "o_6_1",
            "tail_C0_7_jnt" : "o_7_1",
            "tail_C0_8_jnt" : "o_8_1",
            "tail_C0_9_jnt" : "o_9_1",
            "tail_C0_10_jnt" : "o_10_1",
            "tail_C0_11_jnt" : "o_11_1",
            "tail_C0_12_jnt" : "o_12_1",
            "tail_C0_13_jnt" : "o_13_1",
            "tail_C0_14_jnt" : "o_14_1",
            "tail_C0_15_jnt" : "o_15_1",
            "tail_C0_16_jnt" : "o_16_1",
            "tail_C0_17_jnt" : "o_17_1",
            "tail_C0_18_jnt" : "o_18_1",
            "tail_C0_19_jnt" : "o_19_1",
            "tail_C0_20_jnt" : "o_20_1",
            "tail_C0_21_jnt" : "o_21_1",
            "tail_C0_22_jnt" : "o_22_1",
            "tail_C0_23_jnt" : "o_23_1",

            "bag_C0_0_jnt" : "tsutsumi",

            "tie_C0_0_jnt" : "Ctr_M_Tie_01",
            "tie_C0_1_jnt" : "Ctr_M_Tie_02",
            "tie_C0_2_jnt" : "Ctr_M_Tie_03",
            "tie_C0_3_jnt" : "Ctr_M_Tie_04",

            "jacket_C0_0_jnt" : "Ctr_M_Jac_01",
            "jacket_C0_1_jnt" : "Ctr_M_Jac_02",

            "Hair_C0_0_jnt" : "Ctr_M_Hair_01",
            "Hair_C0_1_jnt" : "Ctr_M_Hair_02",
            "Hair_C0_2_jnt" : "Ctr_M_Hair_03",
            "BangsRoot_C0_0_jnt" : "Ctr_M_BangsRoot_01",
            "BangsMain_L4_0_jnt" : "Ctr_M_BangsMain_04",
            "BangsMain_L4_1_jnt" : "Ctr_M_BangsMain_05",
            "BangsMain_R4_0_jnt" : "Ctr_M_BangsMain_01",
            "BangsMain_R4_0_jnt" : "Ctr_M_BangsMain_02",
            "F_C0_0_jnt" : "F_0_1",
            "F_C0_1_jnt" : "F_1_1",
            "F_C0_2_jnt" : "F_2_1",
            "F_C0_3_jnt" : "F_3_1",
            "F_C0_4_jnt" : "F_4_1",
            "F_C0_5_jnt" : "F_5_1",
            "F_C0_6_jnt" : "F_6_1",
            "F_C0_7_jnt" : "F_7_1",
            "F_C0_8_jnt" : "F_8_1",
            "F_C0_9_jnt" : "F_9_1",
            "F_C0_10_jnt" : "F_10_1",
            "F_C0_11_jnt" : "F_11_1",
            "F_C0_12_jnt" : "F_12_1",
            "F_C0_13_jnt" : "F_13_1",
            "F_C0_14_jnt" : "F_14_1",
            "F_C0_15_jnt" : "F_15_1",
            "F_C0_16_jnt" : "F_16_1",
            "F_C0_17_jnt" : "F_17_1",

            "kuchi_C0_0_jnt" : "kouchuu",

        }

        for mgearJnt, mmdJnt in CENTERDICT.items():
                cmds.parentConstraint(mgearJnt, mmdJnt, mo=True, weight=1)

        OVERLists=[
            ["spine_C0_0_jnt", "jouhanshin"],
            ["spine_C0_0_jnt", "kahanshin"]
        ]

        for mgearJnt, mmdJnt in OVERLists:
            cmds.parentConstraint(mgearJnt, mmdJnt, mo=True, weight=1)

        SIDEDICT={"L":("hidari","sa","FL"),"R":("migi","u","FR")}

        for side,mmdside in SIDEDICT.items():
            sayuu=mmdside[0]
            sy=mmdside[1]
            kami=mmdside[2]
            SIDEJNTS = {
                # 足ジョイント接続
                "leg_"+side+"0_0_jnt" : sayuu+"ashi",
                "leg_"+side+"0_1_jnt" : sayuu+"hiza",
                "leg_"+side+"0_end_jnt" : sayuu+"ashikubi",
                "foot_"+side+"0_0_jnt" : sayuu+"ashisakiEX",


                # 腕、指ジョイント接続
                "shoulder_"+side+"0_shoulder_jnt" : sayuu+"kata",
                "arm_"+side+"0_0_jnt" : sayuu+"ude",
                "arm_"+side+"0_1_jnt" : sayuu+"udemojiri",
                "arm_"+side+"0_2_jnt" : sayuu+"hiji",
                "arm_"+side+"0_3_jnt" : sayuu+"temojiri",
                "arm_"+side+"0_end_jnt" : sayuu+"tekubi",
                "thumb_"+side+"0_0_jnt" : sayuu+"oyayubi0",
                "thumb_"+side+"0_1_jnt" : sayuu+"oyayubi1",
                "thumb_"+side+"0_2_jnt" : sayuu+"oyayubi2",
                "finger_"+side+"0_0_jnt" : sayuu+"ninyubi1",
                "finger_"+side+"0_1_jnt" : sayuu+"ninyubi2",
                "finger_"+side+"0_2_jnt" : sayuu+"ninyubi3",
                "finger_"+side+"1_0_jnt" : sy+"chuuyubi1",
                "finger_"+side+"1_1_jnt" : sy+"chuuyubi2",
                "finger_"+side+"1_2_jnt" : sy+"chuuyubi3",
                "finger_"+side+"2_0_jnt" : sayuu+"kusuriyubi1",
                "finger_"+side+"2_1_jnt" : sayuu+"kusuriyubi2",
                "finger_"+side+"2_2_jnt" : sayuu+"kusuriyubi3",
                "finger_"+side+"3_0_jnt" : sayuu+"koyubi1",
                "finger_"+side+"3_1_jnt" : sayuu+"koyubi2",
                "finger_"+side+"3_2_jnt" : sayuu+"koyubi3",

                # 目ジョイント接続
                "eye_"+side+"0_eye_jnt" : sayuu+"me",

                # 足武器ジョイント接続
                "BootsWpn_"+side+"0_0_jnt" : sayuu+"BootsWpn_01",

                # 揺れものジョイント接続
                "Boots_"+side+"0_0_jnt" : "Ctr_"+side+"_Boots_01",
                "Boots_"+side+"0_1_jnt" : "Ctr_"+side+"_BootsPendent_02",
                "Boots_"+side+"1_0_jnt" : "Ctr_"+side+"_Boots_02",
                "Boots_"+side+"2_0_jnt" : "Ctr_"+side+"_Boots_03",
                "Boots_"+side+"3_0_jnt" : "Ctr_"+side+"_Boots_04",
                "Boots_"+side+"4_0_jnt" : "Ctr_"+side+"_Boots_05",
                "Boots_"+side+"4_1_jnt" : "Ctr_"+side+"_BootsPendent_01",

                "uphip_"+side+"0_0_jnt" : sayuu+"shiri1",
                "underhip_"+side+"0_0_jnt" : sayuu+"shiri2",

                "collar_"+side+"1_0_jnt" : "Ctr_"+side+"_Collar_01",
                "collar_"+side+"1_1_jnt" : "Ctr_"+side+"_Collar_02",
                "collar_"+side+"3_0_jnt" : "Ctr_"+side+"_Collar_03",
                "collar_"+side+"3_0_jnt" : "Ctr_"+side+"_Collar_04",
                
                "jacket_"+side+"1_0_jnt" : "Ctr_"+side+"1_Jac_01",
                "jacket_"+side+"1_1_jnt" : "Ctr_"+side+"1_Jac_02",
                "jacket_"+side+"2_0_jnt" : "Ctr_"+side+"2_Jac_01",
                "jacket_"+side+"2_1_jnt" : "Ctr_"+side+"2_Jac_02",
                "jacket_"+side+"3_0_jnt" : "Ctr_"+side+"3_Jac_01",
                "jacket_"+side+"3_1_jnt" : "Ctr_"+side+"3_Jac_02",

                "muneue_"+side+"0_0_jnt" : sayuu+"muneue2",

                "BangsMain_"+side+"0_0_jnt" : "Ctr_"+side+"_BangsMain_01",
                "BangsMain_"+side+"0_1_jnt" : "Ctr_"+side+"_BangsMain_02",
                "BangsMain_"+side+"1_0_jnt" : "Ctr_"+side+"_BangsMain_03",
                "BangsMain_"+side+"1_1_jnt" : "Ctr_"+side+"_BangsMain_04",
                "BangsMain_"+side+"3_0_jnt" : "Ctr_"+kami+"_BangsMain_02",
                "BangsMain_"+side+"2_0_jnt" : "Ctr_"+kami+"_BangsMain_01",
                "Ear_"+side+"0_0_jnt" : "Ctr_"+side+"_Ear_01",
                "EarHair_"+side+"0_0_jnt" : "Ctr_"+side+"_EarHair_01",
                "Hair_"+side+"1_0_jnt" : "Ctr_"+side+"1_Hair_01",
                "Hair_"+side+"1_1_jnt" : "Ctr_"+side+"1_Hair_02",
                "Hair_"+side+"1_2_jnt" : "Ctr_"+side+"1_Hair_03",
                "Hair_"+side+"2_0_jnt" : "Ctr_"+side+"2_Hair_01",
                "Hair_"+side+"2_1_jnt" : "Ctr_"+side+"2_Hair_02",
                "Hair_"+side+"2_2_jnt" : "Ctr_"+side+"2_Hair_03",
                "Hair_"+side+"3_0_jnt" : "Ctr_"+side+"3_Hair_01",
                "Hair_"+side+"3_1_jnt" : "Ctr_"+side+"3_Hair_02",
                "Hair_"+side+"3_2_jnt" : "Ctr_"+side+"3_Hair_03",

                "kuchi_"+side+"0_0_jnt" : "kuchi"+sayuu,
                
                "mayu_"+side+"0_0_jnt" : sayuu+"mayu1",
                "mayu_"+side+"1_0_jnt" : sayuu+"mayu2",
                "mayu_"+side+"2_0_jnt" : sayuu+"mayu3",
                
            }
            
            for mgearJnt,mmdJnt in SIDEJNTS.items():
                cmds.parentConstraint(mgearJnt, mmdJnt, mo=True, weight=1)

        for side,mmdside in SIDEDICT.items():
            sayuu=mmdside[0]
            sy=mmdside[1]
            WEAPONJNTS = {
                    # 武器接続
                "HandWpn_"+side+"0_0_jnt" : "Ctr_"+side+"_HandWpn_F",
                "HandWpn_"+side+"1_0_jnt" : "Ctr_"+side+"_HandWpn_03",
                "HandWpn_"+side+"2_0_jnt" : "Ctr_"+side+"_HandWpn_05",
                "HandWpn_"+side+"3_0_jnt" : "Ctr_"+side+"_HandWpn_07",
            }

            for mgearJnt,mmdJnt in WEAPONJNTS.items():
                cmds.parentConstraint(mgearJnt, mmdJnt, mo=False, weight=1)

        return