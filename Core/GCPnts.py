# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
GCPnts module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_gcpnts.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GCPnts
else:
    import _GCPnts

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _GCPnts.SWIG_PyInstanceMethod_New
_swig_new_static_method = _GCPnts.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _GCPnts.delete_SwigPyIterator
    value = _swig_new_instance_method(_GCPnts.SwigPyIterator_value)
    incr = _swig_new_instance_method(_GCPnts.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_GCPnts.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_GCPnts.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_GCPnts.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_GCPnts.SwigPyIterator_copy)
    next = _swig_new_instance_method(_GCPnts.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_GCPnts.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_GCPnts.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_GCPnts.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GCPnts:
_GCPnts.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Adaptor3d
import OCC.Core.Geom
import OCC.Core.gp
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.TopAbs
import OCC.Core.Adaptor2d
import OCC.Core.Geom2d
import OCC.Core.math
import OCC.Core.Message
GCPnts_Linear = _GCPnts.GCPnts_Linear
GCPnts_Circular = _GCPnts.GCPnts_Circular
GCPnts_Curved = _GCPnts.GCPnts_Curved
GCPnts_DefComposite = _GCPnts.GCPnts_DefComposite
GCPnts_LengthParametrized = _GCPnts.GCPnts_LengthParametrized
GCPnts_Parametrized = _GCPnts.GCPnts_Parametrized
GCPnts_AbsComposite = _GCPnts.GCPnts_AbsComposite
class GCPnts_AbscissaPoint(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>.
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0> with the given tolerance.
        	:param Tol:
        	:type Tol: float
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0> with the given tolerance.
        	:param Tol:
        	:type Tol: float
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>. <Ui> is the starting value used in the iterative process which find the solution, it must be close to the final solution
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:param Ui:
        	:type Ui: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>. <Ui> is the starting value used in the iterative process which find the solution, it must be closed to the final solution
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:param Ui:
        	:type Ui: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>. <Ui> is the starting value used in the iterative process which find the solution, it must be close to the final solution
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:param Ui:
        	:type Ui: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None* the algorithm computes a point on a curve <Curve> at the distance <Abscissa> from the point of parameter <U0>. <Ui> is the starting value used in the iterative process which find the solution, it must be close to the final solution
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param U0:
        	:type U0: float
        	:param Ui:
        	:type Ui: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _GCPnts.GCPnts_AbscissaPoint_swiginit(self, _GCPnts.new_GCPnts_AbscissaPoint(*args))
    IsDone = _swig_new_instance_method(_GCPnts.GCPnts_AbscissaPoint_IsDone)
    Length = _swig_new_static_method(_GCPnts.GCPnts_AbscissaPoint_Length)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_AbscissaPoint_Parameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_AbscissaPoint

# Register GCPnts_AbscissaPoint in _GCPnts:
_GCPnts.GCPnts_AbscissaPoint_swigregister(GCPnts_AbscissaPoint)
GCPnts_AbscissaPoint_Length = _GCPnts.GCPnts_AbscissaPoint_Length

class GCPnts_DistFunction2dMV(OCC.Core.math.math_MultipleVarFunction):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theCurvLinDist:
        	:type theCurvLinDist: GCPnts_DistFunction2d
        	:rtype: None
        """
        _GCPnts.GCPnts_DistFunction2dMV_swiginit(self, _GCPnts.new_GCPnts_DistFunction2dMV(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_DistFunction2dMV

# Register GCPnts_DistFunction2dMV in _GCPnts:
_GCPnts.GCPnts_DistFunction2dMV_swigregister(GCPnts_DistFunction2dMV)

class GCPnts_DistFunctionMV(OCC.Core.math.math_MultipleVarFunction):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theCurvLinDist:
        	:type theCurvLinDist: GCPnts_DistFunction
        	:rtype: None
        """
        _GCPnts.GCPnts_DistFunctionMV_swiginit(self, _GCPnts.new_GCPnts_DistFunctionMV(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_DistFunctionMV

# Register GCPnts_DistFunctionMV in _GCPnts:
_GCPnts.GCPnts_DistFunctionMV_swigregister(GCPnts_DistFunctionMV)

class GCPnts_QuasiUniformAbscissa(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructs an empty algorithm. To define the problem to be solved, use the function Initialize.
        	:rtype: None* Computes a uniform abscissa distribution of points - on the curve C where Abscissa is the curvilinear distance between two consecutive points of the distribution.
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param NbPoints:
        	:type NbPoints: int
        	:rtype: None* Computes a uniform abscissa distribution of points on the part of curve C limited by the two parameter values U1 and U2, where Abscissa is the curvilinear distance between two consecutive points of the distribution. The first point of the distribution is either the origin of curve C or the point of parameter U1. The following points are computed such that the curvilinear distance between two consecutive points is equal to Abscissa. The last point of the distribution is either the end point of curve C or the point of parameter U2. However the curvilinear distance between this last point and the point just preceding it in the distribution is, of course, generally not equal to Abscissa. Use the function IsDone to verify that the computation was successful, the function NbPoints to obtain the number of points of the computed distribution, and the function Parameter to read the parameter of each point. Warning The roles of U1 and U2 are inverted if U1 > U2 . Warning C is an adapted curve, that is, an object which is an interface between: - the services provided by either a 2D curve from the package Geom2d (in the case of an Adaptor2d_Curve2d curve) or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve), - and those required on the curve by the computation algorithm.
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param NbPoints:
        	:type NbPoints: int
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:rtype: None* Computes a uniform abscissa distribution of points on the Curve2d <C>. <NbPoints> defines the nomber of desired points.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param NbPoints:
        	:type NbPoints: int
        	:rtype: None* Computes a Uniform abscissa distribution of points on a part of the Curve2d <C>.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param NbPoints:
        	:type NbPoints: int
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:rtype: None
        """
        _GCPnts.GCPnts_QuasiUniformAbscissa_swiginit(self, _GCPnts.new_GCPnts_QuasiUniformAbscissa(*args))
    Initialize = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformAbscissa_Initialize)
    IsDone = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformAbscissa_IsDone)
    NbPoints = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformAbscissa_NbPoints)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformAbscissa_Parameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_QuasiUniformAbscissa

# Register GCPnts_QuasiUniformAbscissa in _GCPnts:
_GCPnts.GCPnts_QuasiUniformAbscissa_swigregister(GCPnts_QuasiUniformAbscissa)

class GCPnts_QuasiUniformDeflection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Deflection = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_Deflection)

    def __init__(self, *args):
        r"""
        * Constructs an empty algorithm. To define the problem to be solved, use the function Initialize.
        	:rtype: None* Computes a QuasiUniform Deflection distribution of points on the Curve <C>.
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Deflection:
        	:type Deflection: float
        	:param Continuity: default value is GeomAbs_C1
        	:type Continuity: GeomAbs_Shape
        	:rtype: None* Computes a QuasiUniform Deflection distribution of points on the Curve <C>.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Deflection:
        	:type Deflection: float
        	:param Continuity: default value is GeomAbs_C1
        	:type Continuity: GeomAbs_Shape
        	:rtype: None* Computes a QuasiUniform Deflection distribution of points on a part of the Curve <C>.
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Deflection:
        	:type Deflection: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Continuity: default value is GeomAbs_C1
        	:type Continuity: GeomAbs_Shape
        	:rtype: None* Computes a QuasiUniform Deflection distribution of points on a part of the Curve <C>. This and the above algorithms compute a distribution of points: - on the curve C, or - on the part of curve C limited by the two parameter values U1 and U2, where the deflection resulting from the distributed points is not greater than Deflection. The first point of the distribution is either the origin of curve C or the point of parameter U1. The last point of the distribution is either the end point of curve C or the point of parameter U2. Intermediate points of the distribution are built such that the deflection is not greater than Deflection. Using the following evaluation of the deflection: if Pi and Pj are two consecutive points of the distribution, respectively of parameter ui and uj on the curve, the deflection is the distance between: - the mid-point of Pi and Pj (the center of the chord joining these two points) - and the point of mid-parameter of these two points (the point of parameter [(ui+uj) / 2 ] on curve C). Continuity, defaulted to GeomAbs_C1, gives the degree of continuity of the curve C. (Note that C is an Adaptor3d_Curve or an Adaptor2d_Curve2d object, and does not know the degree of continuity of the underlying curve). Use the function IsDone to verify that the computation was successful, the function NbPoints to obtain the number of points of the computed distribution, and the function Parameter to read the parameter of each point. Warning - The roles of U1 and U2 are inverted if U1 > U2. - Derivative functions on the curve are called according to Continuity. An error may occur if Continuity is greater than the real degree of continuity of the curve. Warning C is an adapted curve, i.e. an object which is an interface between: - the services provided by either a 2D curve from the package Geom2d (in the case of an Adaptor2d_Curve2d curve) or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve), - and those required on the curve by the computation algorithm.
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Deflection:
        	:type Deflection: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Continuity: default value is GeomAbs_C1
        	:type Continuity: GeomAbs_Shape
        	:rtype: None
        """
        _GCPnts.GCPnts_QuasiUniformDeflection_swiginit(self, _GCPnts.new_GCPnts_QuasiUniformDeflection(*args))
    Initialize = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_Initialize)
    IsDone = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_IsDone)
    NbPoints = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_NbPoints)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_Parameter)
    Value = _swig_new_instance_method(_GCPnts.GCPnts_QuasiUniformDeflection_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_QuasiUniformDeflection

# Register GCPnts_QuasiUniformDeflection in _GCPnts:
_GCPnts.GCPnts_QuasiUniformDeflection_swigregister(GCPnts_QuasiUniformDeflection)

class GCPnts_TangentialDeflection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddPoint = _swig_new_instance_method(_GCPnts.GCPnts_TangentialDeflection_AddPoint)
    ArcAngularStep = _swig_new_static_method(_GCPnts.GCPnts_TangentialDeflection_ArcAngularStep)

    def __init__(self, *args):
        r"""
        :rtype: None:param C:
        	:type C: Adaptor3d_Curve
        	:param AngularDeflection:
        	:type AngularDeflection: float
        	:param CurvatureDeflection:
        	:type CurvatureDeflection: float
        	:param MinimumOfPoints: default value is 2
        	:type MinimumOfPoints: int
        	:param UTol: default value is 1.0e-9
        	:type UTol: float
        	:param theMinLen: default value is 1.0e-7
        	:type theMinLen: float
        	:rtype: None:param C:
        	:type C: Adaptor3d_Curve
        	:param FirstParameter:
        	:type FirstParameter: float
        	:param LastParameter:
        	:type LastParameter: float
        	:param AngularDeflection:
        	:type AngularDeflection: float
        	:param CurvatureDeflection:
        	:type CurvatureDeflection: float
        	:param MinimumOfPoints: default value is 2
        	:type MinimumOfPoints: int
        	:param UTol: default value is 1.0e-9
        	:type UTol: float
        	:param theMinLen: default value is 1.0e-7
        	:type theMinLen: float
        	:rtype: None:param C:
        	:type C: Adaptor2d_Curve2d
        	:param AngularDeflection:
        	:type AngularDeflection: float
        	:param CurvatureDeflection:
        	:type CurvatureDeflection: float
        	:param MinimumOfPoints: default value is 2
        	:type MinimumOfPoints: int
        	:param UTol: default value is 1.0e-9
        	:type UTol: float
        	:param theMinLen: default value is 1.0e-7
        	:type theMinLen: float
        	:rtype: None:param C:
        	:type C: Adaptor2d_Curve2d
        	:param FirstParameter:
        	:type FirstParameter: float
        	:param LastParameter:
        	:type LastParameter: float
        	:param AngularDeflection:
        	:type AngularDeflection: float
        	:param CurvatureDeflection:
        	:type CurvatureDeflection: float
        	:param MinimumOfPoints: default value is 2
        	:type MinimumOfPoints: int
        	:param UTol: default value is 1.0e-9
        	:type UTol: float
        	:param theMinLen: default value is 1.0e-7
        	:type theMinLen: float
        	:rtype: None
        """
        _GCPnts.GCPnts_TangentialDeflection_swiginit(self, _GCPnts.new_GCPnts_TangentialDeflection(*args))
    Initialize = _swig_new_instance_method(_GCPnts.GCPnts_TangentialDeflection_Initialize)
    NbPoints = _swig_new_instance_method(_GCPnts.GCPnts_TangentialDeflection_NbPoints)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_TangentialDeflection_Parameter)
    Value = _swig_new_instance_method(_GCPnts.GCPnts_TangentialDeflection_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_TangentialDeflection

# Register GCPnts_TangentialDeflection in _GCPnts:
_GCPnts.GCPnts_TangentialDeflection_swigregister(GCPnts_TangentialDeflection)
GCPnts_TangentialDeflection_ArcAngularStep = _GCPnts.GCPnts_TangentialDeflection_ArcAngularStep

class GCPnts_UniformAbscissa(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Abscissa = _swig_new_instance_method(_GCPnts.GCPnts_UniformAbscissa_Abscissa)

    def __init__(self, *args):
        r"""
        * creation of a indefinite UniformAbscissa
        	:rtype: None* Computes a uniform abscissa distribution of points on the Curve <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a Uniform abscissa distribution of points on a part of the Curve <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Abscissa:
        	:type Abscissa: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a uniform abscissa distribution of points on the Curve <C>. <NbPoints> defines the nomber of desired points. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param NbPoints:
        	:type NbPoints: int
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a Uniform abscissa distribution of points on a part of the Curve <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param NbPoints:
        	:type NbPoints: int
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a uniform abscissa distribution of points on the Curve2d <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a Uniform abscissa distribution of points on a part of the Curve2d <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Abscissa:
        	:type Abscissa: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a uniform abscissa distribution of points on the Curve2d <C>. <NbPoints> defines the nomber of desired points. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param NbPoints:
        	:type NbPoints: int
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None* Computes a Uniform abscissa distribution of points on a part of the Curve2d <C>. Parameter Toler is equal Precision::Confusion by default. It Is used for more precise calculation of curve length
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param NbPoints:
        	:type NbPoints: int
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param Toler: default value is -1
        	:type Toler: float
        	:rtype: None
        """
        _GCPnts.GCPnts_UniformAbscissa_swiginit(self, _GCPnts.new_GCPnts_UniformAbscissa(*args))
    Initialize = _swig_new_instance_method(_GCPnts.GCPnts_UniformAbscissa_Initialize)
    IsDone = _swig_new_instance_method(_GCPnts.GCPnts_UniformAbscissa_IsDone)
    NbPoints = _swig_new_instance_method(_GCPnts.GCPnts_UniformAbscissa_NbPoints)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_UniformAbscissa_Parameter)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_UniformAbscissa

# Register GCPnts_UniformAbscissa in _GCPnts:
_GCPnts.GCPnts_UniformAbscissa_swigregister(GCPnts_UniformAbscissa)

class GCPnts_UniformDeflection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Deflection = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_Deflection)

    def __init__(self, *args):
        r"""
        * Constructs an empty algorithm. To define the problem to be solved, use the function Initialize.
        	:rtype: None* Computes a uniform Deflection distribution of points on the Curve <C>. if <WithControl> is True,the algorithm controls the estimate deflection
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Deflection:
        	:type Deflection: float
        	:param WithControl: default value is Standard_True
        	:type WithControl: bool
        	:rtype: None* Computes a uniform Deflection distribution of points on the Curve <C>. if <WithControl> is True,the algorithm controls the estimate deflection
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Deflection:
        	:type Deflection: float
        	:param WithControl: default value is Standard_True
        	:type WithControl: bool
        	:rtype: None* Computes a Uniform Deflection distribution of points on a part of the Curve <C>. if <WithControl> is True,the algorithm controls the estimate deflection
        	:param C:
        	:type C: Adaptor3d_Curve
        	:param Deflection:
        	:type Deflection: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param WithControl: default value is Standard_True
        	:type WithControl: bool
        	:rtype: None* Computes a Uniform Deflection distribution of points on a part of the Curve <C>. if <WithControl> is True,the algorithm controls the estimate deflection
        	:param C:
        	:type C: Adaptor2d_Curve2d
        	:param Deflection:
        	:type Deflection: float
        	:param U1:
        	:type U1: float
        	:param U2:
        	:type U2: float
        	:param WithControl: default value is Standard_True
        	:type WithControl: bool
        	:rtype: None
        """
        _GCPnts.GCPnts_UniformDeflection_swiginit(self, _GCPnts.new_GCPnts_UniformDeflection(*args))
    Initialize = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_Initialize)
    IsDone = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_IsDone)
    NbPoints = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_NbPoints)
    Parameter = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_Parameter)
    Value = _swig_new_instance_method(_GCPnts.GCPnts_UniformDeflection_Value)

    __repr__ = _dumps_object

    __swig_destroy__ = _GCPnts.delete_GCPnts_UniformDeflection

# Register GCPnts_UniformDeflection in _GCPnts:
_GCPnts.GCPnts_UniformDeflection_swigregister(GCPnts_UniformDeflection)



