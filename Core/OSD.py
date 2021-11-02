# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
OSD module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_osd.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _OSD
else:
    import _OSD

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _OSD.SWIG_PyInstanceMethod_New
_swig_new_static_method = _OSD.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _OSD.delete_SwigPyIterator
    value = _swig_new_instance_method(_OSD.SwigPyIterator_value)
    incr = _swig_new_instance_method(_OSD.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_OSD.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_OSD.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_OSD.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_OSD.SwigPyIterator_copy)
    next = _swig_new_instance_method(_OSD.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_OSD.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_OSD.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_OSD.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_OSD.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_OSD.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_OSD.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_OSD.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_OSD.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_OSD.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _OSD:
_OSD.SwigPyIterator_swigregister(SwigPyIterator)


def _dumps_object(klass):
    """ Overwrite default string output for any wrapped object.
    By default, __repr__ method returns something like:
    <OCC.Core.TopoDS.TopoDS_Shape; proxy of <Swig Object of type 'TopoDS_Shape *' at 0x02BB0758> >
    This is too much verbose.
    We prefer :
    <class 'gp_Pnt'>
    or
    <class 'TopoDS_Shape'>
    """
    klass_name = str(klass.__class__).split(".")[3].split("'")[0]
    repr_string = "<class '" + klass_name + "'"
# for TopoDS_Shape, we also look for the base type
    if klass_name == "TopoDS_Shape":
        if klass.IsNull():
            repr_string += ": Null>"
            return repr_string
        st = klass.ShapeType()
        types = {OCC.Core.TopAbs.TopAbs_VERTEX: "Vertex",
                 OCC.Core.TopAbs.TopAbs_SOLID: "Solid",
                 OCC.Core.TopAbs.TopAbs_EDGE: "Edge",
                 OCC.Core.TopAbs.TopAbs_FACE: "Face",
                 OCC.Core.TopAbs.TopAbs_SHELL: "Shell",
                 OCC.Core.TopAbs.TopAbs_WIRE: "Wire",
                 OCC.Core.TopAbs.TopAbs_COMPOUND: "Compound",
                 OCC.Core.TopAbs.TopAbs_COMPSOLID: "Compsolid"}
        repr_string += "; Type:%s" % types[st]        
    elif hasattr(klass, "IsNull"):
        if klass.IsNull():
            repr_string += "; Null"
    repr_string += ">"
    return repr_string


from six import with_metaclass
import warnings
from OCC.Wrapper.wrapper_utils import Proxy, deprecated

import OCC.Core.Standard
import OCC.Core.NCollection
import OCC.Core.TCollection
OSD_NoLock = _OSD.OSD_NoLock
OSD_ReadLock = _OSD.OSD_ReadLock
OSD_WriteLock = _OSD.OSD_WriteLock
OSD_ExclusiveLock = _OSD.OSD_ExclusiveLock
OSD_RTLD_LAZY = _OSD.OSD_RTLD_LAZY
OSD_RTLD_NOW = _OSD.OSD_RTLD_NOW
OSD_ReadOnly = _OSD.OSD_ReadOnly
OSD_WriteOnly = _OSD.OSD_WriteOnly
OSD_ReadWrite = _OSD.OSD_ReadWrite
OSD_Unavailable = _OSD.OSD_Unavailable
OSD_SUN = _OSD.OSD_SUN
OSD_DEC = _OSD.OSD_DEC
OSD_SGI = _OSD.OSD_SGI
OSD_NEC = _OSD.OSD_NEC
OSD_MAC = _OSD.OSD_MAC
OSD_PC = _OSD.OSD_PC
OSD_HP = _OSD.OSD_HP
OSD_IBM = _OSD.OSD_IBM
OSD_VAX = _OSD.OSD_VAX
OSD_LIN = _OSD.OSD_LIN
OSD_AIX = _OSD.OSD_AIX
OSD_WDirectory = _OSD.OSD_WDirectory
OSD_WDirectoryIterator = _OSD.OSD_WDirectoryIterator
OSD_WEnvironment = _OSD.OSD_WEnvironment
OSD_WFile = _OSD.OSD_WFile
OSD_WFileNode = _OSD.OSD_WFileNode
OSD_WFileIterator = _OSD.OSD_WFileIterator
OSD_WPath = _OSD.OSD_WPath
OSD_WProcess = _OSD.OSD_WProcess
OSD_WProtection = _OSD.OSD_WProtection
OSD_WHost = _OSD.OSD_WHost
OSD_WDisk = _OSD.OSD_WDisk
OSD_WChronometer = _OSD.OSD_WChronometer
OSD_WTimer = _OSD.OSD_WTimer
OSD_WPackage = _OSD.OSD_WPackage
OSD_WEnvironmentIterator = _OSD.OSD_WEnvironmentIterator
OSD_Unknown = _OSD.OSD_Unknown
OSD_Default = _OSD.OSD_Default
OSD_UnixBSD = _OSD.OSD_UnixBSD
OSD_UnixSystemV = _OSD.OSD_UnixSystemV
OSD_VMS = _OSD.OSD_VMS
OSD_OS2 = _OSD.OSD_OS2
OSD_OSF = _OSD.OSD_OSF
OSD_MacOs = _OSD.OSD_MacOs
OSD_Taligent = _OSD.OSD_Taligent
OSD_WindowsNT = _OSD.OSD_WindowsNT
OSD_LinuxREDHAT = _OSD.OSD_LinuxREDHAT
OSD_Aix = _OSD.OSD_Aix
OSD_FILE = _OSD.OSD_FILE
OSD_DIRECTORY = _OSD.OSD_DIRECTORY
OSD_LINK = _OSD.OSD_LINK
OSD_SOCKET = _OSD.OSD_SOCKET
OSD_UNKNOWN = _OSD.OSD_UNKNOWN
OSD_SignalMode_AsIs = _OSD.OSD_SignalMode_AsIs
OSD_SignalMode_Set = _OSD.OSD_SignalMode_Set
OSD_SignalMode_SetUnhandled = _OSD.OSD_SignalMode_SetUnhandled
OSD_SignalMode_Unset = _OSD.OSD_SignalMode_Unset
OSD_FromBeginning = _OSD.OSD_FromBeginning
OSD_FromHere = _OSD.OSD_FromHere
OSD_FromEnd = _OSD.OSD_FromEnd
OSD_None = _OSD.OSD_None
OSD_R = _OSD.OSD_R
OSD_W = _OSD.OSD_W
OSD_RW = _OSD.OSD_RW
OSD_X = _OSD.OSD_X
OSD_RX = _OSD.OSD_RX
OSD_WX = _OSD.OSD_WX
OSD_RWX = _OSD.OSD_RWX
OSD_D = _OSD.OSD_D
OSD_RD = _OSD.OSD_RD
OSD_WD = _OSD.OSD_WD
OSD_RWD = _OSD.OSD_RWD
OSD_XD = _OSD.OSD_XD
OSD_RXD = _OSD.OSD_RXD
OSD_WXD = _OSD.OSD_WXD
OSD_RWXD = _OSD.OSD_RWXD

