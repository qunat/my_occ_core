# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BiTgte module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_bitgte.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BiTgte
else:
    import _BiTgte

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BiTgte.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BiTgte.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BiTgte.delete_SwigPyIterator
    value = _swig_new_instance_method(_BiTgte.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BiTgte.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BiTgte.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BiTgte.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BiTgte.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BiTgte.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BiTgte.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BiTgte.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BiTgte.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BiTgte.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BiTgte:
_BiTgte.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TopTools
import OCC.Core.TCollection
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.Geom2d
import OCC.Core.Adaptor3d
import OCC.Core.Adaptor2d
import OCC.Core.math
BiTgte_FaceFace = _BiTgte.BiTgte_FaceFace
BiTgte_FaceEdge = _BiTgte.BiTgte_FaceEdge
BiTgte_FaceVertex = _BiTgte.BiTgte_FaceVertex
BiTgte_EdgeEdge = _BiTgte.BiTgte_EdgeEdge
BiTgte_EdgeVertex = _BiTgte.BiTgte_EdgeVertex
BiTgte_VertexVertex = _BiTgte.BiTgte_VertexVertex
Handle_BiTgte_HCurveOnEdge_Create = _BiTgte.Handle_BiTgte_HCurveOnEdge_Create
Handle_BiTgte_HCurveOnEdge_DownCast = _BiTgte.Handle_BiTgte_HCurveOnEdge_DownCast
Handle_BiTgte_HCurveOnEdge_IsNull = _BiTgte.Handle_BiTgte_HCurveOnEdge_IsNull
Handle_BiTgte_HCurveOnVertex_Create = _BiTgte.Handle_BiTgte_HCurveOnVertex_Create
Handle_BiTgte_HCurveOnVertex_DownCast = _BiTgte.Handle_BiTgte_HCurveOnVertex_DownCast
Handle_BiTgte_HCurveOnVertex_IsNull = _BiTgte.Handle_BiTgte_HCurveOnVertex_IsNull
class BiTgte_Blend(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* <S>: Shape to be rounded <Radius>: radius of the fillet <Tol>: Tol3d used in approximations <NUBS>: if true, generate only NUBS surfaces, if false, generate analytical surfaces if possible
        	:param S:
        	:type S: TopoDS_Shape
        	:param Radius:
        	:type Radius: float
        	:param Tol:
        	:type Tol: float
        	:param NUBS:
        	:type NUBS: bool
        	:rtype: None
        """
        _BiTgte.BiTgte_Blend_swiginit(self, _BiTgte.new_BiTgte_Blend(*args))
    CenterLines = _swig_new_instance_method(_BiTgte.BiTgte_Blend_CenterLines)
    Clear = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Clear)
    ComputeCenters = _swig_new_instance_method(_BiTgte.BiTgte_Blend_ComputeCenters)
    ContactType = _swig_new_instance_method(_BiTgte.BiTgte_Blend_ContactType)
    CurveOnShape1 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_CurveOnShape1)
    CurveOnShape2 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_CurveOnShape2)
    Face = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Face)
    IndicesOfBranche = _swig_new_instance_method(_BiTgte.BiTgte_Blend_IndicesOfBranche)
    Init = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Init)
    IsDone = _swig_new_instance_method(_BiTgte.BiTgte_Blend_IsDone)
    NbBranches = _swig_new_instance_method(_BiTgte.BiTgte_Blend_NbBranches)
    NbSurfaces = _swig_new_instance_method(_BiTgte.BiTgte_Blend_NbSurfaces)
    PCurve1OnFillet = _swig_new_instance_method(_BiTgte.BiTgte_Blend_PCurve1OnFillet)
    PCurve2OnFillet = _swig_new_instance_method(_BiTgte.BiTgte_Blend_PCurve2OnFillet)
    PCurveOnFace1 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_PCurveOnFace1)
    PCurveOnFace2 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_PCurveOnFace2)
    Perform = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Perform)
    SetEdge = _swig_new_instance_method(_BiTgte.BiTgte_Blend_SetEdge)
    SetFaces = _swig_new_instance_method(_BiTgte.BiTgte_Blend_SetFaces)
    SetStoppingFace = _swig_new_instance_method(_BiTgte.BiTgte_Blend_SetStoppingFace)
    Shape = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Shape)
    SupportShape1 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_SupportShape1)
    SupportShape2 = _swig_new_instance_method(_BiTgte.BiTgte_Blend_SupportShape2)
    Surface = _swig_new_instance_method(_BiTgte.BiTgte_Blend_Surface)

    __repr__ = _dumps_object

    __swig_destroy__ = _BiTgte.delete_BiTgte_Blend

# Register BiTgte_Blend in _BiTgte:
_BiTgte.BiTgte_Blend_swigregister(BiTgte_Blend)

class BiTgte_CurveOnEdge(OCC.Core.Adaptor3d.Adaptor3d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param EonF:
        	:type EonF: TopoDS_Edge
        	:param Edge:
        	:type Edge: TopoDS_Edge
        	:rtype: None
        """
        _BiTgte.BiTgte_CurveOnEdge_swiginit(self, _BiTgte.new_BiTgte_CurveOnEdge(*args))
    Init = _swig_new_instance_method(_BiTgte.BiTgte_CurveOnEdge_Init)

    __repr__ = _dumps_object

    __swig_destroy__ = _BiTgte.delete_BiTgte_CurveOnEdge

# Register BiTgte_CurveOnEdge in _BiTgte:
_BiTgte.BiTgte_CurveOnEdge_swigregister(BiTgte_CurveOnEdge)

class BiTgte_CurveOnVertex(OCC.Core.Adaptor3d.Adaptor3d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None:param EonF:
        	:type EonF: TopoDS_Edge
        	:param V:
        	:type V: TopoDS_Vertex
        	:rtype: None
        """
        _BiTgte.BiTgte_CurveOnVertex_swiginit(self, _BiTgte.new_BiTgte_CurveOnVertex(*args))
    Init = _swig_new_instance_method(_BiTgte.BiTgte_CurveOnVertex_Init)

    __repr__ = _dumps_object

    __swig_destroy__ = _BiTgte.delete_BiTgte_CurveOnVertex

# Register BiTgte_CurveOnVertex in _BiTgte:
_BiTgte.BiTgte_CurveOnVertex_swigregister(BiTgte_CurveOnVertex)

class BiTgte_HCurveOnEdge(OCC.Core.Adaptor3d.Adaptor3d_HCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve.
        	:rtype: None* Creates a GenHCurve from a Curve
        	:param C:
        	:type C: BiTgte_CurveOnEdge
        	:rtype: None
        """
        _BiTgte.BiTgte_HCurveOnEdge_swiginit(self, _BiTgte.new_BiTgte_HCurveOnEdge(*args))
    ChangeCurve = _swig_new_instance_method(_BiTgte.BiTgte_HCurveOnEdge_ChangeCurve)
    Set = _swig_new_instance_method(_BiTgte.BiTgte_HCurveOnEdge_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BiTgte_HCurveOnEdge_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BiTgte.delete_BiTgte_HCurveOnEdge

# Register BiTgte_HCurveOnEdge in _BiTgte:
_BiTgte.BiTgte_HCurveOnEdge_swigregister(BiTgte_HCurveOnEdge)

class BiTgte_HCurveOnVertex(OCC.Core.Adaptor3d.Adaptor3d_HCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve.
        	:rtype: None* Creates a GenHCurve from a Curve
        	:param C:
        	:type C: BiTgte_CurveOnVertex
        	:rtype: None
        """
        _BiTgte.BiTgte_HCurveOnVertex_swiginit(self, _BiTgte.new_BiTgte_HCurveOnVertex(*args))
    ChangeCurve = _swig_new_instance_method(_BiTgte.BiTgte_HCurveOnVertex_ChangeCurve)
    Set = _swig_new_instance_method(_BiTgte.BiTgte_HCurveOnVertex_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BiTgte_HCurveOnVertex_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BiTgte.delete_BiTgte_HCurveOnVertex

# Register BiTgte_HCurveOnVertex in _BiTgte:
_BiTgte.BiTgte_HCurveOnVertex_swigregister(BiTgte_HCurveOnVertex)



