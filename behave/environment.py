from budget import MainApp

def before_all(context) :
    (context.qtapp, context.mainapp) = MainApp.appObjects()
