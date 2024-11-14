import mgear.shifter.custom_step as cstp
import maya.cmds as cmds


class CustomShifterStep(cstp.customShifterMainStep):

    def setup(self):

        self.name = "01_importModel"

    def run(self):
        
        file_path = cmds.fileDialog2(
            fileMode=1,
            caption="Select a Maya Binary File",
            fileFilter="Maya Binary (*.mb)",
        )
        cmds.file(file_path, i=True, ignoreVersion=True, namespace=":",)
        return
