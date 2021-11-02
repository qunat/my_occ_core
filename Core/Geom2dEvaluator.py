# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
Geom2dEvaluator module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_geom2devaluator.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Geom2dEvaluator
else:
    import _Geom2dEvaluator

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _Geom2dEvaluator.SWIG_PyInstanceMethod_New
_swig_new_static_method = _Geom2dEvaluator.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _Geom2dEvaluator.delete_SwigPyIterator
    value = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_value)
    incr = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_copy)
    next = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_Geom2dEvaluator.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Geom2dEvaluator:
_Geom2dEvaluator.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom2d
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Geom2dAdaptor
import OCC.Core.Adaptor2d
Handle_Geom2dEvaluator_Curve_Create = _Geom2dEvaluator.Handle_Geom2dEvaluator_Curve_Create
Handle_Geom2dEvaluator_Curve_DownCast = _Geom2dEvaluator.Handle_Geom2dEvaluator_Curve_DownCast
Handle_Geom2dEvaluator_Curve_IsNull = _Geom2dEvaluator.Handle_Geom2dEvaluator_Curve_IsNull
Handle_Geom2dEvaluator_OffsetCurve_Create = _Geom2dEvaluator.Handle_Geom2dEvaluator_OffsetCurve_Create
Handle_Geom2dEvaluator_OffsetCurve_DownCast = _Geom2dEvaluator.Handle_Geom2dEvaluator_OffsetCurve_DownCast
Handle_Geom2dEvaluator_OffsetCurve_IsNull = _Geom2dEvaluator.Handle_Geom2dEvaluator_OffsetCurve_IsNull
class Geom2dEvaluator_Curve(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    D0 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_Curve_D0)
    D1 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_Curve_D1)
    D2 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_Curve_D2)
    D3 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_Curve_D3)
    DN = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_Curve_DN)


    @staticmethod
    def DownCast(t):
      return Handle_Geom2dEvaluator_Curve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dEvaluator.delete_Geom2dEvaluator_Curve

# Register Geom2dEvaluator_Curve in _Geom2dEvaluator:
_Geom2dEvaluator.Geom2dEvaluator_Curve_swigregister(Geom2dEvaluator_Curve)

class Geom2dEvaluator_OffsetCurve(Geom2dEvaluator_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    D0 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_D0)
    D1 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_D1)
    D2 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_D2)
    D3 = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_D3)
    DN = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_DN)

    def __init__(self, *args):
        r"""
        * Initialize evaluator by curve
        	:param theBase:
        	:type theBase: Geom2d_Curve
        	:param theOffset:
        	:type theOffset: float
        	:rtype: None* Initialize evaluator by curve adaptor
        	:param theBase:
        	:type theBase: Geom2dAdaptor_HCurve
        	:param theOffset:
        	:type theOffset: float
        	:rtype: None
        """
        _Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_swiginit(self, _Geom2dEvaluator.new_Geom2dEvaluator_OffsetCurve(*args))
    SetOffsetValue = _swig_new_instance_method(_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_SetOffsetValue)


    @staticmethod
    def DownCast(t):
      return Handle_Geom2dEvaluator_OffsetCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dEvaluator.delete_Geom2dEvaluator_OffsetCurve

# Register Geom2dEvaluator_OffsetCurve in _Geom2dEvaluator:
_Geom2dEvaluator.Geom2dEvaluator_OffsetCurve_swigregister(Geom2dEvaluator_OffsetCurve)



