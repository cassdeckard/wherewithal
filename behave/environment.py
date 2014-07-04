from budget import MainApp

import threading

def before_all(context) :
    (context.qtapp, context.mainapp) = MainApp.appObjects()
    context.thread = threading.Thread(target=context.qtapp.exec_)
