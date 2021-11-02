# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
BinTools module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_bintools.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BinTools
else:
    import _BinTools

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _BinTools.SWIG_PyInstanceMethod_New
_swig_new_static_method = _BinTools.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _BinTools.delete_SwigPyIterator
    value = _swig_new_instance_method(_BinTools.SwigPyIterator_value)
    incr = _swig_new_instance_method(_BinTools.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_BinTools.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_BinTools.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_BinTools.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_BinTools.SwigPyIterator_copy)
    next = _swig_new_instance_method(_BinTools.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_BinTools.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_BinTools.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_BinTools.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_BinTools.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_BinTools.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_BinTools.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_BinTools.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_BinTools.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_BinTools.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BinTools:
_BinTools.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Geom2d
import OCC.Core.GeomAbs
import OCC.Core.TColgp
import OCC.Core.TColStd
import OCC.Core.TCollection
import OCC.Core.Geom
class bintools(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetBool = _swig_new_static_method(_BinTools.bintools_GetBool)
    GetExtChar = _swig_new_static_method(_BinTools.bintools_GetExtChar)
    GetInteger = _swig_new_static_method(_BinTools.bintools_GetInteger)
    GetReal = _swig_new_static_method(_BinTools.bintools_GetReal)
    PutBool = _swig_new_static_method(_BinTools.bintools_PutBool)
    PutExtChar = _swig_new_static_method(_BinTools.bintools_PutExtChar)
    PutInteger = _swig_new_static_method(_BinTools.bintools_PutInteger)
    PutReal = _swig_new_static_method(_BinTools.bintools_PutReal)
    Read = _swig_new_static_method(_BinTools.bintools_Read)
    Write = _swig_new_static_method(_BinTools.bintools_Write)

    __repr__ = _dumps_object


    def __init__(self):
        _BinTools.bintools_swiginit(self, _BinTools.new_bintools())
    __swig_destroy__ = _BinTools.delete_bintools

# Register bintools in _BinTools:
_BinTools.bintools_swigregister(bintools)
bintools_GetBool = _BinTools.bintools_GetBool
bintools_GetExtChar = _BinTools.bintools_GetExtChar
bintools_GetInteger = _BinTools.bintools_GetInteger
bintools_GetReal = _BinTools.bintools_GetReal
bintools_PutBool = _BinTools.bintools_PutBool
bintools_PutExtChar = _BinTools.bintools_PutExtChar
bintools_PutInteger = _BinTools.bintools_PutInteger
bintools_PutReal = _BinTools.bintools_PutReal
bintools_Read = _BinTools.bintools_Read
bintools_Write = _BinTools.bintools_Write

class BinTools_Curve2dSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_Add)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Curves.
        	:rtype: None
        """
        _BinTools.BinTools_Curve2dSet_swiginit(self, _BinTools.new_BinTools_Curve2dSet(*args))
    Clear = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_Clear)
    Curve2d = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_Curve2d)
    Index = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_Index)
    ReadFromString = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_ReadFromString)
    ReadCurve2d = _swig_new_static_method(_BinTools.BinTools_Curve2dSet_ReadCurve2d)
    WriteToString = _swig_new_instance_method(_BinTools.BinTools_Curve2dSet_WriteToString)
    WriteCurve2d = _swig_new_static_method(_BinTools.BinTools_Curve2dSet_WriteCurve2d)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinTools.delete_BinTools_Curve2dSet

# Register BinTools_Curve2dSet in _BinTools:
_BinTools.BinTools_Curve2dSet_swigregister(BinTools_Curve2dSet)
BinTools_Curve2dSet_ReadCurve2d = _BinTools.BinTools_Curve2dSet_ReadCurve2d
BinTools_Curve2dSet_WriteCurve2d = _BinTools.BinTools_Curve2dSet_WriteCurve2d

class BinTools_CurveSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_BinTools.BinTools_CurveSet_Add)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Curves.
        	:rtype: None
        """
        _BinTools.BinTools_CurveSet_swiginit(self, _BinTools.new_BinTools_CurveSet(*args))
    Clear = _swig_new_instance_method(_BinTools.BinTools_CurveSet_Clear)
    Curve = _swig_new_instance_method(_BinTools.BinTools_CurveSet_Curve)
    Index = _swig_new_instance_method(_BinTools.BinTools_CurveSet_Index)
    ReadFromString = _swig_new_instance_method(_BinTools.BinTools_CurveSet_ReadFromString)
    ReadCurve = _swig_new_static_method(_BinTools.BinTools_CurveSet_ReadCurve)
    WriteToString = _swig_new_instance_method(_BinTools.BinTools_CurveSet_WriteToString)
    WriteCurve = _swig_new_static_method(_BinTools.BinTools_CurveSet_WriteCurve)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinTools.delete_BinTools_CurveSet

# Register BinTools_CurveSet in _BinTools:
_BinTools.BinTools_CurveSet_swigregister(BinTools_CurveSet)
BinTools_CurveSet_ReadCurve = _BinTools.BinTools_CurveSet_ReadCurve
BinTools_CurveSet_WriteCurve = _BinTools.BinTools_CurveSet_WriteCurve

class BinTools_LocationSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_BinTools.BinTools_LocationSet_Add)

    def __init__(self, *args):
        r"""
        * Returns an empty set of locations.
        	:rtype: None
        """
        _BinTools.BinTools_LocationSet_swiginit(self, _BinTools.new_BinTools_LocationSet(*args))
    Clear = _swig_new_instance_method(_BinTools.BinTools_LocationSet_Clear)
    Index = _swig_new_instance_method(_BinTools.BinTools_LocationSet_Index)
    Location = _swig_new_instance_method(_BinTools.BinTools_LocationSet_Location)
    NbLocations = _swig_new_instance_method(_BinTools.BinTools_LocationSet_NbLocations)
    ReadFromString = _swig_new_instance_method(_BinTools.BinTools_LocationSet_ReadFromString)
    WriteToString = _swig_new_instance_method(_BinTools.BinTools_LocationSet_WriteToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinTools.delete_BinTools_LocationSet

# Register BinTools_LocationSet in _BinTools:
_BinTools.BinTools_LocationSet_swigregister(BinTools_LocationSet)

class BinTools_ShapeSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Add)
    AddGeometry = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_AddGeometry)
    AddShapes = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_AddShapes)

    def __init__(self, *args):
        r"""
        * Builds an empty ShapeSet. Parameter <isWithTriangles> is added for XML Persistence
        	:param isWithTriangles: default value is Standard_False
        	:type isWithTriangles: bool
        	:rtype: None
        """
        _BinTools.BinTools_ShapeSet_swiginit(self, _BinTools.new_BinTools_ShapeSet(*args))
    ChangeLocations = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ChangeLocations)
    Clear = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Clear)
    FormatNb = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_FormatNb)
    Index = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Index)
    IsWithTriangles = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_IsWithTriangles)
    Locations = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Locations)
    NbShapes = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_NbShapes)
    ReadFromString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadFromString)
    Read = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Read)
    ReadGeometryFromString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadGeometryFromString)
    ReadGeometry = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadGeometry)
    ReadPolygon3DFromString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadPolygon3DFromString)
    ReadPolygonOnTriangulationFromString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadPolygonOnTriangulationFromString)
    ReadTriangulationFromString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_ReadTriangulationFromString)
    SetFormatNb = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_SetFormatNb)
    SetWithTriangles = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_SetWithTriangles)
    Shape = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Shape)
    WriteToString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WriteToString)
    Write = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_Write)
    WriteGeometryToString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WriteGeometryToString)
    WriteGeometry = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WriteGeometry)
    WritePolygon3DToString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WritePolygon3DToString)
    WritePolygonOnTriangulationToString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WritePolygonOnTriangulationToString)
    WriteTriangulationToString = _swig_new_instance_method(_BinTools.BinTools_ShapeSet_WriteTriangulationToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinTools.delete_BinTools_ShapeSet

# Register BinTools_ShapeSet in _BinTools:
_BinTools.BinTools_ShapeSet_swigregister(BinTools_ShapeSet)

class BinTools_SurfaceSet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Add = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_Add)

    def __init__(self, *args):
        r"""
        * Returns an empty set of Surfaces.
        	:rtype: None
        """
        _BinTools.BinTools_SurfaceSet_swiginit(self, _BinTools.new_BinTools_SurfaceSet(*args))
    Clear = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_Clear)
    Index = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_Index)
    ReadFromString = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_ReadFromString)
    ReadSurface = _swig_new_static_method(_BinTools.BinTools_SurfaceSet_ReadSurface)
    Surface = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_Surface)
    WriteToString = _swig_new_instance_method(_BinTools.BinTools_SurfaceSet_WriteToString)
    WriteSurface = _swig_new_static_method(_BinTools.BinTools_SurfaceSet_WriteSurface)

    __repr__ = _dumps_object

    __swig_destroy__ = _BinTools.delete_BinTools_SurfaceSet

# Register BinTools_SurfaceSet in _BinTools:
_BinTools.BinTools_SurfaceSet_swigregister(BinTools_SurfaceSet)
BinTools_SurfaceSet_ReadSurface = _BinTools.BinTools_SurfaceSet_ReadSurface
BinTools_SurfaceSet_WriteSurface = _BinTools.BinTools_SurfaceSet_WriteSurface



