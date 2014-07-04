@given(u'we start the budget main app')
def step_impl(context):
    context.qtapp.exec_()
