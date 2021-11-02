# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BRepAdaptor module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_brepadaptor.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BRepAdaptor
else:
    import _BRepAdaptor

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BRepAdaptor.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BRepAdaptor.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BRepAdaptor.delete_SwigPyIterator
    value = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BRepAdaptor.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BRepAdaptor:
_BRepAdaptor.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TopoDS
import OCC.Core.TopLoc
import OCC.Core.GeomAdaptor
import OCC.Core.Geom2dAdaptor
Handle_BRepAdaptor_HCompCurve_Create = _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_Create
Handle_BRepAdaptor_HCompCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_DownCast
Handle_BRepAdaptor_HCompCurve_IsNull = _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_IsNull
Handle_BRepAdaptor_HCurve_Create = _BRepAdaptor.Handle_BRepAdaptor_HCurve_Create
Handle_BRepAdaptor_HCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCurve_DownCast
Handle_BRepAdaptor_HCurve_IsNull = _BRepAdaptor.Handle_BRepAdaptor_HCurve_IsNull
Handle_BRepAdaptor_HCurve2d_Create = _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_Create
Handle_BRepAdaptor_HCurve2d_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_DownCast
Handle_BRepAdaptor_HCurve2d_IsNull = _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_IsNull
Handle_BRepAdaptor_HSurface_Create = _BRepAdaptor.Handle_BRepAdaptor_HSurface_Create
Handle_BRepAdaptor_HSurface_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HSurface_DownCast
Handle_BRepAdaptor_HSurface_IsNull = _BRepAdaptor.Handle_BRepAdaptor_HSurface_IsNull
Handle_BRepAdaptor_HArray1OfCurve_Create = _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_Create
Handle_BRepAdaptor_HArray1OfCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_DownCast
Handle_BRepAdaptor_HArray1OfCurve_IsNull = _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_IsNull
class BRepAdaptor_Array1OfCurve(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_begin)
    end = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_end)
    cbegin = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_cbegin)
    cend = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_cend)

    def __init__(self, *args):
        _BRepAdaptor.BRepAdaptor_Array1OfCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Array1OfCurve(*args))
    Init = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Init)
    Size = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Size)
    Length = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Length)
    IsEmpty = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_IsEmpty)
    Lower = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Lower)
    Upper = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Upper)
    IsDeletable = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_IsDeletable)
    IsAllocated = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_IsAllocated)
    Assign = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Assign)
    Move = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Move)
    Set = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Set)
    First = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_First)
    ChangeFirst = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_ChangeFirst)
    Last = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Last)
    ChangeLast = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_ChangeLast)
    Value = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Value)
    ChangeValue = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_ChangeValue)
    __call__ = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve___call__)
    SetValue = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_SetValue)
    Resize = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Resize)
    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Array1OfCurve

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


# Register BRepAdaptor_Array1OfCurve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_Array1OfCurve_swigregister(BRepAdaptor_Array1OfCurve)

class BRepAdaptor_CompCurve(OCC.Core.Adaptor3d.Adaptor3d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an undefined Curve with no Wire loaded.
        	:rtype: None:param W:
        	:type W: TopoDS_Wire
        	:param KnotByCurvilinearAbcissa: default value is Standard_False
        	:type KnotByCurvilinearAbcissa: bool
        	:rtype: None* Creates a Curve to acces to the geometry of edge <W>.
        	:param W:
        	:type W: TopoDS_Wire
        	:param KnotByCurvilinearAbcissa:
        	:type KnotByCurvilinearAbcissa: bool
        	:param First:
        	:type First: float
        	:param Last:
        	:type Last: float
        	:param Tol:
        	:type Tol: float
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_CompCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_CompCurve(*args))
    Edge = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_CompCurve_Edge)
    Initialize = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_CompCurve_Initialize)
    Wire = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_CompCurve_Wire)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_CompCurve

# Register BRepAdaptor_CompCurve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_CompCurve_swigregister(BRepAdaptor_CompCurve)

class BRepAdaptor_Curve(OCC.Core.Adaptor3d.Adaptor3d_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an undefined Curve with no Edge loaded.
        	:rtype: None* Creates a Curve to acces to the geometry of edge <E>.
        	:param E:
        	:type E: TopoDS_Edge
        	:rtype: None* Creates a Curve to acces to the geometry of edge <E>. The geometry will be computed using the parametric curve of <E> on the face <F>. An Error is raised if the edge does not have a pcurve on the face.
        	:param E:
        	:type E: TopoDS_Edge
        	:param F:
        	:type F: TopoDS_Face
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_Curve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Curve(*args))
    Curve = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Curve)
    CurveOnSurface = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_CurveOnSurface)
    Edge = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Edge)
    Initialize = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Initialize)
    Is3DCurve = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Is3DCurve)
    IsCurveOnSurface = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_IsCurveOnSurface)
    Reset = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Reset)
    Tolerance = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Tolerance)
    Trsf = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve_Trsf)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Curve

