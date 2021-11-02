# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
MAT module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_mat.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _MAT
else:
    import _MAT

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _MAT.SWIG_PyInstanceMethod_New
_swig_new_static_method = _MAT.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _MAT.delete_SwigPyIterator
    value = _swig_new_instance_method(_MAT.SwigPyIterator_value)
    incr = _swig_new_instance_method(_MAT.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_MAT.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_MAT.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_MAT.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_MAT.SwigPyIterator_copy)
    next = _swig_new_instance_method(_MAT.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_MAT.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_MAT.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_MAT.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_MAT.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_MAT.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_MAT.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_MAT.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_MAT.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_MAT.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _MAT:
_MAT.SwigPyIterator_swigregister(SwigPyIterator)


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
MAT_Left = _MAT.MAT_Left
MAT_Right = _MAT.MAT_Right
Handle_MAT_Arc_Create = _MAT.Handle_MAT_Arc_Create
Handle_MAT_Arc_DownCast = _MAT.Handle_MAT_Arc_DownCast
Handle_MAT_Arc_IsNull = _MAT.Handle_MAT_Arc_IsNull
Handle_MAT_BasicElt_Create = _MAT.Handle_MAT_BasicElt_Create
Handle_MAT_BasicElt_DownCast = _MAT.Handle_MAT_BasicElt_DownCast
Handle_MAT_BasicElt_IsNull = _MAT.Handle_MAT_BasicElt_IsNull
Handle_MAT_Bisector_Create = _MAT.Handle_MAT_Bisector_Create
Handle_MAT_Bisector_DownCast = _MAT.Handle_MAT_Bisector_DownCast
Handle_MAT_Bisector_IsNull = _MAT.Handle_MAT_Bisector_IsNull
Handle_MAT_Edge_Create = _MAT.Handle_MAT_Edge_Create
Handle_MAT_Edge_DownCast = _MAT.Handle_MAT_Edge_DownCast
Handle_MAT_Edge_IsNull = _MAT.Handle_MAT_Edge_IsNull
Handle_MAT_Graph_Create = _MAT.Handle_MAT_Graph_Create
Handle_MAT_Graph_DownCast = _MAT.Handle_MAT_Graph_DownCast
Handle_MAT_Graph_IsNull = _MAT.Handle_MAT_Graph_IsNull
Handle_MAT_ListOfBisector_Create = _MAT.Handle_MAT_ListOfBisector_Create
Handle_MAT_ListOfBisector_DownCast = _MAT.Handle_MAT_ListOfBisector_DownCast
Handle_MAT_ListOfBisector_IsNull = _MAT.Handle_MAT_ListOfBisector_IsNull
Handle_MAT_ListOfEdge_Create = _MAT.Handle_MAT_ListOfEdge_Create
Handle_MAT_ListOfEdge_DownCast = _MAT.Handle_MAT_ListOfEdge_DownCast
Handle_MAT_ListOfEdge_IsNull = _MAT.Handle_MAT_ListOfEdge_IsNull
Handle_MAT_Node_Create = _MAT.Handle_MAT_Node_Create
Handle_MAT_Node_DownCast = _MAT.Handle_MAT_Node_DownCast
Handle_MAT_Node_IsNull = _MAT.Handle_MAT_Node_IsNull
Handle_MAT_TListNodeOfListOfBisector_Create = _MAT.Handle_MAT_TListNodeOfListOfBisector_Create
Handle_MAT_TListNodeOfListOfBisector_DownCast = _MAT.Handle_MAT_TListNodeOfListOfBisector_DownCast
Handle_MAT_TListNodeOfListOfBisector_IsNull = _MAT.Handle_MAT_TListNodeOfListOfBisector_IsNull
Handle_MAT_TListNodeOfListOfEdge_Create = _MAT.Handle_MAT_TListNodeOfListOfEdge_Create
Handle_MAT_TListNodeOfListOfEdge_DownCast = _MAT.Handle_MAT_TListNodeOfListOfEdge_DownCast
Handle_MAT_TListNodeOfListOfEdge_IsNull = _MAT.Handle_MAT_TListNodeOfListOfEdge_IsNull
Handle_MAT_Zone_Create = _MAT.Handle_MAT_Zone_Create
Handle_MAT_Zone_DownCast = _MAT.Handle_MAT_Zone_DownCast
Handle_MAT_Zone_IsNull = _MAT.Handle_MAT_Zone_IsNull
class MAT_DataMapOfIntegerArc(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_begin)
    end = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_cend)

    def __init__(self, *args):
        _MAT.MAT_DataMapOfIntegerArc_swiginit(self, _MAT.new_MAT_DataMapOfIntegerArc(*args))
    Exchange = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Exchange)
    Assign = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Set)
    ReSize = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_ReSize)
    Bind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Bind)
    Bound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Bound)
    IsBound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_IsBound)
    UnBind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_UnBind)
    Seek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Seek)
    Find = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Find)
    ChangeSeek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_ChangeFind)
    __call__ = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc___call__)
    Clear = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Clear)
    __swig_destroy__ = _MAT.delete_MAT_DataMapOfIntegerArc
    Size = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Size)
    Keys = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerArc_Keys)

