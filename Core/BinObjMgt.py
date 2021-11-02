# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BinObjMgt module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_binobjmgt.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BinObjMgt
else:
    import _BinObjMgt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BinObjMgt.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BinObjMgt.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BinObjMgt.delete_SwigPyIterator
    value = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BinObjMgt.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BinObjMgt.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BinObjMgt:
_BinObjMgt.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TDF
import OCC.Core.Storage
class BinObjMgt_Persistent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor
        	:rtype: None
        """
        _BinObjMgt.BinObjMgt_Persistent_swiginit(self, _BinObjMgt.new_BinObjMgt_Persistent(*args))
    Destroy = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Destroy)
    GetAsciiString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetAsciiString)
    GetBoolean = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetBoolean)
    GetByte = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetByte)
    GetByteArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetByteArray)
    GetCharArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetCharArray)
    GetCharacter = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetCharacter)
    GetExtCharArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetExtCharArray)
    GetExtCharacter = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetExtCharacter)
    GetExtendedString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetExtendedString)
    GetGUID = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetGUID)
    GetIntArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetIntArray)
    GetInteger = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetInteger)
    GetLabel = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetLabel)
    GetReal = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetReal)
    GetRealArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetRealArray)
    GetShortReal = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetShortReal)
    GetShortRealArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_GetShortRealArray)
    Id = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Id)
    Init = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Init)
    IsError = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_IsError)
    IsOK = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_IsOK)
    Length = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Length)
    Position = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Position)
    PutAsciiString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutAsciiString)
    PutBoolean = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutBoolean)
    PutByte = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutByte)
    PutByteArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutByteArray)
    PutCString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutCString)
    PutCharArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutCharArray)
    PutCharacter = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutCharacter)
    PutExtCharArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutExtCharArray)
    PutExtCharacter = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutExtCharacter)
    PutExtendedString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutExtendedString)
    PutGUID = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutGUID)
    PutIntArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutIntArray)
    PutInteger = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutInteger)
    PutLabel = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutLabel)
    PutReal = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutReal)
    PutRealArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutRealArray)
    PutShortReal = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutShortReal)
    PutShortRealArray = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_PutShortRealArray)
    ReadFromString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_ReadFromString)
    SetId = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_SetId)
    SetPosition = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_SetPosition)
    SetTypeId = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_SetTypeId)
    Truncate = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_Truncate)
    TypeId = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_TypeId)
    WriteToString = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent_WriteToString)
    __rshift__ = _swig_new_instance_method(_BinObjMgt.BinObjMgt_Persistent___rshift__)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinObjMgt.delete_BinObjMgt_Persistent

# Register BinObjMgt_Persistent in _BinObjMgt:
_BinObjMgt.BinObjMgt_Persistent_swigregister(BinObjMgt_Persistent)

class BinObjMgt_RRelocationTable(OCC.Core.TColStd.TColStd_DataMapOfIntegerTransient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Clear = _swig_new_instance_method(_BinObjMgt.BinObjMgt_RRelocationTable_Clear)
    GetHeaderData = _swig_new_instance_method(_BinObjMgt.BinObjMgt_RRelocationTable_GetHeaderData)
    SetHeaderData = _swig_new_instance_method(_BinObjMgt.BinObjMgt_RRelocationTable_SetHeaderData)

    __repr__ = _dumps_object


    def __init__(self):
        _BinObjMgt.BinObjMgt_RRelocationTable_swiginit(self, _BinObjMgt.new_BinObjMgt_RRelocationTable())
    __swig_destroy__ = _BinObjMgt.delete_BinObjMgt_RRelocationTable

# Register BinObjMgt_RRelocationTable in _BinObjMgt:
_BinObjMgt.BinObjMgt_RRelocationTable_swigregister(BinObjMgt_RRelocationTable)