# Register BRepAdaptor_Curve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_Curve_swigregister(BRepAdaptor_Curve)

class BRepAdaptor_Curve2d(OCC.Core.Geom2dAdaptor.Geom2dAdaptor_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an uninitialized curve2d.
        	:rtype: None* Creates with the pcurve of <E> on <F>.
        	:param E:
        	:type E: TopoDS_Edge
        	:param F:
        	:type F: TopoDS_Face
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_Curve2d_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Curve2d(*args))
    Edge = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve2d_Edge)
    Face = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve2d_Face)
    Initialize = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Curve2d_Initialize)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Curve2d

# Register BRepAdaptor_Curve2d in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_Curve2d_swigregister(BRepAdaptor_Curve2d)

class BRepAdaptor_HCompCurve(OCC.Core.Adaptor3d.Adaptor3d_HCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve.
        	:rtype: None* Creates a GenHCurve from a Curve
        	:param C:
        	:type C: BRepAdaptor_CompCurve
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_HCompCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCompCurve(*args))
    ChangeCurve = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCompCurve_ChangeCurve)
    Set = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCompCurve_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BRepAdaptor_HCompCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCompCurve

# Register BRepAdaptor_HCompCurve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_HCompCurve_swigregister(BRepAdaptor_HCompCurve)

class BRepAdaptor_HCurve(OCC.Core.Adaptor3d.Adaptor3d_HCurve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve.
        	:rtype: None* Creates a GenHCurve from a Curve
        	:param C:
        	:type C: BRepAdaptor_Curve
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_HCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCurve(*args))
    ChangeCurve = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCurve_ChangeCurve)
    Set = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCurve_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BRepAdaptor_HCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCurve

# Register BRepAdaptor_HCurve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_HCurve_swigregister(BRepAdaptor_HCurve)

class BRepAdaptor_HCurve2d(OCC.Core.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHCurve2d.
        	:rtype: None* Creates a GenHCurve2d from a Curve
        	:param C:
        	:type C: BRepAdaptor_Curve2d
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_HCurve2d_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCurve2d(*args))
    ChangeCurve2d = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCurve2d_ChangeCurve2d)
    Set = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HCurve2d_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BRepAdaptor_HCurve2d_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCurve2d

# Register BRepAdaptor_HCurve2d in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_HCurve2d_swigregister(BRepAdaptor_HCurve2d)

class BRepAdaptor_HSurface(OCC.Core.Adaptor3d.Adaptor3d_HSurface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an empty GenHSurface.
        	:rtype: None* Creates a GenHSurface from a Surface.
        	:param S:
        	:type S: BRepAdaptor_Surface
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_HSurface_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HSurface(*args))
    ChangeSurface = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HSurface_ChangeSurface)
    Set = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HSurface_Set)


    @staticmethod
    def DownCast(t):
      return Handle_BRepAdaptor_HSurface_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HSurface

# Register BRepAdaptor_HSurface in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_HSurface_swigregister(BRepAdaptor_HSurface)

class BRepAdaptor_Surface(OCC.Core.Adaptor3d.Adaptor3d_Surface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        * Creates an undefined surface with no face loaded.
        	:rtype: None* Creates a surface to access the geometry of <F>. If <Restriction> is true the parameter range is the parameter range in the UV space of the restriction.
        	:param F:
        	:type F: TopoDS_Face
        	:param R: default value is Standard_True
        	:type R: bool
        	:rtype: None
        """
        _BRepAdaptor.BRepAdaptor_Surface_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Surface(*args))
    ChangeSurface = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_ChangeSurface)
    Face = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_Face)
    Initialize = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_Initialize)
    Surface = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_Surface)
    Tolerance = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_Tolerance)
    Trsf = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_Surface_Trsf)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Surface

# Register BRepAdaptor_Surface in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_Surface_swigregister(BRepAdaptor_Surface)

class BRepAdaptor_HArray1OfCurve(BRepAdaptor_Array1OfCurve, OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.BRepAdaptor_HArray1OfCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HArray1OfCurve(*args))
    Array1 = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Array1)
    ChangeArray1 = _swig_new_instance_method(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_ChangeArray1)


    @staticmethod
    def DownCast(t):
      return Handle_BRepAdaptor_HArray1OfCurve_DownCast(t)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HArray1OfCurve

# Register BRepAdaptor_HArray1OfCurve in _BRepAdaptor:
_BRepAdaptor.BRepAdaptor_HArray1OfCurve_swigregister(BRepAdaptor_HArray1OfCurve)