# Register MAT_DataMapOfIntegerArc in _MAT:
_MAT.MAT_DataMapOfIntegerArc_swigregister(MAT_DataMapOfIntegerArc)

class MAT_DataMapOfIntegerBasicElt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_begin)
    end = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_cend)

    def __init__(self, *args):
        _MAT.MAT_DataMapOfIntegerBasicElt_swiginit(self, _MAT.new_MAT_DataMapOfIntegerBasicElt(*args))
    Exchange = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Exchange)
    Assign = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Set)
    ReSize = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_ReSize)
    Bind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Bind)
    Bound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Bound)
    IsBound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_IsBound)
    UnBind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_UnBind)
    Seek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Seek)
    Find = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Find)
    ChangeSeek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_ChangeFind)
    __call__ = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt___call__)
    Clear = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Clear)
    __swig_destroy__ = _MAT.delete_MAT_DataMapOfIntegerBasicElt
    Size = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Size)
    Keys = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBasicElt_Keys)

# Register MAT_DataMapOfIntegerBasicElt in _MAT:
_MAT.MAT_DataMapOfIntegerBasicElt_swigregister(MAT_DataMapOfIntegerBasicElt)

class MAT_SequenceOfBasicElt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_begin)
    end = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_cend)

    def __init__(self, *args):
        _MAT.MAT_SequenceOfBasicElt_swiginit(self, _MAT.new_MAT_SequenceOfBasicElt(*args))
    Size = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Size)
    Length = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Length)
    Lower = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Lower)
    Upper = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Upper)
    IsEmpty = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_IsEmpty)
    Reverse = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Reverse)
    Exchange = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Exchange)
    delNode = _swig_new_static_method(_MAT.MAT_SequenceOfBasicElt_delNode)
    Clear = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Clear)
    Assign = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Set)
    Remove = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Remove)
    Append = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Append)
    Prepend = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Prepend)
    InsertBefore = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_InsertBefore)
    InsertAfter = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_InsertAfter)
    Split = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Split)
    First = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_First)
    ChangeFirst = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_ChangeFirst)
    Last = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Last)
    ChangeLast = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_ChangeLast)
    Value = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_Value)
    ChangeValue = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_ChangeValue)
    __call__ = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt___call__)
    SetValue = _swig_new_instance_method(_MAT.MAT_SequenceOfBasicElt_SetValue)
    __swig_destroy__ = _MAT.delete_MAT_SequenceOfBasicElt

# Register MAT_SequenceOfBasicElt in _MAT:
_MAT.MAT_SequenceOfBasicElt_swigregister(MAT_SequenceOfBasicElt)
MAT_SequenceOfBasicElt_delNode = _MAT.MAT_SequenceOfBasicElt_delNode

