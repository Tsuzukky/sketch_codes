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

        ##group_widget#
        
        self.Group_OpenMenu = QtWidgets.QGroupBox("Houdini_Script_Maneger",self)
        self.Group_Layout_A = QtWidgets.QVBoxLayout(self)
        
        #Text_widget
        
        self.text_wd = QtWidgets.QTextEdit(self)
        self.text_wd.append("textfrom here")
        
        #Button_widget
        
        self.button_wd = QtWidgets.QPushButton("process",self)
        
        #scrollBar_widget
        self.scroll_wd = QtWidgets.QScrollBar(self)
        
        #self.text_wd.setAligment(QtCore.Qt.AlignLeft)
     
        #_____________________________________##

        self.Group_Layout_A.addWidget(self.Group_OpenMenu)
        self.Group_Layout_A.addWidget(self.text_wd)
        self.Group_Layout_A.addWidget(self.button_wd)
        self.Group_Layout_A.addWidget(self.scroll_wd)
        #Layout_Detail#
        self.Group_Layout_A.setAlignment(QtCore.Qt.AlignTop)
        ##______________end___________________##
        
        #insert Widgets
        self.GlobalLayout_A.addLayout(self.Group_Layout_A)
        
        self.show()
        
        
        
        
A = Tool_widgets()

A.show()
