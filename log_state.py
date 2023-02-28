import glob
import inspect


def log_state(text, var1=None, var2=None, var3=None, var4=None):
    return
    print("########################################################################")
    print("#####################> State <##########################################")

    if var1 is not None:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        name = [var_name for var_name, var_val in callers_local_vars if var_val is var1]
        print(f'#####################> {name} = {var1}')

    if var2 is not None:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        name = [var_name for var_name, var_val in callers_local_vars if var_val is var2]
        print(f'#####################> {name} = {var2}')

    if var3 is not None:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        name = [var_name for var_name, var_val in callers_local_vars if var_val is var3]
        print(f'#####################> {name} = {var3}')

    if var4 is not None:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        name = [var_name for var_name, var_val in callers_local_vars if var_val is var4]
        print(f'#####################> {name} = {var4}')
    print("#####################> all videos : ")
    print(glob.glob('*.mp4'))
    print("#####################> all files : ")
    print(glob.glob('*'))

    print("#####################> ", text)
    print("#####################> State finish <###################################")