class MAT_DataMapOfIntegerBisector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_begin)
    end = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_cend)

    def __init__(self, *args):
        _MAT.MAT_DataMapOfIntegerBisector_swiginit(self, _MAT.new_MAT_DataMapOfIntegerBisector(*args))
    Exchange = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Exchange)
    Assign = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Set)
    ReSize = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_ReSize)
    Bind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Bind)
    Bound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Bound)
    IsBound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_IsBound)
    UnBind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_UnBind)
    Seek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Seek)
    Find = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Find)
    ChangeSeek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_ChangeFind)
    __call__ = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector___call__)
    Clear = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Clear)
    __swig_destroy__ = _MAT.delete_MAT_DataMapOfIntegerBisector
    Size = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Size)
    Keys = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerBisector_Keys)

# Register MAT_DataMapOfIntegerBisector in _MAT:
_MAT.MAT_DataMapOfIntegerBisector_swigregister(MAT_DataMapOfIntegerBisector)

class MAT_SequenceOfArc(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_begin)
    end = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_cend)

    def __init__(self, *args):
        _MAT.MAT_SequenceOfArc_swiginit(self, _MAT.new_MAT_SequenceOfArc(*args))
    Size = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Size)
    Length = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Length)
    Lower = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Lower)
    Upper = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Upper)
    IsEmpty = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_IsEmpty)
    Reverse = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Reverse)
    Exchange = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Exchange)
    delNode = _swig_new_static_method(_MAT.MAT_SequenceOfArc_delNode)
    Clear = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Clear)
    Assign = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Set)
    Remove = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Remove)
    Append = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Append)
    Prepend = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Prepend)
    InsertBefore = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_InsertBefore)
    InsertAfter = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_InsertAfter)
    Split = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Split)
    First = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_First)
    ChangeFirst = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_ChangeFirst)
    Last = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Last)
    ChangeLast = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_ChangeLast)
    Value = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_Value)
    ChangeValue = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_ChangeValue)
    __call__ = _swig_new_instance_method(_MAT.MAT_SequenceOfArc___call__)
    SetValue = _swig_new_instance_method(_MAT.MAT_SequenceOfArc_SetValue)
    __swig_destroy__ = _MAT.delete_MAT_SequenceOfArc

# Register MAT_SequenceOfArc in _MAT:
_MAT.MAT_SequenceOfArc_swigregister(MAT_SequenceOfArc)
MAT_SequenceOfArc_delNode = _MAT.MAT_SequenceOfArc_delNode

class MAT_DataMapOfIntegerNode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_begin)
    end = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_end)
    cbegin = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_cbegin)
    cend = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_cend)

    def __init__(self, *args):
        _MAT.MAT_DataMapOfIntegerNode_swiginit(self, _MAT.new_MAT_DataMapOfIntegerNode(*args))
    Exchange = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Exchange)
    Assign = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Assign)
    Set = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Set)
    ReSize = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_ReSize)
    Bind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Bind)
    Bound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Bound)
    IsBound = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_IsBound)
    UnBind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_UnBind)
    Seek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Seek)
    Find = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Find)
    ChangeSeek = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_ChangeFind)
    __call__ = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode___call__)
    Clear = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Clear)
    __swig_destroy__ = _MAT.delete_MAT_DataMapOfIntegerNode
    Size = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Size)
    Keys = _swig_new_instance_method(_MAT.MAT_DataMapOfIntegerNode_Keys)

# Register MAT_DataMapOfIntegerNode in _MAT:
_MAT.MAT_DataMapOfIntegerNode_swigregister(MAT_DataMapOfIntegerNode)

