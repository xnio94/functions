from importlib import import_module


def dynamic_import(function):
    tmp_functions = 'tmp_functions'  # 'a' + str(random.random())[5:10]
    mod = import_module(tmp_functions + '.' + function)
    return getattr(mod, function)
