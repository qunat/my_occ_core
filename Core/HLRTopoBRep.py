# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
HLRTopoBRep module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_hlrtopobrep.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _HLRTopoBRep
else:
    import _HLRTopoBRep

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _HLRTopoBRep.SWIG_PyInstanceMethod_New
_swig_new_static_method = _HLRTopoBRep.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _HLRTopoBRep.delete_SwigPyIterator
    value = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_value)
    incr = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_copy)
    next = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_HLRTopoBRep.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _HLRTopoBRep:
_HLRTopoBRep.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TopoDS
import OCC.Core.Message
import OCC.Core.TopAbs
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.Contap
import OCC.Core.math
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.IntSurf
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.BRepTopAdaptor
import OCC.Core.BRepAdaptor
import OCC.Core.GeomAdaptor
import OCC.Core.Geom2dAdaptor
import OCC.Core.TopTools
import OCC.Core.HLRAlgo
Handle_HLRTopoBRep_OutLiner_Create = _HLRTopoBRep.Handle_HLRTopoBRep_OutLiner_Create
Handle_HLRTopoBRep_OutLiner_DownCast = _HLRTopoBRep.Handle_HLRTopoBRep_OutLiner_DownCast
Handle_HLRTopoBRep_OutLiner_IsNull = _HLRTopoBRep.Handle_HLRTopoBRep_OutLiner_IsNull
class HLRTopoBRep_DataMapOfShapeFaceData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_begin)
    end = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_end)
    cbegin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_cbegin)
    cend = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_cend)

    def __init__(self, *args):
        _HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_DataMapOfShapeFaceData(*args))
    Exchange = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Exchange)
    Assign = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Assign)
    Set = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Set)
    ReSize = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_ReSize)
    Bind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Bind)
    Bound = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Bound)
    IsBound = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_IsBound)
    UnBind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_UnBind)
    Seek = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Seek)
    Find = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Find)
    ChangeSeek = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_ChangeFind)
    __call__ = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData___call__)
    Clear = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Clear)
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_DataMapOfShapeFaceData
    Size = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_Size)

# Register HLRTopoBRep_DataMapOfShapeFaceData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_DataMapOfShapeFaceData_swigregister(HLRTopoBRep_DataMapOfShapeFaceData)

class HLRTopoBRep_ListOfVData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_begin)
    end = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_end)
    cbegin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_cbegin)
    cend = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_cend)

    def __init__(self, *args):
        _HLRTopoBRep.HLRTopoBRep_ListOfVData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_ListOfVData(*args))
    Size = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Size)
    Assign = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Assign)
    Set = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Set)
    Clear = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Clear)
    First = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_First)
    Last = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Last)
    Append = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Append)
    Prepend = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Prepend)
    RemoveFirst = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_RemoveFirst)
    Remove = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Remove)
    InsertBefore = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_InsertBefore)
    InsertAfter = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_InsertAfter)
    Reverse = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListOfVData_Reverse)
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_ListOfVData

# Register HLRTopoBRep_ListOfVData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_ListOfVData_swigregister(HLRTopoBRep_ListOfVData)

class HLRTopoBRep_ListIteratorOfListOfVData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_ListIteratorOfListOfVData(*args))
    More = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_More)
    Next = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_Next)
    Value = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_Value)
    ChangeValue = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_ChangeValue)
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_ListIteratorOfListOfVData

# Register HLRTopoBRep_ListIteratorOfListOfVData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_ListIteratorOfListOfVData_swigregister(HLRTopoBRep_ListIteratorOfListOfVData)

class HLRTopoBRep_MapOfShapeListOfVData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_begin)
    end = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_end)
    cbegin = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_cbegin)
    cend = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_cend)

    def __init__(self, *args):
        _HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_MapOfShapeListOfVData(*args))
    Exchange = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Exchange)
    Assign = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Assign)
    Set = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Set)
    ReSize = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_ReSize)
    Bind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Bind)
    Bound = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Bound)
    IsBound = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_IsBound)
    UnBind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_UnBind)
    Seek = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Seek)
    Find = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Find)
    ChangeSeek = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_ChangeFind)
    __call__ = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData___call__)
    Clear = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Clear)
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_MapOfShapeListOfVData
    Size = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_Size)

# Register HLRTopoBRep_MapOfShapeListOfVData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_MapOfShapeListOfVData_swigregister(HLRTopoBRep_MapOfShapeListOfVData)

class HLRTopoBRep_DSFiller(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Insert = _swig_new_static_method(_HLRTopoBRep.HLRTopoBRep_DSFiller_Insert)

    __repr__ = _dumps_object


    def __init__(self):
        _HLRTopoBRep.HLRTopoBRep_DSFiller_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_DSFiller())
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_DSFiller

# Register HLRTopoBRep_DSFiller in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_DSFiller_swigregister(HLRTopoBRep_DSFiller)
HLRTopoBRep_DSFiller_Insert = _HLRTopoBRep.HLRTopoBRep_DSFiller_Insert

