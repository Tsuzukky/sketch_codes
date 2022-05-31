import hou
from PySide2 import QtWidgets,QtGui,QtCore


class Tool_widgets(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super(Tool_widgets,self).__init__(*args,**kwargs)

        ##Qt(PySide)Style__Houdini__##
        self.setStyleSheet(hou.qt.styleSheet())
        self.setProperty("houdiniStyle", True)
        ##______________end___________________##
        
        
        ##Main_Widgets_Layout##
        self.GlobalLayout_A = QtWidgets.QVBoxLayout(self)

        ##groupframe_Layout##
        #Group_A#
        self.Group_OpenMenu = QtWidgets.QGroupBox("Houdini_Script_Maneger",self)
        self.Group_Layout_A = QtWidgets.QVBoxLayout(self)
        
        #_____________________________________##

        self.Group_Layout_A.addWidget(self.Group_OpenMenu)
        #Layout_Detail#
        self.Group_Layout_A.setAlignment(QtCore.Qt.AlignLeft| QtCore.Qt.AlignTop)
        ##______________end___________________##
        
        #insert Widgets
        self.GlobalLayout_A.addLayout(self.Group_Layout_A)
        
        self.show()
        
        
        
        
A = Tool_widgets()

A.show()
