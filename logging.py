import glob
import inspect


def name_of(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


def log_state(text, *args):
    print("#####################> ", text)
    for i in range(len(args)):
        print(f'#####################> {name_of(args[i])} = {args[i]}')

    print("#####################> all videos : ")
    print(glob.glob('*.mp4'))
    print("#####################> all files : ")
    print(glob.glob('*'))
