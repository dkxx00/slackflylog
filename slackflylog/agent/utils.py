import sys
import traceback

PY2 = sys.version_info[0] == 2

if not PY2:
    string_types = (str, )
else:
    string_types = (str, unicode)


def import_string(import_name, silent=False):
    import_name = str(import_name).replace(':', '.')
    try:
        try:
            __import__(import_name)
        except ImportError:
            if '.' not in import_name:
                raise
        else:
            return sys.modules[import_name]

        module_name, obj_name = import_name.rsplit('.', 1)
        try:
            module = __import__(module_name, None, None, [obj_name])
        except ImportError:
            module = import_string(module_name)

        try:
            return getattr(module, obj_name)
        except AttributeError as e:
            raise ImportError(e)

    except ImportError as e:
        if not silent:
            # Use 'with_traceback()' method for Python 3
            if PY2:
                t, v, tb = sys.exc_info()
                raise t, v, tb
            else:
                raise ImportError(e).with_traceback(sys.exc_info()[2])