class HLRTopoBRep_Data(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddIntL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddIntL)
    AddIntV = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddIntV)
    AddIsoL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddIsoL)
    AddOldS = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddOldS)
    AddOutL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddOutL)
    AddOutV = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddOutV)
    AddSplE = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_AddSplE)
    Append = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Append)
    Clean = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Clean)
    Clear = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Clear)
    Edge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Edge)
    EdgeHasSplE = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_EdgeHasSplE)
    EdgeSplE = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_EdgeSplE)
    FaceHasIntL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceHasIntL)
    FaceHasIsoL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceHasIsoL)
    FaceHasOutL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceHasOutL)
    FaceIntL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceIntL)
    FaceIsoL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceIsoL)
    FaceOutL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_FaceOutL)

    def __init__(self, *args):
        r""":rtype: None"""
        _HLRTopoBRep.HLRTopoBRep_Data_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_Data(*args))
    InitEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_InitEdge)
    InitVertex = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_InitVertex)
    InsertBefore = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_InsertBefore)
    IsIntLFaceEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsIntLFaceEdge)
    IsIntV = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsIntV)
    IsIsoLFaceEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsIsoLFaceEdge)
    IsOutLFaceEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsOutLFaceEdge)
    IsOutV = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsOutV)
    IsSplEEdgeEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_IsSplEEdgeEdge)
    MoreEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_MoreEdge)
    MoreVertex = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_MoreVertex)
    NewSOldS = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_NewSOldS)
    NextEdge = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_NextEdge)
    NextVertex = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_NextVertex)
    Parameter = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Parameter)
    Vertex = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_Data_Vertex)

    __repr__ = _dumps_object

    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_Data

# Register HLRTopoBRep_Data in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_Data_swigregister(HLRTopoBRep_Data)

class HLRTopoBRep_FaceData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddIntL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_AddIntL)
    AddIsoL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_AddIsoL)
    AddOutL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_AddOutL)
    FaceIntL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_FaceIntL)
    FaceIsoL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_FaceIsoL)
    FaceOutL = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_FaceData_FaceOutL)

    def __init__(self, *args):
        r""":rtype: None"""
        _HLRTopoBRep.HLRTopoBRep_FaceData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_FaceData(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_FaceData

# Register HLRTopoBRep_FaceData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_FaceData_swigregister(HLRTopoBRep_FaceData)

class HLRTopoBRep_FaceIsoLiner(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    MakeIsoLine = _swig_new_static_method(_HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_MakeIsoLine)
    MakeVertex = _swig_new_static_method(_HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_MakeVertex)
    Perform = _swig_new_static_method(_HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_Perform)

    __repr__ = _dumps_object


    def __init__(self):
        _HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_FaceIsoLiner())
    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_FaceIsoLiner

# Register HLRTopoBRep_FaceIsoLiner in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_swigregister(HLRTopoBRep_FaceIsoLiner)
HLRTopoBRep_FaceIsoLiner_MakeIsoLine = _HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_MakeIsoLine
HLRTopoBRep_FaceIsoLiner_MakeVertex = _HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_MakeVertex
HLRTopoBRep_FaceIsoLiner_Perform = _HLRTopoBRep.HLRTopoBRep_FaceIsoLiner_Perform

class HLRTopoBRep_OutLiner(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DataStructure = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_OutLiner_DataStructure)
    Fill = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_OutLiner_Fill)

    def __init__(self, *args):
        r"""
        :rtype: None:param OriSh:
        	:type OriSh: TopoDS_Shape
        	:rtype: None:param OriS:
        	:type OriS: TopoDS_Shape
        	:param OutS:
        	:type OutS: TopoDS_Shape
        	:rtype: None
        """
        _HLRTopoBRep.HLRTopoBRep_OutLiner_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_OutLiner(*args))
    OriginalShape = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_OutLiner_OriginalShape)
    OutLinedShape = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_OutLiner_OutLinedShape)


    @staticmethod
    def DownCast(t):
      return Handle_HLRTopoBRep_OutLiner_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_OutLiner

# Register HLRTopoBRep_OutLiner in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_OutLiner_swigregister(HLRTopoBRep_OutLiner)

class HLRTopoBRep_VData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param P:
        	:type P: float
        	:param V:
        	:type V: TopoDS_Shape
        	:rtype: None
        """
        _HLRTopoBRep.HLRTopoBRep_VData_swiginit(self, _HLRTopoBRep.new_HLRTopoBRep_VData(*args))
    Parameter = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_VData_Parameter)
    Vertex = _swig_new_instance_method(_HLRTopoBRep.HLRTopoBRep_VData_Vertex)

    __repr__ = _dumps_object

    __swig_destroy__ = _HLRTopoBRep.delete_HLRTopoBRep_VData

# Register HLRTopoBRep_VData in _HLRTopoBRep:
_HLRTopoBRep.HLRTopoBRep_VData_swigregister(HLRTopoBRep_VData)