class MAT_Arc(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FirstElement = _swig_new_instance_method(_MAT.MAT_Arc_FirstElement)
    FirstNode = _swig_new_instance_method(_MAT.MAT_Arc_FirstNode)
    GeomIndex = _swig_new_instance_method(_MAT.MAT_Arc_GeomIndex)
    HasNeighbour = _swig_new_instance_method(_MAT.MAT_Arc_HasNeighbour)
    Index = _swig_new_instance_method(_MAT.MAT_Arc_Index)

    def __init__(self, *args):
        r"""
        :param ArcIndex:
        	:type ArcIndex: int
        	:param GeomIndex:
        	:type GeomIndex: int
        	:param FirstElement:
        	:type FirstElement: MAT_BasicElt
        	:param SecondElement:
        	:type SecondElement: MAT_BasicElt
        	:rtype: None
        """
        _MAT.MAT_Arc_swiginit(self, _MAT.new_MAT_Arc(*args))
    Neighbour = _swig_new_instance_method(_MAT.MAT_Arc_Neighbour)
    SecondElement = _swig_new_instance_method(_MAT.MAT_Arc_SecondElement)
    SecondNode = _swig_new_instance_method(_MAT.MAT_Arc_SecondNode)
    SetFirstArc = _swig_new_instance_method(_MAT.MAT_Arc_SetFirstArc)
    SetFirstElement = _swig_new_instance_method(_MAT.MAT_Arc_SetFirstElement)
    SetFirstNode = _swig_new_instance_method(_MAT.MAT_Arc_SetFirstNode)
    SetGeomIndex = _swig_new_instance_method(_MAT.MAT_Arc_SetGeomIndex)
    SetIndex = _swig_new_instance_method(_MAT.MAT_Arc_SetIndex)
    SetNeighbour = _swig_new_instance_method(_MAT.MAT_Arc_SetNeighbour)
    SetSecondArc = _swig_new_instance_method(_MAT.MAT_Arc_SetSecondArc)
    SetSecondElement = _swig_new_instance_method(_MAT.MAT_Arc_SetSecondElement)
    SetSecondNode = _swig_new_instance_method(_MAT.MAT_Arc_SetSecondNode)
    TheOtherNode = _swig_new_instance_method(_MAT.MAT_Arc_TheOtherNode)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Arc_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Arc

# Register MAT_Arc in _MAT:
_MAT.MAT_Arc_swigregister(MAT_Arc)

class MAT_BasicElt(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    EndArc = _swig_new_instance_method(_MAT.MAT_BasicElt_EndArc)
    GeomIndex = _swig_new_instance_method(_MAT.MAT_BasicElt_GeomIndex)
    Index = _swig_new_instance_method(_MAT.MAT_BasicElt_Index)

    def __init__(self, *args):
        r"""
        * Constructor, <anInteger> is the <index> of <self>.
        	:param anInteger:
        	:type anInteger: int
        	:rtype: None
        """
        _MAT.MAT_BasicElt_swiginit(self, _MAT.new_MAT_BasicElt(*args))
    SetEndArc = _swig_new_instance_method(_MAT.MAT_BasicElt_SetEndArc)
    SetGeomIndex = _swig_new_instance_method(_MAT.MAT_BasicElt_SetGeomIndex)
    SetIndex = _swig_new_instance_method(_MAT.MAT_BasicElt_SetIndex)
    SetStartArc = _swig_new_instance_method(_MAT.MAT_BasicElt_SetStartArc)
    StartArc = _swig_new_instance_method(_MAT.MAT_BasicElt_StartArc)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_BasicElt_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_BasicElt

# Register MAT_BasicElt in _MAT:
_MAT.MAT_BasicElt_swigregister(MAT_BasicElt)

class MAT_Bisector(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddBisector = _swig_new_instance_method(_MAT.MAT_Bisector_AddBisector)
    BisectorNumber = _swig_new_instance_method(_MAT.MAT_Bisector_BisectorNumber)
    DistIssuePoint = _swig_new_instance_method(_MAT.MAT_Bisector_DistIssuePoint)
    Dump = _swig_new_instance_method(_MAT.MAT_Bisector_Dump)
    EndPoint = _swig_new_instance_method(_MAT.MAT_Bisector_EndPoint)
    FirstBisector = _swig_new_instance_method(_MAT.MAT_Bisector_FirstBisector)
    FirstEdge = _swig_new_instance_method(_MAT.MAT_Bisector_FirstEdge)
    FirstParameter = _swig_new_instance_method(_MAT.MAT_Bisector_FirstParameter)
    FirstVector = _swig_new_instance_method(_MAT.MAT_Bisector_FirstVector)
    IndexNumber = _swig_new_instance_method(_MAT.MAT_Bisector_IndexNumber)
    IssuePoint = _swig_new_instance_method(_MAT.MAT_Bisector_IssuePoint)
    LastBisector = _swig_new_instance_method(_MAT.MAT_Bisector_LastBisector)
    List = _swig_new_instance_method(_MAT.MAT_Bisector_List)

    def __init__(self, *args):
        r""":rtype: None"""
        _MAT.MAT_Bisector_swiginit(self, _MAT.new_MAT_Bisector(*args))
    SecondEdge = _swig_new_instance_method(_MAT.MAT_Bisector_SecondEdge)
    SecondParameter = _swig_new_instance_method(_MAT.MAT_Bisector_SecondParameter)
    SecondVector = _swig_new_instance_method(_MAT.MAT_Bisector_SecondVector)
    Sense = _swig_new_instance_method(_MAT.MAT_Bisector_Sense)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Bisector_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Bisector

# Register MAT_Bisector in _MAT:
_MAT.MAT_Bisector_swigregister(MAT_Bisector)

class MAT_Edge(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Distance = _swig_new_instance_method(_MAT.MAT_Edge_Distance)
    Dump = _swig_new_instance_method(_MAT.MAT_Edge_Dump)
    EdgeNumber = _swig_new_instance_method(_MAT.MAT_Edge_EdgeNumber)
    FirstBisector = _swig_new_instance_method(_MAT.MAT_Edge_FirstBisector)
    IntersectionPoint = _swig_new_instance_method(_MAT.MAT_Edge_IntersectionPoint)

    def __init__(self, *args):
        r""":rtype: None"""
        _MAT.MAT_Edge_swiginit(self, _MAT.new_MAT_Edge(*args))
    SecondBisector = _swig_new_instance_method(_MAT.MAT_Edge_SecondBisector)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Edge_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Edge

# Register MAT_Edge in _MAT:
_MAT.MAT_Edge_swigregister(MAT_Edge)

class MAT_Graph(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Arc = _swig_new_instance_method(_MAT.MAT_Graph_Arc)
    BasicElt = _swig_new_instance_method(_MAT.MAT_Graph_BasicElt)
    ChangeBasicElt = _swig_new_instance_method(_MAT.MAT_Graph_ChangeBasicElt)
    ChangeBasicElts = _swig_new_instance_method(_MAT.MAT_Graph_ChangeBasicElts)
    CompactArcs = _swig_new_instance_method(_MAT.MAT_Graph_CompactArcs)
    CompactNodes = _swig_new_instance_method(_MAT.MAT_Graph_CompactNodes)
    FusionOfBasicElts = _swig_new_instance_method(_MAT.MAT_Graph_FusionOfBasicElts)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None
        """
        _MAT.MAT_Graph_swiginit(self, _MAT.new_MAT_Graph(*args))
    Node = _swig_new_instance_method(_MAT.MAT_Graph_Node)
    NumberOfArcs = _swig_new_instance_method(_MAT.MAT_Graph_NumberOfArcs)
    NumberOfBasicElts = _swig_new_instance_method(_MAT.MAT_Graph_NumberOfBasicElts)
    NumberOfInfiniteNodes = _swig_new_instance_method(_MAT.MAT_Graph_NumberOfInfiniteNodes)
    NumberOfNodes = _swig_new_instance_method(_MAT.MAT_Graph_NumberOfNodes)
    Perform = _swig_new_instance_method(_MAT.MAT_Graph_Perform)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Graph_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Graph

# Register MAT_Graph in _MAT:
_MAT.MAT_Graph_swigregister(MAT_Graph)

class MAT_ListOfBisector(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BackAdd = _swig_new_instance_method(_MAT.MAT_ListOfBisector_BackAdd)
    Brackets = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Brackets)
    Current = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Current)
    Dump = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Dump)
    First = _swig_new_instance_method(_MAT.MAT_ListOfBisector_First)
    FirstItem = _swig_new_instance_method(_MAT.MAT_ListOfBisector_FirstItem)
    FrontAdd = _swig_new_instance_method(_MAT.MAT_ListOfBisector_FrontAdd)
    Index = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Index)
    Init = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Init)
    IsEmpty = _swig_new_instance_method(_MAT.MAT_ListOfBisector_IsEmpty)
    Last = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Last)
    LastItem = _swig_new_instance_method(_MAT.MAT_ListOfBisector_LastItem)
    LinkAfter = _swig_new_instance_method(_MAT.MAT_ListOfBisector_LinkAfter)
    LinkBefore = _swig_new_instance_method(_MAT.MAT_ListOfBisector_LinkBefore)
    Loop = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Loop)

    def __init__(self, *args):
        r""":rtype: None"""
        _MAT.MAT_ListOfBisector_swiginit(self, _MAT.new_MAT_ListOfBisector(*args))
    More = _swig_new_instance_method(_MAT.MAT_ListOfBisector_More)
    Next = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Next)
    NextItem = _swig_new_instance_method(_MAT.MAT_ListOfBisector_NextItem)
    Number = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Number)
    Permute = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Permute)
    Previous = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Previous)
    PreviousItem = _swig_new_instance_method(_MAT.MAT_ListOfBisector_PreviousItem)
    Unlink = _swig_new_instance_method(_MAT.MAT_ListOfBisector_Unlink)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_ListOfBisector_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_ListOfBisector

# Register MAT_ListOfBisector in _MAT:
_MAT.MAT_ListOfBisector_swigregister(MAT_ListOfBisector)

class MAT_ListOfEdge(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BackAdd = _swig_new_instance_method(_MAT.MAT_ListOfEdge_BackAdd)
    Brackets = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Brackets)
    Current = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Current)
    Dump = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Dump)
    First = _swig_new_instance_method(_MAT.MAT_ListOfEdge_First)
    FirstItem = _swig_new_instance_method(_MAT.MAT_ListOfEdge_FirstItem)
    FrontAdd = _swig_new_instance_method(_MAT.MAT_ListOfEdge_FrontAdd)
    Index = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Index)
    Init = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Init)
    IsEmpty = _swig_new_instance_method(_MAT.MAT_ListOfEdge_IsEmpty)
    Last = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Last)
    LastItem = _swig_new_instance_method(_MAT.MAT_ListOfEdge_LastItem)
    LinkAfter = _swig_new_instance_method(_MAT.MAT_ListOfEdge_LinkAfter)
    LinkBefore = _swig_new_instance_method(_MAT.MAT_ListOfEdge_LinkBefore)
    Loop = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Loop)

    def __init__(self, *args):
        r""":rtype: None"""
        _MAT.MAT_ListOfEdge_swiginit(self, _MAT.new_MAT_ListOfEdge(*args))
    More = _swig_new_instance_method(_MAT.MAT_ListOfEdge_More)
    Next = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Next)
    NextItem = _swig_new_instance_method(_MAT.MAT_ListOfEdge_NextItem)
    Number = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Number)
    Permute = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Permute)
    Previous = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Previous)
    PreviousItem = _swig_new_instance_method(_MAT.MAT_ListOfEdge_PreviousItem)
    Unlink = _swig_new_instance_method(_MAT.MAT_ListOfEdge_Unlink)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_ListOfEdge_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_ListOfEdge

# Register MAT_ListOfEdge in _MAT:
_MAT.MAT_ListOfEdge_swigregister(MAT_ListOfEdge)

class MAT_Node(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Distance = _swig_new_instance_method(_MAT.MAT_Node_Distance)
    GeomIndex = _swig_new_instance_method(_MAT.MAT_Node_GeomIndex)
    Index = _swig_new_instance_method(_MAT.MAT_Node_Index)
    Infinite = _swig_new_instance_method(_MAT.MAT_Node_Infinite)
    LinkedArcs = _swig_new_instance_method(_MAT.MAT_Node_LinkedArcs)

    def __init__(self, *args):
        r"""
        :param GeomIndex:
        	:type GeomIndex: int
        	:param LinkedArc:
        	:type LinkedArc: MAT_Arc
        	:param Distance:
        	:type Distance: float
        	:rtype: None
        """
        _MAT.MAT_Node_swiginit(self, _MAT.new_MAT_Node(*args))
    NearElts = _swig_new_instance_method(_MAT.MAT_Node_NearElts)
    OnBasicElt = _swig_new_instance_method(_MAT.MAT_Node_OnBasicElt)
    PendingNode = _swig_new_instance_method(_MAT.MAT_Node_PendingNode)
    SetIndex = _swig_new_instance_method(_MAT.MAT_Node_SetIndex)
    SetLinkedArc = _swig_new_instance_method(_MAT.MAT_Node_SetLinkedArc)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Node_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Node

# Register MAT_Node in _MAT:
_MAT.MAT_Node_swigregister(MAT_Node)

class MAT_TListNodeOfListOfBisector(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Dummy = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfBisector_Dummy)
    GetItem = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfBisector_GetItem)

    def __init__(self, *args):
        r"""
        :rtype: None:param anitem:
        	:type anitem: MAT_Bisector
        	:rtype: None
        """
        _MAT.MAT_TListNodeOfListOfBisector_swiginit(self, _MAT.new_MAT_TListNodeOfListOfBisector(*args))
    Next = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfBisector_Next)
    Previous = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfBisector_Previous)
    SetItem = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfBisector_SetItem)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_TListNodeOfListOfBisector_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_TListNodeOfListOfBisector

# Register MAT_TListNodeOfListOfBisector in _MAT:
_MAT.MAT_TListNodeOfListOfBisector_swigregister(MAT_TListNodeOfListOfBisector)

class MAT_TListNodeOfListOfEdge(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Dummy = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfEdge_Dummy)
    GetItem = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfEdge_GetItem)

    def __init__(self, *args):
        r"""
        :rtype: None:param anitem:
        	:type anitem: MAT_Edge
        	:rtype: None
        """
        _MAT.MAT_TListNodeOfListOfEdge_swiginit(self, _MAT.new_MAT_TListNodeOfListOfEdge(*args))
    Next = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfEdge_Next)
    Previous = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfEdge_Previous)
    SetItem = _swig_new_instance_method(_MAT.MAT_TListNodeOfListOfEdge_SetItem)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_TListNodeOfListOfEdge_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_TListNodeOfListOfEdge

# Register MAT_TListNodeOfListOfEdge in _MAT:
_MAT.MAT_TListNodeOfListOfEdge_swigregister(MAT_TListNodeOfListOfEdge)

class MAT_Zone(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ArcOnFrontier = _swig_new_instance_method(_MAT.MAT_Zone_ArcOnFrontier)
    Limited = _swig_new_instance_method(_MAT.MAT_Zone_Limited)

    def __init__(self, *args):
        r"""
        :rtype: None* Compute the frontier of the Zone of proximity.
        	:param aBasicElt:
        	:type aBasicElt: MAT_BasicElt
        	:rtype: None
        """
        _MAT.MAT_Zone_swiginit(self, _MAT.new_MAT_Zone(*args))
    NoEmptyZone = _swig_new_instance_method(_MAT.MAT_Zone_NoEmptyZone)
    NumberOfArcs = _swig_new_instance_method(_MAT.MAT_Zone_NumberOfArcs)
    Perform = _swig_new_instance_method(_MAT.MAT_Zone_Perform)


    @staticmethod
    def DownCast(t):
      return Handle_MAT_Zone_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _MAT.delete_MAT_Zone

# Register MAT_Zone in _MAT:
_MAT.MAT_Zone_swigregister(MAT_Zone)


