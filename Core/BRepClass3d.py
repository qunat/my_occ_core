# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BRepClass3d module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_brepclass3d.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BRepClass3d
else:
    import _BRepClass3d

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BRepClass3d.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BRepClass3d.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BRepClass3d.delete_SwigPyIterator
    value = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BRepClass3d.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BRepClass3d.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BRepClass3d:
_BRepClass3d.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.IntCurveSurface
import OCC.Core.math
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.Intf
import OCC.Core.Bnd
import OCC.Core.BVH
import OCC.Core.IntSurf
import OCC.Core.TopTools
import OCC.Core.IntCurvesFace
import OCC.Core.BRepAdaptor
import OCC.Core.GeomAdaptor
import OCC.Core.Geom2dAdaptor
class BRepClass3d_MapOfInter(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_begin)
    end = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_end)
    cbegin = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_cbegin)
    cend = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_cend)

    def __init__(self, *args):
        _BRepClass3d.BRepClass3d_MapOfInter_swiginit(self, _BRepClass3d.new_BRepClass3d_MapOfInter(*args))
    Exchange = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Exchange)
    Assign = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Assign)
    Set = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Set)
    ReSize = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_ReSize)
    Bind = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Bind)
    Bound = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Bound)
    IsBound = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_IsBound)
    UnBind = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_UnBind)
    Seek = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Seek)
    Find = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Find)
    ChangeSeek = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_ChangeFind)
    __call__ = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter___call__)
    Clear = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Clear)
    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_MapOfInter
    Size = _swig_new_instance_method(_BRepClass3d.BRepClass3d_MapOfInter_Size)

# Register BRepClass3d_MapOfInter in _BRepClass3d:
_BRepClass3d.BRepClass3d_MapOfInter_swigregister(BRepClass3d_MapOfInter)

class BRepClass3d_BndBoxTree(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepClass3d.BRepClass3d_BndBoxTree_swiginit(self, _BRepClass3d.new_BRepClass3d_BndBoxTree(*args))
    Add = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_Add)
    Select = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_Select)
    Clear = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_Clear)
    IsEmpty = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_IsEmpty)
    Root = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_Root)
    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_BndBoxTree
    Allocator = _swig_new_instance_method(_BRepClass3d.BRepClass3d_BndBoxTree_Allocator)

# Register BRepClass3d_BndBoxTree in _BRepClass3d:
_BRepClass3d.BRepClass3d_BndBoxTree_swigregister(BRepClass3d_BndBoxTree)

