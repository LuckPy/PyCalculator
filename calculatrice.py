from PySide6 import QtWidgets, QtCore
from functools import partial


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.display = []

    def setup_ui(self):
        self.create_layout()
        self.create_widgets()
        self.modify_widgets()
        self.css()
        self.setup_connexions()
        self.add_widgets_to_layout()
        self.setFixedSize(350, 600)
        self.setWindowTitle("pyCalculatrice")

    def create_layout(self):
        self.center_layout = QtWidgets.QWidget()
        self.setCentralWidget(self.center_layout)
        self.layout = QtWidgets.QGridLayout(self.center_layout)

    def create_widgets(self):
        # AFFICHAGE
        self.display_result = QtWidgets.QLineEdit()
        self.display_action = QtWidgets.QLineEdit()
        # NOMBRES
        self.buttons = {f"btn_{str(i)}": self.BtnNumber(str(i)) for i in range(10)}
        print(self.buttons)
        # OPERATEURS
        self.operators = {f"op_{str(i)}": self.BtnOperator(str(i)) for i in ["%", "/", "*", "-", "+", "="]}
        # UTILES
        self.utiles = {f"ut_{str(i)}": self.BtnOperator(str(i)) for i in ["AC", "DEL", ","]}
        # BRACKETS
        self.brakets = {f"br_{str(i)}": self.BtnBracket(str(i)) for i in ["(", ")"]}

    def modify_widgets(self):
        self.display_result.setFixedHeight(100)
        self.display_result.setReadOnly(True)
        self.display_action.setFixedHeight(40)
        self.display_action.setReadOnly(True)
        self.display_action.setAlignment(QtCore.Qt.AlignRight)
        self.display_result.setAlignment(QtCore.Qt.AlignRight)
    
    def css(self):
        self.setStyleSheet(
            "QWidget {background-color: #444c66;}"
            "QLineEdit {"
            "font-size: 20px;"
            "background-color: #1e1e1e;"
            "border: none;"
            "border-radius: 5px;}"       
            )       
        self.display_result.setStyleSheet("font-size: 38px;")

    def add_widgets_to_layout(self):
        # AFFICHAGE
        self.layout.addWidget(self.display_result, 0, 0, 1, 8)
        self.layout.addWidget(self.display_action, 1, 0, 1, 8)
        # NOMBRES
        self.layout.addWidget(self.buttons["btn_0"], 6, 2, 1, 2)
        self.layout.addWidget(self.buttons["btn_1"], 5, 0, 1, 2)
        self.layout.addWidget(self.buttons["btn_2"], 5, 2, 1, 2)
        self.layout.addWidget(self.buttons["btn_3"], 5, 4, 1, 2) 
        self.layout.addWidget(self.buttons["btn_4"], 4, 0, 1, 2)
        self.layout.addWidget(self.buttons["btn_5"], 4, 2, 1, 2)
        self.layout.addWidget(self.buttons["btn_6"], 4, 4, 1, 2)
        self.layout.addWidget(self.buttons["btn_7"], 3, 0, 1, 2)
        self.layout.addWidget(self.buttons["btn_8"], 3, 2, 1, 2)
        self.layout.addWidget(self.buttons["btn_9"], 3, 4, 1, 2)
        # OP
        self.layout.addWidget(self.operators["op_%"], 2, 4, 1, 2)
        self.layout.addWidget(self.operators["op_/"], 2, 6, 1, 2)
        self.layout.addWidget(self.operators["op_*"], 3, 6, 1, 2)
        self.layout.addWidget(self.operators["op_-"], 4, 6, 1, 2)
        self.layout.addWidget(self.operators["op_+"], 5, 6, 1, 2)
        self.layout.addWidget(self.operators["op_="], 6, 6, 1, 2)
        
        self.layout.addWidget(self.utiles["ut_AC"], 2, 0, 1, 2) 
        self.layout.addWidget(self.utiles["ut_DEL"], 2, 2, 1, 2)
        self.layout.addWidget(self.utiles["ut_,"], 6, 4, 1, 2)
        self.layout.addWidget(self.brakets["br_("], 6, 0, 1, 1)
        self.layout.addWidget(self.brakets["br_)"], 6, 1, 1, 1)

    def setup_connexions(self):
        self.buttons["btn_0"].clicked.connect(partial(self.add_to_display, self.buttons["btn_0"].text()))
        self.buttons["btn_1"].clicked.connect(partial(self.add_to_display, self.buttons["btn_1"].text()))
        self.buttons["btn_2"].clicked.connect(partial(self.add_to_display, self.buttons["btn_2"].text()))
        self.buttons["btn_3"].clicked.connect(partial(self.add_to_display, self.buttons["btn_3"].text()))
        self.buttons["btn_4"].clicked.connect(partial(self.add_to_display, self.buttons["btn_4"].text()))
        self.buttons["btn_5"].clicked.connect(partial(self.add_to_display, self.buttons["btn_5"].text()))
        self.buttons["btn_6"].clicked.connect(partial(self.add_to_display, self.buttons["btn_6"].text()))
        self.buttons["btn_7"].clicked.connect(partial(self.add_to_display, self.buttons["btn_7"].text()))
        self.buttons["btn_8"].clicked.connect(partial(self.add_to_display, self.buttons["btn_8"].text()))
        self.buttons["btn_9"].clicked.connect(partial(self.add_to_display, self.buttons["btn_9"].text()))
        self.operators["op_%"].clicked.connect(partial(self.add_to_display, self.operators["op_%"].text()))
        self.operators["op_/"].clicked.connect(partial(self.add_to_display, self.operators["op_/"].text()))
        self.operators["op_*"].clicked.connect(partial(self.add_to_display, self.operators["op_*"].text()))
        self.operators["op_-"].clicked.connect(partial(self.add_to_display, self.operators["op_-"].text()))
        self.operators["op_+"].clicked.connect(partial(self.add_to_display, self.operators["op_+"].text()))      
        self.utiles["ut_,"].clicked.connect(partial(self.add_to_display, self.utiles["ut_,"].text()))
        self.brakets["br_("].clicked.connect(partial(self.add_to_display, self.brakets["br_("].text()))
        self.brakets["br_)"].clicked.connect(partial(self.add_to_display, self.brakets["br_)"].text()))
        self.utiles["ut_DEL"].clicked.connect(self.del_last_entry)
        self.utiles["ut_AC"].clicked.connect(self.reset)
        self.operators["op_="].clicked.connect(self.sum_display_action)

    def add_to_display(self, element):
        self.display.append(element)
        self.display_action.setText("".join(self.display))

    def del_last_entry(self):
        self.display.pop()   
        self.display_action.setText("".join(self.display))

    def sum_display_action(self):
        self.display = [i.replace("%", "/100") for i in self.display]
        self.display_result.setText(str(eval("".join(self.display))))
        self.display_action.clear()
        self.display.clear()

    def reset(self):
        self.display_result.setText("")
        self.display_action.setText("")
        self.display.clear()

    class Btn(QtWidgets.QPushButton):
        def __init__(self, text):
            super().__init__()
            self.setFixedSize(80, 80)
            self.setText(text)
            self.setStyleSheet(
                "Btn { background-color: #f0f8ff; font-size: 20px; border: none; border-radius: 5px; color: black;}"
                "Btn:hover {background-color: #d4dbe1;}"
            )

    class BtnOperator(Btn):
        def __init__(self, text):
            super().__init__(text=text)

    class BtnNumber(Btn):
        def __init__(self, text):
            super().__init__(text=text)
    
    class BtnBracket(Btn):
        def __init__(self, text):
            super().__init__(text=text)
            self.setFixedSize(37, 80)



App = QtWidgets.QApplication([])
win = MainWindow()
win.show()
App.exec_()
