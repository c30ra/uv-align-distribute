class __OperatorManager:
    def __init__(self):
        self.__operator_list = []
        self.__ui_list = []

    def addOperator(self, operator):
        self.__operator_list.append(operator)

    def classList(self):
        return self.__operator_list

    def addUI(self, ui):
        self.__ui_list.append(ui)

    def draw(self, context, layout):
        for ui in self.__ui_list:
            ui.draw(context, layout)


om = __OperatorManager()
