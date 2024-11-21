import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):


    def setup(self):

        self.name = "11_setAttr"

    def run(self):

        cmds.setAttr("JaneDoeRig.jnt_vis", 0)
        cmds.setAttr("JaneDoeRig.ctl_vis_on_playback", 0)

        cmds.setAttr("JaneDoe_subetenooya.visibility", 0)
        cmds.setAttr("JaneDoe_sousachuushin.visibility", 0)
        cmds.setAttr("JaneDoe__Bip001_Prop2.visibility", 0)
        
        cmds.setAttr("guide.visibility", 0)

        return