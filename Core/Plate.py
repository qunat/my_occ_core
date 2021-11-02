# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Plate module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_plate.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Plate
else:
    import _Plate

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Plate.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Plate.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Plate.delete_SwigPyIterator
    value = _swig_new_instance_method(_Plate.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Plate.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Plate.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Plate.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Plate.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Plate.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Plate.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Plate.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Plate.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Plate.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Plate.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Plate.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Plate.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Plate.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Plate.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Plate.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Plate:
_Plate.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.gp
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Message
Handle_Plate_HArray1OfPinpointConstraint_Create = _Plate.Handle_Plate_HArray1OfPinpointConstraint_Create
Handle_Plate_HArray1OfPinpointConstraint_DownCast = _Plate.Handle_Plate_HArray1OfPinpointConstraint_DownCast
Handle_Plate_HArray1OfPinpointConstraint_IsNull = _Plate.Handle_Plate_HArray1OfPinpointConstraint_IsNull
class Plate_Array1OfPinpointConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_begin)
    end = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_end)
    cbegin = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_cbegin)
    cend = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_cend)

    def __init__(self, *args):
        _Plate.Plate_Array1OfPinpointConstraint_swiginit(self, _Plate.new_Plate_Array1OfPinpointConstraint(*args))
    Init = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Init)
    Size = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Size)
    Length = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Length)
    IsEmpty = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_IsEmpty)
    Lower = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Lower)
    Upper = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Upper)
    IsDeletable = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_IsDeletable)
    IsAllocated = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_IsAllocated)
    Assign = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Assign)
    Move = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Move)
    Set = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Set)
    First = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_First)
    ChangeFirst = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_ChangeFirst)
    Last = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Last)
    ChangeLast = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_ChangeLast)
    Value = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Value)
    ChangeValue = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_ChangeValue)
    __call__ = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint___call__)
    SetValue = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_SetValue)
    Resize = _swig_new_instance_method(_Plate.Plate_Array1OfPinpointConstraint_Resize)
    __swig_destroy__ = _Plate.delete_Plate_Array1OfPinpointConstraint

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


# Register Plate_Array1OfPinpointConstraint in _Plate:
_Plate.Plate_Array1OfPinpointConstraint_swigregister(Plate_Array1OfPinpointConstraint)

class Plate_SequenceOfPinpointConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_begin)
    end = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_end)
    cbegin = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_cbegin)
    cend = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_cend)

    def __init__(self, *args):
        _Plate.Plate_SequenceOfPinpointConstraint_swiginit(self, _Plate.new_Plate_SequenceOfPinpointConstraint(*args))
    Size = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Size)
    Length = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Length)
    Lower = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Lower)
    Upper = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Upper)
    IsEmpty = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_IsEmpty)
    Reverse = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Reverse)
    Exchange = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Exchange)
    delNode = _swig_new_static_method(_Plate.Plate_SequenceOfPinpointConstraint_delNode)
    Clear = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Clear)
    Assign = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Assign)
    Set = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Set)
    Remove = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Remove)
    Append = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Append)
    Prepend = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Prepend)
    InsertBefore = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_InsertBefore)
    InsertAfter = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_InsertAfter)
    Split = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Split)
    First = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_First)
    ChangeFirst = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_ChangeFirst)
    Last = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Last)
    ChangeLast = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_ChangeLast)
    Value = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_Value)
    ChangeValue = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_ChangeValue)
    __call__ = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint___call__)
    SetValue = _swig_new_instance_method(_Plate.Plate_SequenceOfPinpointConstraint_SetValue)
    __swig_destroy__ = _Plate.delete_Plate_SequenceOfPinpointConstraint

# Register Plate_SequenceOfPinpointConstraint in _Plate:
_Plate.Plate_SequenceOfPinpointConstraint_swigregister(Plate_SequenceOfPinpointConstraint)
Plate_SequenceOfPinpointConstraint_delNode = _Plate.Plate_SequenceOfPinpointConstraint_delNode

class Plate_SequenceOfLinearXYZConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_begin)
    end = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_end)
    cbegin = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_cbegin)
    cend = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_cend)

    def __init__(self, *args):
        _Plate.Plate_SequenceOfLinearXYZConstraint_swiginit(self, _Plate.new_Plate_SequenceOfLinearXYZConstraint(*args))
    Size = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Size)
    Length = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Length)
    Lower = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Lower)
    Upper = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Upper)
    IsEmpty = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_IsEmpty)
    Reverse = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Reverse)
    Exchange = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Exchange)
    delNode = _swig_new_static_method(_Plate.Plate_SequenceOfLinearXYZConstraint_delNode)
    Clear = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Clear)
    Assign = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Assign)
    Set = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Set)
    Remove = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Remove)
    Append = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Append)
    Prepend = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Prepend)
    InsertBefore = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_InsertBefore)
    InsertAfter = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_InsertAfter)
    Split = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Split)
    First = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_First)
    ChangeFirst = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_ChangeFirst)
    Last = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Last)
    ChangeLast = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_ChangeLast)
    Value = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_Value)
    ChangeValue = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_ChangeValue)
    __call__ = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint___call__)
    SetValue = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearXYZConstraint_SetValue)
    __swig_destroy__ = _Plate.delete_Plate_SequenceOfLinearXYZConstraint

# Register Plate_SequenceOfLinearXYZConstraint in _Plate:
_Plate.Plate_SequenceOfLinearXYZConstraint_swigregister(Plate_SequenceOfLinearXYZConstraint)
Plate_SequenceOfLinearXYZConstraint_delNode = _Plate.Plate_SequenceOfLinearXYZConstraint_delNode

class Plate_SequenceOfLinearScalarConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_begin)
    end = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_end)
    cbegin = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_cbegin)
    cend = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_cend)

    def __init__(self, *args):
        _Plate.Plate_SequenceOfLinearScalarConstraint_swiginit(self, _Plate.new_Plate_SequenceOfLinearScalarConstraint(*args))
    Size = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Size)
    Length = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Length)
    Lower = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Lower)
    Upper = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Upper)
    IsEmpty = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_IsEmpty)
    Reverse = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Reverse)
    Exchange = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Exchange)
    delNode = _swig_new_static_method(_Plate.Plate_SequenceOfLinearScalarConstraint_delNode)
    Clear = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Clear)
    Assign = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Assign)
    Set = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Set)
    Remove = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Remove)
    Append = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Append)
    Prepend = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Prepend)
    InsertBefore = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_InsertBefore)
    InsertAfter = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_InsertAfter)
    Split = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Split)
    First = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_First)
    ChangeFirst = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_ChangeFirst)
    Last = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Last)
    ChangeLast = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_ChangeLast)
    Value = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_Value)
    ChangeValue = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_ChangeValue)
    __call__ = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint___call__)
    SetValue = _swig_new_instance_method(_Plate.Plate_SequenceOfLinearScalarConstraint_SetValue)
    __swig_destroy__ = _Plate.delete_Plate_SequenceOfLinearScalarConstraint

# Register Plate_SequenceOfLinearScalarConstraint in _Plate:
_Plate.Plate_SequenceOfLinearScalarConstraint_swigregister(Plate_SequenceOfLinearScalarConstraint)
Plate_SequenceOfLinearScalarConstraint_delNode = _Plate.Plate_SequenceOfLinearScalarConstraint_delNode

