# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BSplCLib module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_bsplclib.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BSplCLib
else:
    import _BSplCLib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BSplCLib.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BSplCLib.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BSplCLib.delete_SwigPyIterator
    value = _swig_new_instance_method(_BSplCLib.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BSplCLib.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BSplCLib.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BSplCLib.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BSplCLib.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BSplCLib.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BSplCLib.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BSplCLib.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BSplCLib.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BSplCLib.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BSplCLib:
_BSplCLib.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.math
import OCC.Core.Message
import OCC.Core.gp
import OCC.Core.TColgp
import OCC.Core.GeomAbs
BSplCLib_NonConstant = _BSplCLib.BSplCLib_NonConstant
BSplCLib_Constant = _BSplCLib.BSplCLib_Constant
BSplCLib_QuasiConstant = _BSplCLib.BSplCLib_QuasiConstant
BSplCLib_NonUniform = _BSplCLib.BSplCLib_NonUniform
BSplCLib_Uniform = _BSplCLib.BSplCLib_Uniform
Handle_BSplCLib_Cache_Create = _BSplCLib.Handle_BSplCLib_Cache_Create
Handle_BSplCLib_Cache_DownCast = _BSplCLib.Handle_BSplCLib_Cache_DownCast
Handle_BSplCLib_Cache_IsNull = _BSplCLib.Handle_BSplCLib_Cache_IsNull
class bsplclib(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AntiBoorScheme = _swig_new_static_method(_BSplCLib.bsplclib_AntiBoorScheme)
    Bohm = _swig_new_static_method(_BSplCLib.bsplclib_Bohm)
    BoorIndex = _swig_new_static_method(_BSplCLib.bsplclib_BoorIndex)
    BoorScheme = _swig_new_static_method(_BSplCLib.bsplclib_BoorScheme)
    BuildBSpMatrix = _swig_new_static_method(_BSplCLib.bsplclib_BuildBSpMatrix)
    BuildBoor = _swig_new_static_method(_BSplCLib.bsplclib_BuildBoor)
    BuildCache = _swig_new_static_method(_BSplCLib.bsplclib_BuildCache)
    BuildEval = _swig_new_static_method(_BSplCLib.bsplclib_BuildEval)
    BuildKnots = _swig_new_static_method(_BSplCLib.bsplclib_BuildKnots)
    BuildSchoenbergPoints = _swig_new_static_method(_BSplCLib.bsplclib_BuildSchoenbergPoints)
    CacheD0 = _swig_new_static_method(_BSplCLib.bsplclib_CacheD0)
    CacheD1 = _swig_new_static_method(_BSplCLib.bsplclib_CacheD1)
    CacheD2 = _swig_new_static_method(_BSplCLib.bsplclib_CacheD2)
    CacheD3 = _swig_new_static_method(_BSplCLib.bsplclib_CacheD3)
    CoefsD0 = _swig_new_static_method(_BSplCLib.bsplclib_CoefsD0)
    CoefsD1 = _swig_new_static_method(_BSplCLib.bsplclib_CoefsD1)
    CoefsD2 = _swig_new_static_method(_BSplCLib.bsplclib_CoefsD2)
    CoefsD3 = _swig_new_static_method(_BSplCLib.bsplclib_CoefsD3)
    D0 = _swig_new_static_method(_BSplCLib.bsplclib_D0)
    D1 = _swig_new_static_method(_BSplCLib.bsplclib_D1)
    D2 = _swig_new_static_method(_BSplCLib.bsplclib_D2)
    D3 = _swig_new_static_method(_BSplCLib.bsplclib_D3)
    Derivative = _swig_new_static_method(_BSplCLib.bsplclib_Derivative)
    Eval = _swig_new_static_method(_BSplCLib.bsplclib_Eval)
    EvalBsplineBasis = _swig_new_static_method(_BSplCLib.bsplclib_EvalBsplineBasis)
    FactorBandedMatrix = _swig_new_static_method(_BSplCLib.bsplclib_FactorBandedMatrix)
    FirstUKnotIndex = _swig_new_static_method(_BSplCLib.bsplclib_FirstUKnotIndex)
    FlatBezierKnots = _swig_new_static_method(_BSplCLib.bsplclib_FlatBezierKnots)
    FlatIndex = _swig_new_static_method(_BSplCLib.bsplclib_FlatIndex)
    FunctionMultiply = _swig_new_static_method(_BSplCLib.bsplclib_FunctionMultiply)
    FunctionReparameterise = _swig_new_static_method(_BSplCLib.bsplclib_FunctionReparameterise)
    GetPole = _swig_new_static_method(_BSplCLib.bsplclib_GetPole)
    Hunt = _swig_new_static_method(_BSplCLib.bsplclib_Hunt)
    IncreaseDegree = _swig_new_static_method(_BSplCLib.bsplclib_IncreaseDegree)
    IncreaseDegreeCountKnots = _swig_new_static_method(_BSplCLib.bsplclib_IncreaseDegreeCountKnots)
    InsertKnot = _swig_new_static_method(_BSplCLib.bsplclib_InsertKnot)
    InsertKnots = _swig_new_static_method(_BSplCLib.bsplclib_InsertKnots)
    Interpolate = _swig_new_static_method(_BSplCLib.bsplclib_Interpolate)
    IsRational = _swig_new_static_method(_BSplCLib.bsplclib_IsRational)
    KnotAnalysis = _swig_new_static_method(_BSplCLib.bsplclib_KnotAnalysis)
    KnotForm = _swig_new_static_method(_BSplCLib.bsplclib_KnotForm)
    KnotSequence = _swig_new_static_method(_BSplCLib.bsplclib_KnotSequence)
    KnotSequenceLength = _swig_new_static_method(_BSplCLib.bsplclib_KnotSequenceLength)
    Knots = _swig_new_static_method(_BSplCLib.bsplclib_Knots)
    KnotsLength = _swig_new_static_method(_BSplCLib.bsplclib_KnotsLength)
    LastUKnotIndex = _swig_new_static_method(_BSplCLib.bsplclib_LastUKnotIndex)
    LocateParameter = _swig_new_static_method(_BSplCLib.bsplclib_LocateParameter)
    MaxDegree = _swig_new_static_method(_BSplCLib.bsplclib_MaxDegree)
    MaxKnotMult = _swig_new_static_method(_BSplCLib.bsplclib_MaxKnotMult)
    MergeBSplineKnots = _swig_new_static_method(_BSplCLib.bsplclib_MergeBSplineKnots)
    MinKnotMult = _swig_new_static_method(_BSplCLib.bsplclib_MinKnotMult)
    MovePoint = _swig_new_static_method(_BSplCLib.bsplclib_MovePoint)
    MovePointAndTangent = _swig_new_static_method(_BSplCLib.bsplclib_MovePointAndTangent)
    MultForm = _swig_new_static_method(_BSplCLib.bsplclib_MultForm)
    NbPoles = _swig_new_static_method(_BSplCLib.bsplclib_NbPoles)
    NoMults = _swig_new_static_method(_BSplCLib.bsplclib_NoMults)
    NoWeights = _swig_new_static_method(_BSplCLib.bsplclib_NoWeights)
    PoleIndex = _swig_new_static_method(_BSplCLib.bsplclib_PoleIndex)
    PolesCoefficients = _swig_new_static_method(_BSplCLib.bsplclib_PolesCoefficients)
    PrepareInsertKnots = _swig_new_static_method(_BSplCLib.bsplclib_PrepareInsertKnots)
    PrepareTrimming = _swig_new_static_method(_BSplCLib.bsplclib_PrepareTrimming)
    PrepareUnperiodize = _swig_new_static_method(_BSplCLib.bsplclib_PrepareUnperiodize)
    RaiseMultiplicity = _swig_new_static_method(_BSplCLib.bsplclib_RaiseMultiplicity)
    RemoveKnot = _swig_new_static_method(_BSplCLib.bsplclib_RemoveKnot)
    Reparametrize = _swig_new_static_method(_BSplCLib.bsplclib_Reparametrize)
    Resolution = _swig_new_static_method(_BSplCLib.bsplclib_Resolution)
    Reverse = _swig_new_static_method(_BSplCLib.bsplclib_Reverse)
    SolveBandedSystem = _swig_new_static_method(_BSplCLib.bsplclib_SolveBandedSystem)
    TangExtendToConstraint = _swig_new_static_method(_BSplCLib.bsplclib_TangExtendToConstraint)
    Trimming = _swig_new_static_method(_BSplCLib.bsplclib_Trimming)
    Unperiodize = _swig_new_static_method(_BSplCLib.bsplclib_Unperiodize)

    __repr__ = _dumps_object


    def __init__(self):
        _BSplCLib.bsplclib_swiginit(self, _BSplCLib.new_bsplclib())
    __swig_destroy__ = _BSplCLib.delete_bsplclib

# Register bsplclib in _BSplCLib:
_BSplCLib.bsplclib_swigregister(bsplclib)
bsplclib_AntiBoorScheme = _BSplCLib.bsplclib_AntiBoorScheme
bsplclib_Bohm = _BSplCLib.bsplclib_Bohm
bsplclib_BoorIndex = _BSplCLib.bsplclib_BoorIndex
bsplclib_BoorScheme = _BSplCLib.bsplclib_BoorScheme
bsplclib_BuildBSpMatrix = _BSplCLib.bsplclib_BuildBSpMatrix
bsplclib_BuildBoor = _BSplCLib.bsplclib_BuildBoor
bsplclib_BuildCache = _BSplCLib.bsplclib_BuildCache
bsplclib_BuildEval = _BSplCLib.bsplclib_BuildEval
bsplclib_BuildKnots = _BSplCLib.bsplclib_BuildKnots
bsplclib_BuildSchoenbergPoints = _BSplCLib.bsplclib_BuildSchoenbergPoints
bsplclib_CacheD0 = _BSplCLib.bsplclib_CacheD0
bsplclib_CacheD1 = _BSplCLib.bsplclib_CacheD1
bsplclib_CacheD2 = _BSplCLib.bsplclib_CacheD2
bsplclib_CacheD3 = _BSplCLib.bsplclib_CacheD3
bsplclib_CoefsD0 = _BSplCLib.bsplclib_CoefsD0
bsplclib_CoefsD1 = _BSplCLib.bsplclib_CoefsD1
bsplclib_CoefsD2 = _BSplCLib.bsplclib_CoefsD2
bsplclib_CoefsD3 = _BSplCLib.bsplclib_CoefsD3
bsplclib_D0 = _BSplCLib.bsplclib_D0
bsplclib_D1 = _BSplCLib.bsplclib_D1
bsplclib_D2 = _BSplCLib.bsplclib_D2
bsplclib_D3 = _BSplCLib.bsplclib_D3
bsplclib_Derivative = _BSplCLib.bsplclib_Derivative
bsplclib_Eval = _BSplCLib.bsplclib_Eval
bsplclib_EvalBsplineBasis = _BSplCLib.bsplclib_EvalBsplineBasis
bsplclib_FactorBandedMatrix = _BSplCLib.bsplclib_FactorBandedMatrix
bsplclib_FirstUKnotIndex = _BSplCLib.bsplclib_FirstUKnotIndex
bsplclib_FlatBezierKnots = _BSplCLib.bsplclib_FlatBezierKnots
bsplclib_FlatIndex = _BSplCLib.bsplclib_FlatIndex
bsplclib_FunctionMultiply = _BSplCLib.bsplclib_FunctionMultiply
bsplclib_FunctionReparameterise = _BSplCLib.bsplclib_FunctionReparameterise
bsplclib_GetPole = _BSplCLib.bsplclib_GetPole
bsplclib_Hunt = _BSplCLib.bsplclib_Hunt
bsplclib_IncreaseDegree = _BSplCLib.bsplclib_IncreaseDegree
bsplclib_IncreaseDegreeCountKnots = _BSplCLib.bsplclib_IncreaseDegreeCountKnots
bsplclib_InsertKnot = _BSplCLib.bsplclib_InsertKnot
bsplclib_InsertKnots = _BSplCLib.bsplclib_InsertKnots
bsplclib_Interpolate = _BSplCLib.bsplclib_Interpolate
bsplclib_IsRational = _BSplCLib.bsplclib_IsRational
bsplclib_KnotAnalysis = _BSplCLib.bsplclib_KnotAnalysis
bsplclib_KnotForm = _BSplCLib.bsplclib_KnotForm
bsplclib_KnotSequence = _BSplCLib.bsplclib_KnotSequence
bsplclib_KnotSequenceLength = _BSplCLib.bsplclib_KnotSequenceLength
bsplclib_Knots = _BSplCLib.bsplclib_Knots
bsplclib_KnotsLength = _BSplCLib.bsplclib_KnotsLength
bsplclib_LastUKnotIndex = _BSplCLib.bsplclib_LastUKnotIndex
bsplclib_LocateParameter = _BSplCLib.bsplclib_LocateParameter
bsplclib_MaxDegree = _BSplCLib.bsplclib_MaxDegree
bsplclib_MaxKnotMult = _BSplCLib.bsplclib_MaxKnotMult
bsplclib_MergeBSplineKnots = _BSplCLib.bsplclib_MergeBSplineKnots
bsplclib_MinKnotMult = _BSplCLib.bsplclib_MinKnotMult
bsplclib_MovePoint = _BSplCLib.bsplclib_MovePoint
bsplclib_MovePointAndTangent = _BSplCLib.bsplclib_MovePointAndTangent
bsplclib_MultForm = _BSplCLib.bsplclib_MultForm
bsplclib_NbPoles = _BSplCLib.bsplclib_NbPoles
bsplclib_NoMults = _BSplCLib.bsplclib_NoMults
bsplclib_NoWeights = _BSplCLib.bsplclib_NoWeights
bsplclib_PoleIndex = _BSplCLib.bsplclib_PoleIndex
bsplclib_PolesCoefficients = _BSplCLib.bsplclib_PolesCoefficients
bsplclib_PrepareInsertKnots = _BSplCLib.bsplclib_PrepareInsertKnots
bsplclib_PrepareTrimming = _BSplCLib.bsplclib_PrepareTrimming
bsplclib_PrepareUnperiodize = _BSplCLib.bsplclib_PrepareUnperiodize
bsplclib_RaiseMultiplicity = _BSplCLib.bsplclib_RaiseMultiplicity
bsplclib_RemoveKnot = _BSplCLib.bsplclib_RemoveKnot
bsplclib_Reparametrize = _BSplCLib.bsplclib_Reparametrize
bsplclib_Resolution = _BSplCLib.bsplclib_Resolution
bsplclib_Reverse = _BSplCLib.bsplclib_Reverse
bsplclib_SolveBandedSystem = _BSplCLib.bsplclib_SolveBandedSystem
bsplclib_TangExtendToConstraint = _BSplCLib.bsplclib_TangExtendToConstraint
bsplclib_Trimming = _BSplCLib.bsplclib_Trimming
bsplclib_Unperiodize = _BSplCLib.bsplclib_Unperiodize

class BSplCLib_Cache(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Constructor, prepares data structures for caching values on a 2d curve. \param theDegree degree of the curve \param thePeriodic identify whether the curve is periodic \param theFlatKnots knots of Bezier/B-spline curve (with repetitions) \param thePoles2d array of poles of 2D curve \param theWeights array of weights of corresponding poles
        	:param theDegree:
        	:type theDegree: int
        	:param thePeriodic:
        	:type thePeriodic: bool
        	:param theFlatKnots:
        	:type theFlatKnots: TColStd_Array1OfReal
        	:param thePoles2d:
        	:type thePoles2d: TColgp_Array1OfPnt2d
        	:param theWeights: default value is NULL
        	:type theWeights: TColStd_Array1OfReal *
        	:rtype: None* Constructor, prepares data structures for caching values on a 3d curve. \param theDegree degree of the curve \param thePeriodic identify whether the curve is periodic \param theFlatKnots knots of Bezier/B-spline curve (with repetitions) \param thePoles array of poles of 3D curve \param theWeights array of weights of corresponding poles
        	:param theDegree:
        	:type theDegree: int
        	:param thePeriodic:
        	:type thePeriodic: bool
        	:param theFlatKnots:
        	:type theFlatKnots: TColStd_Array1OfReal
        	:param thePoles:
        	:type thePoles: TColgp_Array1OfPnt
        	:param theWeights: default value is NULL
        	:type theWeights: TColStd_Array1OfReal *
        	:rtype: None
        """
        _BSplCLib.BSplCLib_Cache_swiginit(self, _BSplCLib.new_BSplCLib_Cache(*args))
    BuildCache = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_BuildCache)
    D0 = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_D0)
    D1 = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_D1)
    D2 = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_D2)
    D3 = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_D3)
    IsCacheValid = _swig_new_instance_method(_BSplCLib.BSplCLib_Cache_IsCacheValid)


    @staticmethod
    def DownCast(t):
      return Handle_BSplCLib_Cache_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BSplCLib.delete_BSplCLib_Cache

# Register BSplCLib_Cache in _BSplCLib:
_BSplCLib.BSplCLib_Cache_swigregister(BSplCLib_Cache)

class BSplCLib_CacheParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SpanStart = property(_BSplCLib.BSplCLib_CacheParams_SpanStart_get, _BSplCLib.BSplCLib_CacheParams_SpanStart_set)
    SpanLength = property(_BSplCLib.BSplCLib_CacheParams_SpanLength_get, _BSplCLib.BSplCLib_CacheParams_SpanLength_set)
    SpanIndex = property(_BSplCLib.BSplCLib_CacheParams_SpanIndex_get, _BSplCLib.BSplCLib_CacheParams_SpanIndex_set)

    def __init__(self, *args):
        r"""
        * ///< index of the span Constructor, prepares data structures for caching. \param theDegree degree of the B-spline (or Bezier) \param thePeriodic identify whether the B-spline is periodic \param theFlatKnots knots of Bezier / B-spline parameterization
        	:param theDegree:
        	:type theDegree: int
        	:param thePeriodic:
        	:type thePeriodic: bool
        	:param theFlatKnots:
        	:type theFlatKnots: TColStd_Array1OfReal
        	:rtype: None
        """
        _BSplCLib.BSplCLib_CacheParams_swiginit(self, _BSplCLib.new_BSplCLib_CacheParams(*args))
    IsCacheValid = _swig_new_instance_method(_BSplCLib.BSplCLib_CacheParams_IsCacheValid)
    LocateParameter = _swig_new_instance_method(_BSplCLib.BSplCLib_CacheParams_LocateParameter)
    PeriodicNormalization = _swig_new_instance_method(_BSplCLib.BSplCLib_CacheParams_PeriodicNormalization)

    __repr__ = _dumps_object

    __swig_destroy__ = _BSplCLib.delete_BSplCLib_CacheParams

# Register BSplCLib_CacheParams in _BSplCLib:
_BSplCLib.BSplCLib_CacheParams_swigregister(BSplCLib_CacheParams)



