# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GC module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_gc.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GC
else:
    import _GC

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GC.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GC.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GC.delete_SwigPyIterator
    value = _swig_new_instance_method(_GC.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GC.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GC.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GC.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GC.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GC.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GC.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GC.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GC.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GC.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GC.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GC.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GC.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GC.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GC.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GC.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GC:
_GC.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.gce
class GC_MakeMirror(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param Point:
        	:type Point: gp_Pnt
        	:rtype: None:param Axis:
        	:type Axis: gp_Ax1
        	:rtype: None:param Line:
        	:type Line: gp_Lin
        	:rtype: None* Make a symetry transformation af axis defined by <Point> and <Direc>.
        	:param Point:
        	:type Point: gp_Pnt
        	:param Direc:
        	:type Direc: gp_Dir
        	:rtype: None* Make a symetry transformation of plane <Plane>.
        	:param Plane:
        	:type Plane: gp_Pln
        	:rtype: None* Make a symetry transformation of plane <Plane>.
        	:param Plane:
        	:type Plane: gp_Ax2
        	:rtype: None
        """
        _GC.GC_MakeMirror_swiginit(self, _GC.new_GC_MakeMirror(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeMirror_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeMirror

# Register GC_MakeMirror in _GC:
_GC.GC_MakeMirror_swigregister(GC_MakeMirror)

class GC_MakeRotation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructs a rotation through angle Angle about the axis defined by the line Line.
        	:param Line:
        	:type Line: gp_Lin
        	:param Angle:
        	:type Angle: float
        	:rtype: None* Constructs a rotation through angle Angle about the axis defined by the axis Axis.
        	:param Axis:
        	:type Axis: gp_Ax1
        	:param Angle:
        	:type Angle: float
        	:rtype: None* Constructs a rotation through angle Angle about the axis defined by the point Point and the unit vector Direc.
        	:param Point:
        	:type Point: gp_Pnt
        	:param Direc:
        	:type Direc: gp_Dir
        	:param Angle:
        	:type Angle: float
        	:rtype: None
        """
        _GC.GC_MakeRotation_swiginit(self, _GC.new_GC_MakeRotation(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeRotation_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeRotation

# Register GC_MakeRotation in _GC:
_GC.GC_MakeRotation_swigregister(GC_MakeRotation)

class GC_MakeScale(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructs a scaling transformation with - Point as the center of the transformation, and - Scale as the scale factor.
        	:param Point:
        	:type Point: gp_Pnt
        	:param Scale:
        	:type Scale: float
        	:rtype: None
        """
        _GC.GC_MakeScale_swiginit(self, _GC.new_GC_MakeScale(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeScale_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeScale

# Register GC_MakeScale in _GC:
_GC.GC_MakeScale_swigregister(GC_MakeScale)

class GC_MakeTranslation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructs a translation along the vector ' Vect '
        	:param Vect:
        	:type Vect: gp_Vec
        	:rtype: None* Constructs a translation along the vector (Point1,Point2) defined from the point Point1 to the point Point2.
        	:param Point1:
        	:type Point1: gp_Pnt
        	:param Point2:
        	:type Point2: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeTranslation_swiginit(self, _GC.new_GC_MakeTranslation(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeTranslation_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeTranslation

# Register GC_MakeTranslation in _GC:
_GC.GC_MakeTranslation_swigregister(GC_MakeTranslation)

class GC_Root(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsDone = _swig_new_instance_method(_GC.GC_Root_IsDone)
    Status = _swig_new_instance_method(_GC.GC_Root_Status)

    __repr__ = _dumps_object


    def __init__(self):
        _GC.GC_Root_swiginit(self, _GC.new_GC_Root())
    __swig_destroy__ = _GC.delete_GC_Root

# Register GC_Root in _GC:
_GC.GC_Root_swigregister(GC_Root)

class GC_MakeArcOfCircle(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Make an arc of circle (TrimmedCurve from Geom) from a circle between two angles Alpha1 and Alpha2 given in radiians.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param Alpha1:
        	:type Alpha1: float
        	:param Alpha2:
        	:type Alpha2: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Make an arc of circle (TrimmedCurve from Geom) from a circle between point <P> and the angle Alpha given in radians.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param P:
        	:type P: gp_Pnt
        	:param Alpha:
        	:type Alpha: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Make an arc of circle (TrimmedCurve from Geom) from a circle between two points P1 and P2.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Make an arc of circle (TrimmedCurve from Geom) from three points P1,P2,P3 between two points P1 and P2.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:rtype: None* Make an arc of circle (TrimmedCurve from Geom) from two points P1,P2 and the tangente to the solution at the point P1. The orientation of the arc is: - the sense determined by the order of the points P1, P3 and P2; - the sense defined by the vector V; or - for other syntaxes: - the sense of Circ if Sense is true, or - the opposite sense if Sense is false. Note: Alpha1, Alpha2 and Alpha are angle values, given in radians. Warning If an error occurs (that is, when IsDone returns false), the Status function returns: - gce_ConfusedPoints if: - any 2 of the 3 points P1, P2 and P3 are coincident, or - P1 and P2 are coincident; or - gce_IntersectionError if: - P1, P2 and P3 are collinear and not coincident, or - the vector defined by the points P1 and P2 is collinear with the vector V.
        	:param P1:
        	:type P1: gp_Pnt
        	:param V:
        	:type V: gp_Vec
        	:param P2:
        	:type P2: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeArcOfCircle_swiginit(self, _GC.new_GC_MakeArcOfCircle(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeArcOfCircle_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeArcOfCircle

# Register GC_MakeArcOfCircle in _GC:
_GC.GC_MakeArcOfCircle_swigregister(GC_MakeArcOfCircle)

class GC_MakeArcOfEllipse(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructs an arc of Ellipse (TrimmedCurve from Geom) from a Ellipse between two parameters Alpha1 and Alpha2.
        	:param Elips:
        	:type Elips: gp_Elips
        	:param Alpha1:
        	:type Alpha1: float
        	:param Alpha2:
        	:type Alpha2: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Constructs an arc of Ellipse (TrimmedCurve from Geom) from a Ellipse between point <P> and the angle Alpha given in radians.
        	:param Elips:
        	:type Elips: gp_Elips
        	:param P:
        	:type P: gp_Pnt
        	:param Alpha:
        	:type Alpha: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Constructs an arc of Ellipse (TrimmedCurve from Geom) from a Ellipse between two points P1 and P2. The orientation of the arc of ellipse is: - the sense of Elips if Sense is true, or - the opposite sense if Sense is false. Notes: - Alpha1, Alpha2 and Alpha are angle values, given in radians. - IsDone always returns true.
        	:param Elips:
        	:type Elips: gp_Elips
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param Sense:
        	:type Sense: bool
        	:rtype: None
        """
        _GC.GC_MakeArcOfEllipse_swiginit(self, _GC.new_GC_MakeArcOfEllipse(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeArcOfEllipse_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeArcOfEllipse

# Register GC_MakeArcOfEllipse in _GC:
_GC.GC_MakeArcOfEllipse_swigregister(GC_MakeArcOfEllipse)

class GC_MakeArcOfHyperbola(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an arc of Hyperbola (TrimmedCurve from Geom) from a Hyperbola between two parameters Alpha1 and Alpha2 (given in radians).
        	:param Hypr:
        	:type Hypr: gp_Hypr
        	:param Alpha1:
        	:type Alpha1: float
        	:param Alpha2:
        	:type Alpha2: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Creates an arc of Hyperbola (TrimmedCurve from Geom) from a Hyperbola between point <P> and the parameter Alpha (given in radians).
        	:param Hypr:
        	:type Hypr: gp_Hypr
        	:param P:
        	:type P: gp_Pnt
        	:param Alpha:
        	:type Alpha: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Creates an arc of Hyperbola (TrimmedCurve from Geom) from a Hyperbola between two points P1 and P2. The orientation of the arc of hyperbola is: - the sense of Hypr if Sense is true, or - the opposite sense if Sense is false.
        	:param Hypr:
        	:type Hypr: gp_Hypr
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param Sense:
        	:type Sense: bool
        	:rtype: None
        """
        _GC.GC_MakeArcOfHyperbola_swiginit(self, _GC.new_GC_MakeArcOfHyperbola(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeArcOfHyperbola_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeArcOfHyperbola

# Register GC_MakeArcOfHyperbola in _GC:
_GC.GC_MakeArcOfHyperbola_swigregister(GC_MakeArcOfHyperbola)

class GC_MakeArcOfParabola(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an arc of Parabola (TrimmedCurve from Geom) from a Parabola between two parameters Alpha1 and Alpha2 (given in radians).
        	:param Parab:
        	:type Parab: gp_Parab
        	:param Alpha1:
        	:type Alpha1: float
        	:param Alpha2:
        	:type Alpha2: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Creates an arc of Parabola (TrimmedCurve from Geom) from a Parabola between point <P> and the parameter Alpha (given in radians).
        	:param Parab:
        	:type Parab: gp_Parab
        	:param P:
        	:type P: gp_Pnt
        	:param Alpha:
        	:type Alpha: float
        	:param Sense:
        	:type Sense: bool
        	:rtype: None* Creates an arc of Parabola (TrimmedCurve from Geom) from a Parabola between two points P1 and P2.
        	:param Parab:
        	:type Parab: gp_Parab
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param Sense:
        	:type Sense: bool
        	:rtype: None
        """
        _GC.GC_MakeArcOfParabola_swiginit(self, _GC.new_GC_MakeArcOfParabola(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeArcOfParabola_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeArcOfParabola

# Register GC_MakeArcOfParabola in _GC:
_GC.GC_MakeArcOfParabola_swigregister(GC_MakeArcOfParabola)

class GC_MakeCircle(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * creates a circle from a non persistent circle C by its conversion.
        	:param C:
        	:type C: gp_Circ
        	:rtype: None* A2 is the local coordinates system of the circle. It is not forbidden to create a circle with Radius = 0.0 Status is 'NegativeRadius' if Radius < 0.
        	:param A2:
        	:type A2: gp_Ax2
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Make a Circle from Geom <TheCirc> parallel to another Circ <Circ> with a distance <Dist>. If Dist is greater than zero the result is enclosing the circle <Circ>, else the result is enclosed by the circle <Circ>.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param Dist:
        	:type Dist: float
        	:rtype: None* Make a Circle from Geom <TheCirc> parallel to another Circ <Circ> and passing through a Pnt <Point>.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param Point:
        	:type Point: gp_Pnt
        	:rtype: None* Make a Circ from gp <TheCirc> passing through 3 Pnt2d <P1>,<P2>,<P3>.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:rtype: None* Make a Circle from Geom <TheCirc> with its center <Center> and the normal of its plane <Norm> and its radius <Radius>.
        	:param Center:
        	:type Center: gp_Pnt
        	:param Norm:
        	:type Norm: gp_Dir
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Make a Circle from Geom <TheCirc> with its center <Center> and the normal of its plane defined by the two points <Center> and <PtAxis> and its radius <Radius>.
        	:param Center:
        	:type Center: gp_Pnt
        	:param PtAxis:
        	:type PtAxis: gp_Pnt
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Make a Circle from Geom <TheCirc> with its center <Center> and its radius <Radius>.
        	:param Axis:
        	:type Axis: gp_Ax1
        	:param Radius:
        	:type Radius: float
        	:rtype: None
        """
        _GC.GC_MakeCircle_swiginit(self, _GC.new_GC_MakeCircle(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeCircle_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeCircle

# Register GC_MakeCircle in _GC:
_GC.GC_MakeCircle_swigregister(GC_MakeCircle)

class GC_MakeConicalSurface(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * A2 defines the local coordinate system of the conical surface. Ang is the conical surface semi-angle ]0, PI/2[. Radius is the radius of the circle Viso in the placement plane of the conical surface defined with 'XAxis' and 'YAxis'. The 'ZDirection' of A2 defines the direction of the surface's axis of symmetry. If the location point of A2 is the apex of the surface Radius = 0 . At the creation the parametrization of the surface is defined such that the normal Vector (N = D1U ^ D1V) is oriented towards the 'outside region' of the surface. Status is 'NegativeRadius' if Radius < 0.0 or 'BadAngle' if Ang < Resolution from gp or Ang >= PI/ - Resolution
        	:param A2:
        	:type A2: gp_Ax2
        	:param Ang:
        	:type Ang: float
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Creates a ConicalSurface from a non persistent Cone from package gp.
        	:param C:
        	:type C: gp_Cone
        	:rtype: None* Make a ConicalSurface from Geom <TheCone> passing through 3 Pnt <P1>,<P2>,<P3>. Its axis is <P1P2> and the radius of its base is the distance between <P3> and <P1P2>. The distance between <P4> and <P1P2> is the radius of the section passing through <P4>. An error iss raised if <P1>,<P2>,<P3>,<P4> are colinear or if <P3P4> is perpendicular to <P1P2> or <P3P4> is colinear to <P1P2>.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:param P4:
        	:type P4: gp_Pnt
        	:rtype: None* Make a ConicalSurface with two points and two radius. The axis of the solution is the line passing through <P1> and <P2>. <R1> is the radius of the section passing through <P1> and <R2> the radius of the section passing through <P2>.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param R1:
        	:type R1: float
        	:param R2:
        	:type R2: float
        	:rtype: None
        """
        _GC.GC_MakeConicalSurface_swiginit(self, _GC.new_GC_MakeConicalSurface(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeConicalSurface_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeConicalSurface

# Register GC_MakeConicalSurface in _GC:
_GC.GC_MakeConicalSurface_swigregister(GC_MakeConicalSurface)

class GC_MakeCylindricalSurface(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * A2 defines the local coordinate system of the cylindrical surface. The 'ZDirection' of A2 defines the direction of the surface's axis of symmetry. At the creation the parametrization of the surface is defined such that the normal Vector (N = D1U ^ D1V) is oriented towards the 'outside region' of the surface. Warnings : It is not forbidden to create a cylindrical surface with Radius = 0.0 Status is 'NegativeRadius' if Radius < 0.0
        	:param A2:
        	:type A2: gp_Ax2
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Creates a CylindricalSurface from a non persistent Cylinder from package gp.
        	:param C:
        	:type C: gp_Cylinder
        	:rtype: None* Make a CylindricalSurface from Geom <TheCylinder> parallel to another CylindricalSurface <Cylinder> and passing through a Pnt <Point>.
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param Point:
        	:type Point: gp_Pnt
        	:rtype: None* Make a CylindricalSurface from Geom <TheCylinder> parallel to another CylindricalSurface <Cylinder> at the distance <Dist> which can be greater or lower than zero. The radius of the result is the absolute value of the radius of <Cyl> plus <Dist>
        	:param Cyl:
        	:type Cyl: gp_Cylinder
        	:param Dist:
        	:type Dist: float
        	:rtype: None* Make a CylindricalSurface from Geom <TheCylinder> passing through 3 Pnt <P1>,<P2>,<P3>. Its axis is <P1P2> and its radius is the distance between <P3> and <P1P2>
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:rtype: None* Make a CylindricalSurface by its axis <Axis> and radius <Radius>.
        	:param Axis:
        	:type Axis: gp_Ax1
        	:param Radius:
        	:type Radius: float
        	:rtype: None* Make a CylindricalSurface by its circular base.
        	:param Circ:
        	:type Circ: gp_Circ
        	:rtype: None
        """
        _GC.GC_MakeCylindricalSurface_swiginit(self, _GC.new_GC_MakeCylindricalSurface(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeCylindricalSurface_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeCylindricalSurface

# Register GC_MakeCylindricalSurface in _GC:
_GC.GC_MakeCylindricalSurface_swigregister(GC_MakeCylindricalSurface)

class GC_MakeEllipse(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an ellipse from a non persistent ellipse E from package gp by its conversion.
        	:param E:
        	:type E: gp_Elips
        	:rtype: None* Constructs an ellipse with major and minor radii MajorRadius and MinorRadius, and located in the plane defined by the 'X Axis' and 'Y Axis' of the coordinate system A2, where: - its center is the origin of A2, and - its major axis is the 'X Axis' of A2; Warnings : The MakeEllipse class does not prevent the construction of an ellipse where MajorRadius is equal to MinorRadius. If an error occurs (that is, when IsDone returns false), the Status function returns: - gce_InvertRadius if MajorRadius is less than MinorRadius; - gce_NegativeRadius if MinorRadius is less than 0.0; - gce_NullAxis if the points S1 and Center are coincident; or - gce_InvertAxis if: - the major radius computed with Center and S1 is less than the minor radius computed with Center, S1 and S2, or - Center, S1 and S2 are collinear.
        	:param A2:
        	:type A2: gp_Ax2
        	:param MajorRadius:
        	:type MajorRadius: float
        	:param MinorRadius:
        	:type MinorRadius: float
        	:rtype: None* Constructs an ellipse centered on the point Center, where - the plane of the ellipse is defined by Center, S1 and S2, - its major axis is defined by Center and S1, - its major radius is the distance between Center and S1, and - its minor radius is the distance between S2 and the major axis.
        	:param S1:
        	:type S1: gp_Pnt
        	:param S2:
        	:type S2: gp_Pnt
        	:param Center:
        	:type Center: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeEllipse_swiginit(self, _GC.new_GC_MakeEllipse(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeEllipse_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeEllipse

# Register GC_MakeEllipse in _GC:
_GC.GC_MakeEllipse_swigregister(GC_MakeEllipse)

class GC_MakeHyperbola(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an Hyperbola from a non persistent hyperbola from package gp by conversion.
        	:param H:
        	:type H: gp_Hypr
        	:rtype: None* Constructs a hyperbola centered on the origin of the coordinate system A2, with major and minor radii MajorRadius and MinorRadius, where: the plane of the hyperbola is defined by the 'X Axis' and 'Y Axis' of A2, - its major axis is the 'X Axis' of A2.
        	:param A2:
        	:type A2: gp_Ax2
        	:param MajorRadius:
        	:type MajorRadius: float
        	:param MinorRadius:
        	:type MinorRadius: float
        	:rtype: None* Constructs a hyperbola centered on the point Center, where - the plane of the hyperbola is defined by Center, S1 and S2, - its major axis is defined by Center and S1, - its major radius is the distance between Center and S1, and - its minor radius is the distance between S2 and the major axis;
        	:param S1:
        	:type S1: gp_Pnt
        	:param S2:
        	:type S2: gp_Pnt
        	:param Center:
        	:type Center: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeHyperbola_swiginit(self, _GC.new_GC_MakeHyperbola(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeHyperbola_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeHyperbola

# Register GC_MakeHyperbola in _GC:
_GC.GC_MakeHyperbola_swigregister(GC_MakeHyperbola)

class GC_MakeLine(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates a line located in 3D space with the axis placement A1. The Location of A1 is the origin of the line.
        	:param A1:
        	:type A1: gp_Ax1
        	:rtype: None* Creates a line from a non persistent line from package gp.
        	:param L:
        	:type L: gp_Lin
        	:rtype: None* P is the origin and V is the direction of the line.
        	:param P:
        	:type P: gp_Pnt
        	:param V:
        	:type V: gp_Dir
        	:rtype: None* Make a Line from Geom <TheLin> parallel to another Lin <Lin> and passing through a Pnt <Point>.
        	:param Lin:
        	:type Lin: gp_Lin
        	:param Point:
        	:type Point: gp_Pnt
        	:rtype: None* Make a Line from Geom <TheLin> passing through 2 Pnt <P1>,<P2>. It returns false if <p1> and <P2> are confused. Warning If the points P1 and P2 are coincident (that is, when IsDone returns false), the Status function returns gce_ConfusedPoints.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeLine_swiginit(self, _GC.new_GC_MakeLine(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeLine_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeLine

# Register GC_MakeLine in _GC:
_GC.GC_MakeLine_swigregister(GC_MakeLine)

class GC_MakePlane(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates a plane from a non persistent plane from package gp.
        	:param Pl:
        	:type Pl: gp_Pln
        	:rtype: None* P is the 'Location' point or origin of the plane. V is the direction normal to the plane.
        	:param P:
        	:type P: gp_Pnt
        	:param V:
        	:type V: gp_Dir
        	:rtype: None* Creates a plane from its cartesian equation : Ax + By + Cz + D = 0.0 Status is 'BadEquation' if Sqrt (A*A + B*B + C*C) <= Resolution from gp
        	:param A:
        	:type A: float
        	:param B:
        	:type B: float
        	:param C:
        	:type C: float
        	:param D:
        	:type D: float
        	:rtype: None* Make a Plane from Geom <ThePlane> parallel to another Pln <Pln> and passing through a Pnt <Point>.
        	:param Pln:
        	:type Pln: gp_Pln
        	:param Point:
        	:type Point: gp_Pnt
        	:rtype: None* Make a Plane from Geom <ThePlane> parallel to another Pln <Pln> at the distance <Dist> which can be greater or lower than zero. In the first case the result is at the distance <Dist> to the plane <Pln> in the direction of the normal to <Pln>. Otherwize it is in the oposite direction.
        	:param Pln:
        	:type Pln: gp_Pln
        	:param Dist:
        	:type Dist: float
        	:rtype: None* Make a Plane from Geom <ThePlane> passing through 3 Pnt <P1>,<P2>,<P3>. It returns false if <P1> <P2> <P3> are confused.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:rtype: None* Make a Plane passing through the location of <Axis>and normal to the Direction of <Axis>.
        	:param Axis:
        	:type Axis: gp_Ax1
        	:rtype: None
        """
        _GC.GC_MakePlane_swiginit(self, _GC.new_GC_MakePlane(*args))
    Value = _swig_new_instance_method(_GC.GC_MakePlane_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakePlane

# Register GC_MakePlane in _GC:
_GC.GC_MakePlane_swigregister(GC_MakePlane)

class GC_MakeSegment(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Make a segment of Line from the 2 points <P1> and <P2>. It returns NullObject if <P1> and <P2> are confused.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:rtype: None* Make a segment of Line from the line <Line1> between the two parameters U1 and U2. It returns NullObject if <U1> is equal <U2>.
        	:param Line:
        	:type Line: gp_Lin
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:rtype: None* Make a segment of Line from the line <Line1> between the point <Point> and the parameter Ulast. It returns NullObject if <U1> is equal <U2>.
        	:param Line:
        	:type Line: gp_Lin
        	:param Point:
        	:type Point: gp_Pnt
        	:param Ulast:
        	:type Ulast: float
        	:rtype: None* Make a segment of Line from the line <Line1> between the two points <P1> and <P2>. It returns NullObject if <U1> is equal <U2>.
        	:param Line:
        	:type Line: gp_Lin
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:rtype: None
        """
        _GC.GC_MakeSegment_swiginit(self, _GC.new_GC_MakeSegment(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeSegment_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeSegment

# Register GC_MakeSegment in _GC:
_GC.GC_MakeSegment_swigregister(GC_MakeSegment)

class GC_MakeTrimmedCone(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Make a RectangularTrimmedSurface <TheCone> from Geom It is trimmed by P3 and P4. Its axis is <P1P2> and the radius of its base is the distance between <P3> and <P1P2>. The distance between <P4> and <P1P2> is the radius of the section passing through <P4>. An error iss raised if <P1>,<P2>,<P3>,<P4> are colinear or if <P3P4> is perpendicular to <P1P2> or <P3P4> is colinear to <P1P2>.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:param P4:
        	:type P4: gp_Pnt
        	:rtype: None* Make a RectangularTrimmedSurface from Geom <TheCone> from a cone and trimmed by two points P1 and P2 and the two radius <R1> and <R2> of the sections passing through <P1> an <P2>. Warning If an error occurs (that is, when IsDone returns false), the Status function returns: - gce_ConfusedPoints if points P1 and P2, or P3 and P4, are coincident; - gce_NullAngle if: - the lines joining P1 to P2 and P3 to P4 are parallel, or - R1 and R2 are equal (i.e. their difference is less than gp::Resolution()); - gce_NullRadius if: - the line joining P1 to P2 is perpendicular to the line joining P3 to P4, or - the points P1, P2, P3 and P4 are collinear; - gce_NegativeRadius if R1 or R2 is negative; or - gce_NullAxis if points P1 and P2 are coincident (2nd syntax only).
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param R1:
        	:type R1: float
        	:param R2:
        	:type R2: float
        	:rtype: None
        """
        _GC.GC_MakeTrimmedCone_swiginit(self, _GC.new_GC_MakeTrimmedCone(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeTrimmedCone_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeTrimmedCone

# Register GC_MakeTrimmedCone in _GC:
_GC.GC_MakeTrimmedCone_swigregister(GC_MakeTrimmedCone)

class GC_MakeTrimmedCylinder(GC_Root):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Make a cylindricalSurface <Cyl> from Geom Its axis is is <P1P2> and its radius is the distance between <P3> and <P1P2>. The height is the distance between P1 and P2.
        	:param P1:
        	:type P1: gp_Pnt
        	:param P2:
        	:type P2: gp_Pnt
        	:param P3:
        	:type P3: gp_Pnt
        	:rtype: None* Make a cylindricalSurface <Cyl> from gp by its base <Circ>. Its axis is the normal to the plane defined bi <Circ>. <Height> can be greater than zero or lower than zero. In the first case the V parametric direction of the result has the same orientation as the normal to <Circ>. In the other case it has the opposite orientation.
        	:param Circ:
        	:type Circ: gp_Circ
        	:param Height:
        	:type Height: float
        	:rtype: None* Make a cylindricalSurface <Cyl> from gp by its axis <A1> and its radius <Radius>. It returns NullObject if <Radius> is lower than zero. <Height> can be greater than zero or lower than zero. In the first case the V parametric direction of the result has the same orientation as <A1>. In the other case it has the opposite orientation.
        	:param A1:
        	:type A1: gp_Ax1
        	:param Radius:
        	:type Radius: float
        	:param Height:
        	:type Height: float
        	:rtype: None
        """
        _GC.GC_MakeTrimmedCylinder_swiginit(self, _GC.new_GC_MakeTrimmedCylinder(*args))
    Value = _swig_new_instance_method(_GC.GC_MakeTrimmedCylinder_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GC.delete_GC_MakeTrimmedCylinder

# Register GC_MakeTrimmedCylinder in _GC:
_GC.GC_MakeTrimmedCylinder_swigregister(GC_MakeTrimmedCylinder)