class Plate_D1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DU = _swig_new_instance_method(_Plate.Plate_D1_DU)
    DV = _swig_new_instance_method(_Plate.Plate_D1_DV)

    def __init__(self, *args):
        r"""
        :param du:
        	:type du: gp_XYZ
        	:param dv:
        	:type dv: gp_XYZ
        	:rtype: None:param ref:
        	:type ref: Plate_D1
        	:rtype: None
        """
        _Plate.Plate_D1_swiginit(self, _Plate.new_Plate_D1(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_D1

# Register Plate_D1 in _Plate:
_Plate.Plate_D1_swigregister(Plate_D1)

class Plate_D2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param duu:
        	:type duu: gp_XYZ
        	:param duv:
        	:type duv: gp_XYZ
        	:param dvv:
        	:type dvv: gp_XYZ
        	:rtype: None:param ref:
        	:type ref: Plate_D2
        	:rtype: None
        """
        _Plate.Plate_D2_swiginit(self, _Plate.new_Plate_D2(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_D2

# Register Plate_D2 in _Plate:
_Plate.Plate_D2_swigregister(Plate_D2)

class Plate_D3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param duuu:
        	:type duuu: gp_XYZ
        	:param duuv:
        	:type duuv: gp_XYZ
        	:param duvv:
        	:type duvv: gp_XYZ
        	:param dvvv:
        	:type dvvv: gp_XYZ
        	:rtype: None:param ref:
        	:type ref: Plate_D3
        	:rtype: None
        """
        _Plate.Plate_D3_swiginit(self, _Plate.new_Plate_D3(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_D3

# Register Plate_D3 in _Plate:
_Plate.Plate_D3_swigregister(Plate_D3)

class Plate_FreeGtoCConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetPPC = _swig_new_instance_method(_Plate.Plate_FreeGtoCConstraint_GetPPC)
    LSC = _swig_new_instance_method(_Plate.Plate_FreeGtoCConstraint_LSC)

    def __init__(self, *args):
        r"""
        :param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param IncrementalLoad: default value is 1.0
        	:type IncrementalLoad: float
        	:param orientation: default value is 0
        	:type orientation: int
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:param IncrementalLoad: default value is 1.0
        	:type IncrementalLoad: float
        	:param orientation: default value is 0
        	:type orientation: int
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:param D3S:
        	:type D3S: Plate_D3
        	:param D3T:
        	:type D3T: Plate_D3
        	:param IncrementalLoad: default value is 1.0
        	:type IncrementalLoad: float
        	:param orientation: default value is 0
        	:type orientation: int
        	:rtype: None
        """
        _Plate.Plate_FreeGtoCConstraint_swiginit(self, _Plate.new_Plate_FreeGtoCConstraint(*args))
    nb_LSC = _swig_new_instance_method(_Plate.Plate_FreeGtoCConstraint_nb_LSC)
    nb_PPC = _swig_new_instance_method(_Plate.Plate_FreeGtoCConstraint_nb_PPC)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_FreeGtoCConstraint

# Register Plate_FreeGtoCConstraint in _Plate:
_Plate.Plate_FreeGtoCConstraint_swigregister(Plate_FreeGtoCConstraint)

class Plate_GlobalTranslationConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    LXYZC = _swig_new_instance_method(_Plate.Plate_GlobalTranslationConstraint_LXYZC)

    def __init__(self, *args):
        r"""
        :param SOfXY:
        	:type SOfXY: TColgp_SequenceOfXY
        	:rtype: None
        """
        _Plate.Plate_GlobalTranslationConstraint_swiginit(self, _Plate.new_Plate_GlobalTranslationConstraint(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_GlobalTranslationConstraint

# Register Plate_GlobalTranslationConstraint in _Plate:
_Plate.Plate_GlobalTranslationConstraint_swigregister(Plate_GlobalTranslationConstraint)

class Plate_GtoCConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    D1SurfInit = _swig_new_instance_method(_Plate.Plate_GtoCConstraint_D1SurfInit)
    GetPPC = _swig_new_instance_method(_Plate.Plate_GtoCConstraint_GetPPC)

    def __init__(self, *args):
        r"""
        :param ref:
        	:type ref: Plate_GtoCConstraint
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param nP:
        	:type nP: gp_XYZ
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:param nP:
        	:type nP: gp_XYZ
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:param D3S:
        	:type D3S: Plate_D3
        	:param D3T:
        	:type D3T: Plate_D3
        	:rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param D1S:
        	:type D1S: Plate_D1
        	:param D1T:
        	:type D1T: Plate_D1
        	:param D2S:
        	:type D2S: Plate_D2
        	:param D2T:
        	:type D2T: Plate_D2
        	:param D3S:
        	:type D3S: Plate_D3
        	:param D3T:
        	:type D3T: Plate_D3
        	:param nP:
        	:type nP: gp_XYZ
        	:rtype: None
        """
        _Plate.Plate_GtoCConstraint_swiginit(self, _Plate.new_Plate_GtoCConstraint(*args))
    nb_PPC = _swig_new_instance_method(_Plate.Plate_GtoCConstraint_nb_PPC)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_GtoCConstraint

# Register Plate_GtoCConstraint in _Plate:
_Plate.Plate_GtoCConstraint_swigregister(Plate_GtoCConstraint)

class Plate_LineConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    LSC = _swig_new_instance_method(_Plate.Plate_LineConstraint_LSC)

    def __init__(self, *args):
        r"""
        :param point2d:
        	:type point2d: gp_XY
        	:param lin:
        	:type lin: gp_Lin
        	:param iu: default value is 0
        	:type iu: int
        	:param iv: default value is 0
        	:type iv: int
        	:rtype: None
        """
        _Plate.Plate_LineConstraint_swiginit(self, _Plate.new_Plate_LineConstraint(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_LineConstraint

# Register Plate_LineConstraint in _Plate:
_Plate.Plate_LineConstraint_swigregister(Plate_LineConstraint)

class Plate_LinearScalarConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Coeff = _swig_new_instance_method(_Plate.Plate_LinearScalarConstraint_Coeff)
    GetPPC = _swig_new_instance_method(_Plate.Plate_LinearScalarConstraint_GetPPC)

    def __init__(self, *args):
        r"""
        :rtype: None:param thePPC1:
        	:type thePPC1: Plate_PinpointConstraint
        	:param theCoeff:
        	:type theCoeff: gp_XYZ
        	:rtype: None:param thePPC:
        	:type thePPC: Plate_Array1OfPinpointConstraint
        	:param theCoeff:
        	:type theCoeff: TColgp_Array1OfXYZ
        	:rtype: None:param thePPC:
        	:type thePPC: Plate_Array1OfPinpointConstraint
        	:param theCoeff:
        	:type theCoeff: TColgp_Array2OfXYZ
        	:rtype: None:param ColLen:
        	:type ColLen: int
        	:param RowLen:
        	:type RowLen: int
        	:rtype: None
        """
        _Plate.Plate_LinearScalarConstraint_swiginit(self, _Plate.new_Plate_LinearScalarConstraint(*args))
    SetCoeff = _swig_new_instance_method(_Plate.Plate_LinearScalarConstraint_SetCoeff)
    SetPPC = _swig_new_instance_method(_Plate.Plate_LinearScalarConstraint_SetPPC)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_LinearScalarConstraint

# Register Plate_LinearScalarConstraint in _Plate:
_Plate.Plate_LinearScalarConstraint_swigregister(Plate_LinearScalarConstraint)

class Plate_LinearXYZConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Coeff = _swig_new_instance_method(_Plate.Plate_LinearXYZConstraint_Coeff)
    GetPPC = _swig_new_instance_method(_Plate.Plate_LinearXYZConstraint_GetPPC)

    def __init__(self, *args):
        r"""
        :rtype: None:param thePPC:
        	:type thePPC: Plate_Array1OfPinpointConstraint
        	:param theCoeff:
        	:type theCoeff: TColStd_Array1OfReal
        	:rtype: None:param thePPC:
        	:type thePPC: Plate_Array1OfPinpointConstraint
        	:param theCoeff:
        	:type theCoeff: TColStd_Array2OfReal
        	:rtype: None:param ColLen:
        	:type ColLen: int
        	:param RowLen:
        	:type RowLen: int
        	:rtype: None
        """
        _Plate.Plate_LinearXYZConstraint_swiginit(self, _Plate.new_Plate_LinearXYZConstraint(*args))
    SetCoeff = _swig_new_instance_method(_Plate.Plate_LinearXYZConstraint_SetCoeff)
    SetPPC = _swig_new_instance_method(_Plate.Plate_LinearXYZConstraint_SetPPC)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_LinearXYZConstraint

# Register Plate_LinearXYZConstraint in _Plate:
_Plate.Plate_LinearXYZConstraint_swigregister(Plate_LinearXYZConstraint)

class Plate_PinpointConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Idu = _swig_new_instance_method(_Plate.Plate_PinpointConstraint_Idu)
    Idv = _swig_new_instance_method(_Plate.Plate_PinpointConstraint_Idv)

    def __init__(self, *args):
        r"""
        :rtype: None:param point2d:
        	:type point2d: gp_XY
        	:param ImposedValue:
        	:type ImposedValue: gp_XYZ
        	:param iu: default value is 0
        	:type iu: int
        	:param iv: default value is 0
        	:type iv: int
        	:rtype: None
        """
        _Plate.Plate_PinpointConstraint_swiginit(self, _Plate.new_Plate_PinpointConstraint(*args))
    Pnt2d = _swig_new_instance_method(_Plate.Plate_PinpointConstraint_Pnt2d)
    Value = _swig_new_instance_method(_Plate.Plate_PinpointConstraint_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_PinpointConstraint

# Register Plate_PinpointConstraint in _Plate:
_Plate.Plate_PinpointConstraint_swigregister(Plate_PinpointConstraint)

class Plate_PlaneConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    LSC = _swig_new_instance_method(_Plate.Plate_PlaneConstraint_LSC)

    def __init__(self, *args):
        r"""
        :param point2d:
        	:type point2d: gp_XY
        	:param pln:
        	:type pln: gp_Pln
        	:param iu: default value is 0
        	:type iu: int
        	:param iv: default value is 0
        	:type iv: int
        	:rtype: None
        """
        _Plate.Plate_PlaneConstraint_swiginit(self, _Plate.new_Plate_PlaneConstraint(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_PlaneConstraint

# Register Plate_PlaneConstraint in _Plate:
_Plate.Plate_PlaneConstraint_swigregister(Plate_PlaneConstraint)

class Plate_Plate(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CoefPol = _swig_new_instance_method(_Plate.Plate_Plate_CoefPol)
    Continuity = _swig_new_instance_method(_Plate.Plate_Plate_Continuity)
    Copy = _swig_new_instance_method(_Plate.Plate_Plate_Copy)
    Evaluate = _swig_new_instance_method(_Plate.Plate_Plate_Evaluate)
    EvaluateDerivative = _swig_new_instance_method(_Plate.Plate_Plate_EvaluateDerivative)
    Init = _swig_new_instance_method(_Plate.Plate_Plate_Init)
    IsDone = _swig_new_instance_method(_Plate.Plate_Plate_IsDone)
    Load = _swig_new_instance_method(_Plate.Plate_Plate_Load)

    def __init__(self, *args):
        r"""
        :rtype: None:param Ref:
        	:type Ref: Plate_Plate
        	:rtype: None
        """
        _Plate.Plate_Plate_swiginit(self, _Plate.new_Plate_Plate(*args))
    SetPolynomialPartOnly = _swig_new_instance_method(_Plate.Plate_Plate_SetPolynomialPartOnly)
    SolveTI = _swig_new_instance_method(_Plate.Plate_Plate_SolveTI)
    UVBox = _swig_new_instance_method(_Plate.Plate_Plate_UVBox)
    UVConstraints = _swig_new_instance_method(_Plate.Plate_Plate_UVConstraints)
    destroy = _swig_new_instance_method(_Plate.Plate_Plate_destroy)
    Set = _swig_new_instance_method(_Plate.Plate_Plate_Set)

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_Plate

# Register Plate_Plate in _Plate:
_Plate.Plate_Plate_swigregister(Plate_Plate)

class Plate_SampledCurveConstraint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    LXYZC = _swig_new_instance_method(_Plate.Plate_SampledCurveConstraint_LXYZC)

    def __init__(self, *args):
        r"""
        :param SOPPC:
        	:type SOPPC: Plate_SequenceOfPinpointConstraint
        	:param n:
        	:type n: int
        	:rtype: None
        """
        _Plate.Plate_SampledCurveConstraint_swiginit(self, _Plate.new_Plate_SampledCurveConstraint(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _Plate.delete_Plate_SampledCurveConstraint

# Register Plate_SampledCurveConstraint in _Plate:
_Plate.Plate_SampledCurveConstraint_swigregister(Plate_SampledCurveConstraint)

class Plate_HArray1OfPinpointConstraint(Plate_Array1OfPinpointConstraint, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Plate.Plate_HArray1OfPinpointConstraint_swiginit(self, _Plate.new_Plate_HArray1OfPinpointConstraint(*args))
    Array1 = _swig_new_instance_method(_Plate.Plate_HArray1OfPinpointConstraint_Array1)
    ChangeArray1 = _swig_new_instance_method(_Plate.Plate_HArray1OfPinpointConstraint_ChangeArray1)


    @staticmethod
    def DownCast(t):
      return Handle_Plate_HArray1OfPinpointConstraint_DownCast(t)

    __swig_destroy__ = _Plate.delete_Plate_HArray1OfPinpointConstraint

# Register Plate_HArray1OfPinpointConstraint in _Plate:
_Plate.Plate_HArray1OfPinpointConstraint_swigregister(Plate_HArray1OfPinpointConstraint)



