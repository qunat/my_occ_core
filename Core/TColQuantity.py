# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
TColQuantity module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_tcolquantity.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _TColQuantity
else:
    import _TColQuantity

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _TColQuantity.SWIG_PyInstanceMethod_New
_swig_new_static_method = _TColQuantity.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _TColQuantity.delete_SwigPyIterator
    value = _swig_new_instance_method(_TColQuantity.SwigPyIterator_value)
    incr = _swig_new_instance_method(_TColQuantity.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_TColQuantity.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_TColQuantity.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_TColQuantity.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_TColQuantity.SwigPyIterator_copy)
    next = _swig_new_instance_method(_TColQuantity.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_TColQuantity.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_TColQuantity.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_TColQuantity.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _TColQuantity:
_TColQuantity.SwigPyIterator_swigregister(SwigPyIterator)


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
Handle_TColQuantity_HArray1OfLength_Create = _TColQuantity.Handle_TColQuantity_HArray1OfLength_Create
Handle_TColQuantity_HArray1OfLength_DownCast = _TColQuantity.Handle_TColQuantity_HArray1OfLength_DownCast
Handle_TColQuantity_HArray1OfLength_IsNull = _TColQuantity.Handle_TColQuantity_HArray1OfLength_IsNull
Handle_TColQuantity_HArray2OfLength_Create = _TColQuantity.Handle_TColQuantity_HArray2OfLength_Create
Handle_TColQuantity_HArray2OfLength_DownCast = _TColQuantity.Handle_TColQuantity_HArray2OfLength_DownCast
Handle_TColQuantity_HArray2OfLength_IsNull = _TColQuantity.Handle_TColQuantity_HArray2OfLength_IsNull
class TColQuantity_Array1OfLength(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_begin)
    end = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_end)
    cbegin = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_cbegin)
    cend = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_cend)

    def __init__(self, *args):
        _TColQuantity.TColQuantity_Array1OfLength_swiginit(self, _TColQuantity.new_TColQuantity_Array1OfLength(*args))
    Init = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Init)
    Size = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Size)
    Length = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Length)
    IsEmpty = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_IsEmpty)
    Lower = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Lower)
    Upper = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Upper)
    IsDeletable = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_IsDeletable)
    IsAllocated = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_IsAllocated)
    Assign = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Assign)
    Move = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Move)
    Set = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Set)
    First = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_First)
    ChangeFirst = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_ChangeFirst)
    Last = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Last)
    ChangeLast = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_ChangeLast)
    Value = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Value)
    ChangeValue = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_ChangeValue)
    __call__ = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength___call__)
    SetValue = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_SetValue)
    Resize = _swig_new_instance_method(_TColQuantity.TColQuantity_Array1OfLength_Resize)
    __swig_destroy__ = _TColQuantity.delete_TColQuantity_Array1OfLength

    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next


# Register TColQuantity_Array1OfLength in _TColQuantity:
_TColQuantity.TColQuantity_Array1OfLength_swigregister(TColQuantity_Array1OfLength)

class TColQuantity_Array2OfLength(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TColQuantity.TColQuantity_Array2OfLength_swiginit(self, _TColQuantity.new_TColQuantity_Array2OfLength(*args))
    Init = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Init)
    Size = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Size)
    Length = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Length)
    NbRows = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_NbRows)
    NbColumns = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_NbColumns)
    RowLength = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_RowLength)
    ColLength = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_ColLength)
    LowerRow = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_LowerRow)
    UpperRow = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_UpperRow)
    LowerCol = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_LowerCol)
    UpperCol = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_UpperCol)
    IsDeletable = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_IsDeletable)
    Assign = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Assign)
    Move = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Move)
    Set = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Set)
    Value = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Value)
    ChangeValue = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_ChangeValue)
    __call__ = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength___call__)
    SetValue = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_SetValue)
    Resize = _swig_new_instance_method(_TColQuantity.TColQuantity_Array2OfLength_Resize)
    __swig_destroy__ = _TColQuantity.delete_TColQuantity_Array2OfLength

# Register TColQuantity_Array2OfLength in _TColQuantity:
_TColQuantity.TColQuantity_Array2OfLength_swigregister(TColQuantity_Array2OfLength)

class TColQuantity_HArray1OfLength(TColQuantity_Array1OfLength, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TColQuantity.TColQuantity_HArray1OfLength_swiginit(self, _TColQuantity.new_TColQuantity_HArray1OfLength(*args))
    Array1 = _swig_new_instance_method(_TColQuantity.TColQuantity_HArray1OfLength_Array1)
    ChangeArray1 = _swig_new_instance_method(_TColQuantity.TColQuantity_HArray1OfLength_ChangeArray1)


    @staticmethod
    def DownCast(t):
      return Handle_TColQuantity_HArray1OfLength_DownCast(t)

    __swig_destroy__ = _TColQuantity.delete_TColQuantity_HArray1OfLength

# Register TColQuantity_HArray1OfLength in _TColQuantity:
_TColQuantity.TColQuantity_HArray1OfLength_swigregister(TColQuantity_HArray1OfLength)

class TColQuantity_HArray2OfLength(TColQuantity_Array2OfLength, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _TColQuantity.TColQuantity_HArray2OfLength_swiginit(self, _TColQuantity.new_TColQuantity_HArray2OfLength(*args))
    Array2 = _swig_new_instance_method(_TColQuantity.TColQuantity_HArray2OfLength_Array2)
    ChangeArray2 = _swig_new_instance_method(_TColQuantity.TColQuantity_HArray2OfLength_ChangeArray2)


    @staticmethod
    def DownCast(t):
      return Handle_TColQuantity_HArray2OfLength_DownCast(t)

    __swig_destroy__ = _TColQuantity.delete_TColQuantity_HArray2OfLength

# Register TColQuantity_HArray2OfLength in _TColQuantity:
_TColQuantity.TColQuantity_HArray2OfLength_swigregister(TColQuantity_HArray2OfLength)