class brepclass3d(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    OuterShell = _swig_new_static_method(_BRepClass3d.brepclass3d_OuterShell)

    __repr__ = _dumps_object


    def __init__(self):
        _BRepClass3d.brepclass3d_swiginit(self, _BRepClass3d.new_brepclass3d())
    __swig_destroy__ = _BRepClass3d.delete_brepclass3d

# Register brepclass3d in _BRepClass3d:
_BRepClass3d.brepclass3d_swigregister(brepclass3d)
brepclass3d_OuterShell = _BRepClass3d.brepclass3d_OuterShell

class BRepClass3d_Intersector3d(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None
        """
        _BRepClass3d.BRepClass3d_Intersector3d_swiginit(self, _BRepClass3d.new_BRepClass3d_Intersector3d(*args))
    Face = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_Face)
    HasAPoint = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_HasAPoint)
    IsDone = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_IsDone)
    Perform = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_Perform)
    Pnt = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_Pnt)
    State = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_State)
    Transition = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_Transition)
    UParameter = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_UParameter)
    VParameter = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_VParameter)
    WParameter = _swig_new_instance_method(_BRepClass3d.BRepClass3d_Intersector3d_WParameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_Intersector3d

# Register BRepClass3d_Intersector3d in _BRepClass3d:
_BRepClass3d.BRepClass3d_Intersector3d_swigregister(BRepClass3d_Intersector3d)

class BRepClass3d_SClassifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Constructor to classify the point P with the tolerance Tol on the solid S.
        	:param S:
        	:type S: BRepClass3d_SolidExplorer
        	:param P:
        	:type P: gp_Pnt
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _BRepClass3d.BRepClass3d_SClassifier_swiginit(self, _BRepClass3d.new_BRepClass3d_SClassifier(*args))
    Face = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_Face)
    IsOnAFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_IsOnAFace)
    Perform = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_Perform)
    PerformInfinitePoint = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_PerformInfinitePoint)
    Rejected = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_Rejected)
    State = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SClassifier_State)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_SClassifier

# Register BRepClass3d_SClassifier in _BRepClass3d:
_BRepClass3d.BRepClass3d_SClassifier_swigregister(BRepClass3d_SClassifier)

class BRepClass3d_SolidExplorer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param S:
        	:type S: TopoDS_Shape
        	:rtype: None
        """
        _BRepClass3d.BRepClass3d_SolidExplorer_swiginit(self, _BRepClass3d.new_BRepClass3d_SolidExplorer(*args))
    Box = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_Box)
    CurrentFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_CurrentFace)
    CurrentShell = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_CurrentShell)
    Destroy = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_Destroy)
    DumpSegment = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_DumpSegment)
    FindAPointInTheFace = _swig_new_static_method(_BRepClass3d.BRepClass3d_SolidExplorer_FindAPointInTheFace)
    GetFaceSegmentIndex = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_GetFaceSegmentIndex)
    GetMapEV = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_GetMapEV)
    GetShape = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_GetShape)
    GetTree = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_GetTree)
    InitFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_InitFace)
    InitShape = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_InitShape)
    InitShell = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_InitShell)
    Intersector = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_Intersector)
    MoreFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_MoreFace)
    MoreShell = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_MoreShell)
    NextFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_NextFace)
    NextShell = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_NextShell)
    OtherSegment = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_OtherSegment)
    PointInTheFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_PointInTheFace)
    Reject = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_Reject)
    RejectFace = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_RejectFace)
    RejectShell = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_RejectShell)
    Segment = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidExplorer_Segment)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_SolidExplorer

# Register BRepClass3d_SolidExplorer in _BRepClass3d:
_BRepClass3d.BRepClass3d_SolidExplorer_swigregister(BRepClass3d_SolidExplorer)
BRepClass3d_SolidExplorer_FindAPointInTheFace = _BRepClass3d.BRepClass3d_SolidExplorer_FindAPointInTheFace

class BRepClass3d_SolidPassiveClassifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an undefined classifier.
        	:rtype: None
        """
        _BRepClass3d.BRepClass3d_SolidPassiveClassifier_swiginit(self, _BRepClass3d.new_BRepClass3d_SolidPassiveClassifier(*args))
    Compare = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_Compare)
    HasIntersection = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_HasIntersection)
    Intersector = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_Intersector)
    Parameter = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_Parameter)
    Reset = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_Reset)
    State = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidPassiveClassifier_State)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_SolidPassiveClassifier

# Register BRepClass3d_SolidPassiveClassifier in _BRepClass3d:
_BRepClass3d.BRepClass3d_SolidPassiveClassifier_swigregister(BRepClass3d_SolidPassiveClassifier)

class BRepClass3d_SolidClassifier(BRepClass3d_SClassifier):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * empty constructor
        	:rtype: None* Constructor from a Shape.
        	:param S:
        	:type S: TopoDS_Shape
        	:rtype: None* Constructor to classify the point P with the tolerance Tol on the solid S.
        	:param S:
        	:type S: TopoDS_Shape
        	:param P:
        	:type P: gp_Pnt
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _BRepClass3d.BRepClass3d_SolidClassifier_swiginit(self, _BRepClass3d.new_BRepClass3d_SolidClassifier(*args))
    Destroy = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidClassifier_Destroy)
    Load = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidClassifier_Load)
    Perform = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidClassifier_Perform)
    PerformInfinitePoint = _swig_new_instance_method(_BRepClass3d.BRepClass3d_SolidClassifier_PerformInfinitePoint)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepClass3d.delete_BRepClass3d_SolidClassifier

# Register BRepClass3d_SolidClassifier in _BRepClass3d:
_BRepClass3d.BRepClass3d_SolidClassifier_swigregister(BRepClass3d_SolidClassifier)



