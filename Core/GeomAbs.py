# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GeomAbs module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geomabs.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GeomAbs
else:
    import _GeomAbs

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GeomAbs.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GeomAbs.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GeomAbs.delete_SwigPyIterator
    value = _swig_new_instance_method(_GeomAbs.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GeomAbs.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GeomAbs.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GeomAbs.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GeomAbs.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GeomAbs.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GeomAbs.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GeomAbs.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GeomAbs.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GeomAbs.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GeomAbs:
_GeomAbs.SwigPyIterator_swigregister(SwigPyIterator)


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
GeomAbs_IsoU = _GeomAbs.GeomAbs_IsoU
GeomAbs_IsoV = _GeomAbs.GeomAbs_IsoV
GeomAbs_NoneIso = _GeomAbs.GeomAbs_NoneIso
GeomAbs_Arc = _GeomAbs.GeomAbs_Arc
GeomAbs_Tangent = _GeomAbs.GeomAbs_Tangent
GeomAbs_Intersection = _GeomAbs.GeomAbs_Intersection
GeomAbs_Plane = _GeomAbs.GeomAbs_Plane
GeomAbs_Cylinder = _GeomAbs.GeomAbs_Cylinder
GeomAbs_Cone = _GeomAbs.GeomAbs_Cone
GeomAbs_Sphere = _GeomAbs.GeomAbs_Sphere
GeomAbs_Torus = _GeomAbs.GeomAbs_Torus
GeomAbs_BezierSurface = _GeomAbs.GeomAbs_BezierSurface
GeomAbs_BSplineSurface = _GeomAbs.GeomAbs_BSplineSurface
GeomAbs_SurfaceOfRevolution = _GeomAbs.GeomAbs_SurfaceOfRevolution
GeomAbs_SurfaceOfExtrusion = _GeomAbs.GeomAbs_SurfaceOfExtrusion
GeomAbs_OffsetSurface = _GeomAbs.GeomAbs_OffsetSurface
GeomAbs_OtherSurface = _GeomAbs.GeomAbs_OtherSurface
GeomAbs_Line = _GeomAbs.GeomAbs_Line
GeomAbs_Circle = _GeomAbs.GeomAbs_Circle
GeomAbs_Ellipse = _GeomAbs.GeomAbs_Ellipse
GeomAbs_Hyperbola = _GeomAbs.GeomAbs_Hyperbola
GeomAbs_Parabola = _GeomAbs.GeomAbs_Parabola
GeomAbs_BezierCurve = _GeomAbs.GeomAbs_BezierCurve
GeomAbs_BSplineCurve = _GeomAbs.GeomAbs_BSplineCurve
GeomAbs_OffsetCurve = _GeomAbs.GeomAbs_OffsetCurve
GeomAbs_OtherCurve = _GeomAbs.GeomAbs_OtherCurve
GeomAbs_PlanarForm = _GeomAbs.GeomAbs_PlanarForm
GeomAbs_ConicalForm = _GeomAbs.GeomAbs_ConicalForm
GeomAbs_CylindricalForm = _GeomAbs.GeomAbs_CylindricalForm
GeomAbs_ToroidalForm = _GeomAbs.GeomAbs_ToroidalForm
GeomAbs_SphericalForm = _GeomAbs.GeomAbs_SphericalForm
GeomAbs_RevolutionForm = _GeomAbs.GeomAbs_RevolutionForm
GeomAbs_RuledForm = _GeomAbs.GeomAbs_RuledForm
GeomAbs_QuadricForm = _GeomAbs.GeomAbs_QuadricForm
GeomAbs_OtherSurfaceForm = _GeomAbs.GeomAbs_OtherSurfaceForm
GeomAbs_C0 = _GeomAbs.GeomAbs_C0
GeomAbs_G1 = _GeomAbs.GeomAbs_G1
GeomAbs_C1 = _GeomAbs.GeomAbs_C1
GeomAbs_G2 = _GeomAbs.GeomAbs_G2
GeomAbs_C2 = _GeomAbs.GeomAbs_C2
GeomAbs_C3 = _GeomAbs.GeomAbs_C3
GeomAbs_CN = _GeomAbs.GeomAbs_CN
GeomAbs_NonUniform = _GeomAbs.GeomAbs_NonUniform
GeomAbs_Uniform = _GeomAbs.GeomAbs_Uniform
GeomAbs_QuasiUniform = _GeomAbs.GeomAbs_QuasiUniform
GeomAbs_PiecewiseBezier = _GeomAbs.GeomAbs_PiecewiseBezier
GeomAbs_PolylineForm = _GeomAbs.GeomAbs_PolylineForm
GeomAbs_CircularForm = _GeomAbs.GeomAbs_CircularForm
GeomAbs_EllipticForm = _GeomAbs.GeomAbs_EllipticForm
GeomAbs_HyperbolicForm = _GeomAbs.GeomAbs_HyperbolicForm
GeomAbs_ParabolicForm = _GeomAbs.GeomAbs_ParabolicForm
GeomAbs_OtherCurveForm = _GeomAbs.GeomAbs_OtherCurveForm
GeomAbs_SameUV = _GeomAbs.GeomAbs_SameUV
GeomAbs_SameU = _GeomAbs.GeomAbs_SameU
GeomAbs_SameV = _GeomAbs.GeomAbs_SameV
GeomAbs_OppositeUV = _GeomAbs.GeomAbs_OppositeUV


