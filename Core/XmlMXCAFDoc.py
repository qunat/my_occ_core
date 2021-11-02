# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
XmlMXCAFDoc module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_xmlmxcafdoc.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _XmlMXCAFDoc
else:
    import _XmlMXCAFDoc

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _XmlMXCAFDoc.SWIG_PyInstanceMethod_New
_swig_new_static_method = _XmlMXCAFDoc.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _XmlMXCAFDoc.delete_SwigPyIterator
    value = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_value)
    incr = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_copy)
    next = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_XmlMXCAFDoc.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _XmlMXCAFDoc:
_XmlMXCAFDoc.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.XmlMDF
import OCC.Core.Message
import OCC.Core.TDF
import OCC.Core.TCollection
import OCC.Core.TColStd
import OCC.Core.XmlObjMgt
import OCC.Core.LDOM
import OCC.Core.gp
import OCC.Core.Storage
import OCC.Core.TopTools
import OCC.Core.TopoDS
import OCC.Core.TopAbs
import OCC.Core.TopLoc
Handle_XmlMXCAFDoc_AreaDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AreaDriver_Create
Handle_XmlMXCAFDoc_AreaDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AreaDriver_DownCast
Handle_XmlMXCAFDoc_AreaDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AreaDriver_IsNull
Handle_XmlMXCAFDoc_AssemblyItemRefDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AssemblyItemRefDriver_Create
Handle_XmlMXCAFDoc_AssemblyItemRefDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AssemblyItemRefDriver_DownCast
Handle_XmlMXCAFDoc_AssemblyItemRefDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_AssemblyItemRefDriver_IsNull
Handle_XmlMXCAFDoc_CentroidDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_CentroidDriver_Create
Handle_XmlMXCAFDoc_CentroidDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_CentroidDriver_DownCast
Handle_XmlMXCAFDoc_CentroidDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_CentroidDriver_IsNull
Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_Create
Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_DownCast
Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_IsNull
Handle_XmlMXCAFDoc_ColorDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorDriver_Create
Handle_XmlMXCAFDoc_ColorDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorDriver_DownCast
Handle_XmlMXCAFDoc_ColorDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorDriver_IsNull
Handle_XmlMXCAFDoc_ColorToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorToolDriver_Create
Handle_XmlMXCAFDoc_ColorToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorToolDriver_DownCast
Handle_XmlMXCAFDoc_ColorToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ColorToolDriver_IsNull
Handle_XmlMXCAFDoc_DatumDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DatumDriver_Create
Handle_XmlMXCAFDoc_DatumDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DatumDriver_DownCast
Handle_XmlMXCAFDoc_DatumDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DatumDriver_IsNull
Handle_XmlMXCAFDoc_DimTolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolDriver_Create
Handle_XmlMXCAFDoc_DimTolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolDriver_DownCast
Handle_XmlMXCAFDoc_DimTolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolDriver_IsNull
Handle_XmlMXCAFDoc_DimTolToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolToolDriver_Create
Handle_XmlMXCAFDoc_DimTolToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolToolDriver_DownCast
Handle_XmlMXCAFDoc_DimTolToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DimTolToolDriver_IsNull
Handle_XmlMXCAFDoc_DocumentToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DocumentToolDriver_Create
Handle_XmlMXCAFDoc_DocumentToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DocumentToolDriver_DownCast
Handle_XmlMXCAFDoc_DocumentToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_DocumentToolDriver_IsNull
Handle_XmlMXCAFDoc_GraphNodeDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_GraphNodeDriver_Create
Handle_XmlMXCAFDoc_GraphNodeDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_GraphNodeDriver_DownCast
Handle_XmlMXCAFDoc_GraphNodeDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_GraphNodeDriver_IsNull
Handle_XmlMXCAFDoc_LayerToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LayerToolDriver_Create
Handle_XmlMXCAFDoc_LayerToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LayerToolDriver_DownCast
Handle_XmlMXCAFDoc_LayerToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LayerToolDriver_IsNull
Handle_XmlMXCAFDoc_LocationDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LocationDriver_Create
Handle_XmlMXCAFDoc_LocationDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LocationDriver_DownCast
Handle_XmlMXCAFDoc_LocationDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_LocationDriver_IsNull
Handle_XmlMXCAFDoc_MaterialDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialDriver_Create
Handle_XmlMXCAFDoc_MaterialDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialDriver_DownCast
Handle_XmlMXCAFDoc_MaterialDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialDriver_IsNull
Handle_XmlMXCAFDoc_MaterialToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialToolDriver_Create
Handle_XmlMXCAFDoc_MaterialToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialToolDriver_DownCast
Handle_XmlMXCAFDoc_MaterialToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_MaterialToolDriver_IsNull
Handle_XmlMXCAFDoc_NoteDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteDriver_Create
Handle_XmlMXCAFDoc_NoteDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteDriver_DownCast
Handle_XmlMXCAFDoc_NoteDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteDriver_IsNull
Handle_XmlMXCAFDoc_NotesToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NotesToolDriver_Create
Handle_XmlMXCAFDoc_NotesToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NotesToolDriver_DownCast
Handle_XmlMXCAFDoc_NotesToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NotesToolDriver_IsNull
Handle_XmlMXCAFDoc_ShapeToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ShapeToolDriver_Create
Handle_XmlMXCAFDoc_ShapeToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ShapeToolDriver_DownCast
Handle_XmlMXCAFDoc_ShapeToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ShapeToolDriver_IsNull
Handle_XmlMXCAFDoc_ViewToolDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ViewToolDriver_Create
Handle_XmlMXCAFDoc_ViewToolDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ViewToolDriver_DownCast
Handle_XmlMXCAFDoc_ViewToolDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_ViewToolDriver_IsNull
Handle_XmlMXCAFDoc_VolumeDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_VolumeDriver_Create
Handle_XmlMXCAFDoc_VolumeDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_VolumeDriver_DownCast
Handle_XmlMXCAFDoc_VolumeDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_VolumeDriver_IsNull
Handle_XmlMXCAFDoc_NoteBinDataDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBinDataDriver_Create
Handle_XmlMXCAFDoc_NoteBinDataDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBinDataDriver_DownCast
Handle_XmlMXCAFDoc_NoteBinDataDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBinDataDriver_IsNull
Handle_XmlMXCAFDoc_NoteCommentDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteCommentDriver_Create
Handle_XmlMXCAFDoc_NoteCommentDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteCommentDriver_DownCast
Handle_XmlMXCAFDoc_NoteCommentDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteCommentDriver_IsNull
Handle_XmlMXCAFDoc_NoteBalloonDriver_Create = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBalloonDriver_Create
Handle_XmlMXCAFDoc_NoteBalloonDriver_DownCast = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBalloonDriver_DownCast
Handle_XmlMXCAFDoc_NoteBalloonDriver_IsNull = _XmlMXCAFDoc.Handle_XmlMXCAFDoc_NoteBalloonDriver_IsNull
class xmlmxcafdoc(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AddDrivers = _swig_new_static_method(_XmlMXCAFDoc.xmlmxcafdoc_AddDrivers)

    __repr__ = _dumps_object


    def __init__(self):
        _XmlMXCAFDoc.xmlmxcafdoc_swiginit(self, _XmlMXCAFDoc.new_xmlmxcafdoc())
    __swig_destroy__ = _XmlMXCAFDoc.delete_xmlmxcafdoc

# Register xmlmxcafdoc in _XmlMXCAFDoc:
_XmlMXCAFDoc.xmlmxcafdoc_swigregister(xmlmxcafdoc)
xmlmxcafdoc_AddDrivers = _XmlMXCAFDoc.xmlmxcafdoc_AddDrivers

class XmlMXCAFDoc_AreaDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_AreaDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_AreaDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_AreaDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_AreaDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_AreaDriver

# Register XmlMXCAFDoc_AreaDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_AreaDriver_swigregister(XmlMXCAFDoc_AreaDriver)

class XmlMXCAFDoc_AssemblyItemRefDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_AssemblyItemRefDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_AssemblyItemRefDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_AssemblyItemRefDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_AssemblyItemRefDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_AssemblyItemRefDriver

# Register XmlMXCAFDoc_AssemblyItemRefDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_AssemblyItemRefDriver_swigregister(XmlMXCAFDoc_AssemblyItemRefDriver)

class XmlMXCAFDoc_CentroidDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_CentroidDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_CentroidDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_CentroidDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_CentroidDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_CentroidDriver

# Register XmlMXCAFDoc_CentroidDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_CentroidDriver_swigregister(XmlMXCAFDoc_CentroidDriver)

class XmlMXCAFDoc_ClippingPlaneToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_ClippingPlaneToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_ClippingPlaneToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_ClippingPlaneToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_ClippingPlaneToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_ClippingPlaneToolDriver

# Register XmlMXCAFDoc_ClippingPlaneToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_ClippingPlaneToolDriver_swigregister(XmlMXCAFDoc_ClippingPlaneToolDriver)

class XmlMXCAFDoc_ColorDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_ColorDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_ColorDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_ColorDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_ColorDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_ColorDriver

# Register XmlMXCAFDoc_ColorDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_ColorDriver_swigregister(XmlMXCAFDoc_ColorDriver)

class XmlMXCAFDoc_ColorToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_ColorToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_ColorToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_ColorToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_ColorToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_ColorToolDriver

# Register XmlMXCAFDoc_ColorToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_ColorToolDriver_swigregister(XmlMXCAFDoc_ColorToolDriver)

class XmlMXCAFDoc_DatumDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_DatumDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_DatumDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_DatumDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_DatumDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_DatumDriver

# Register XmlMXCAFDoc_DatumDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_DatumDriver_swigregister(XmlMXCAFDoc_DatumDriver)

class XmlMXCAFDoc_DimTolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_DimTolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_DimTolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_DimTolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_DimTolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_DimTolDriver

# Register XmlMXCAFDoc_DimTolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_DimTolDriver_swigregister(XmlMXCAFDoc_DimTolDriver)

class XmlMXCAFDoc_DimTolToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_DimTolToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_DimTolToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_DimTolToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_DimTolToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_DimTolToolDriver

# Register XmlMXCAFDoc_DimTolToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_DimTolToolDriver_swigregister(XmlMXCAFDoc_DimTolToolDriver)

class XmlMXCAFDoc_DocumentToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_DocumentToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_DocumentToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_DocumentToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_DocumentToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_DocumentToolDriver

# Register XmlMXCAFDoc_DocumentToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_DocumentToolDriver_swigregister(XmlMXCAFDoc_DocumentToolDriver)

class XmlMXCAFDoc_GraphNodeDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_GraphNodeDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_GraphNodeDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_GraphNodeDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_GraphNodeDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_GraphNodeDriver

# Register XmlMXCAFDoc_GraphNodeDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_GraphNodeDriver_swigregister(XmlMXCAFDoc_GraphNodeDriver)

class XmlMXCAFDoc_LayerToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_LayerToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_LayerToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_LayerToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_LayerToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_LayerToolDriver

# Register XmlMXCAFDoc_LayerToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_LayerToolDriver_swigregister(XmlMXCAFDoc_LayerToolDriver)

class XmlMXCAFDoc_LocationDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_LocationDriver_Paste)
    SetSharedLocations = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_LocationDriver_SetSharedLocations)
    Translate = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_LocationDriver_Translate)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_LocationDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_LocationDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_LocationDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_LocationDriver

# Register XmlMXCAFDoc_LocationDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_LocationDriver_swigregister(XmlMXCAFDoc_LocationDriver)

class XmlMXCAFDoc_MaterialDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_MaterialDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_MaterialDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_MaterialDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_MaterialDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_MaterialDriver

# Register XmlMXCAFDoc_MaterialDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_MaterialDriver_swigregister(XmlMXCAFDoc_MaterialDriver)

class XmlMXCAFDoc_MaterialToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_MaterialToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_MaterialToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_MaterialToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_MaterialToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_MaterialToolDriver

# Register XmlMXCAFDoc_MaterialToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_MaterialToolDriver_swigregister(XmlMXCAFDoc_MaterialToolDriver)

class XmlMXCAFDoc_NoteDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_NoteDriver_Paste)


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_NoteDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_NoteDriver

# Register XmlMXCAFDoc_NoteDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_NoteDriver_swigregister(XmlMXCAFDoc_NoteDriver)

class XmlMXCAFDoc_NotesToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_NotesToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_NotesToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_NotesToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_NotesToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_NotesToolDriver

# Register XmlMXCAFDoc_NotesToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_NotesToolDriver_swigregister(XmlMXCAFDoc_NotesToolDriver)

class XmlMXCAFDoc_ShapeToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_ShapeToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_ShapeToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_ShapeToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_ShapeToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_ShapeToolDriver

# Register XmlMXCAFDoc_ShapeToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_ShapeToolDriver_swigregister(XmlMXCAFDoc_ShapeToolDriver)

class XmlMXCAFDoc_ViewToolDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_ViewToolDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMsgDriver:
        	:type theMsgDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_ViewToolDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_ViewToolDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_ViewToolDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_ViewToolDriver

# Register XmlMXCAFDoc_ViewToolDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_ViewToolDriver_swigregister(XmlMXCAFDoc_ViewToolDriver)

class XmlMXCAFDoc_VolumeDriver(OCC.Core.XmlMDF.XmlMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_VolumeDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_VolumeDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_VolumeDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_VolumeDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_VolumeDriver

# Register XmlMXCAFDoc_VolumeDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_VolumeDriver_swigregister(XmlMXCAFDoc_VolumeDriver)

class XmlMXCAFDoc_NoteBinDataDriver(XmlMXCAFDoc_NoteDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_NoteBinDataDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_NoteBinDataDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_NoteBinDataDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_NoteBinDataDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_NoteBinDataDriver

# Register XmlMXCAFDoc_NoteBinDataDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_NoteBinDataDriver_swigregister(XmlMXCAFDoc_NoteBinDataDriver)

class XmlMXCAFDoc_NoteCommentDriver(XmlMXCAFDoc_NoteDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Paste = _swig_new_instance_method(_XmlMXCAFDoc.XmlMXCAFDoc_NoteCommentDriver_Paste)

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_NoteCommentDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_NoteCommentDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_NoteCommentDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_NoteCommentDriver

# Register XmlMXCAFDoc_NoteCommentDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_NoteCommentDriver_swigregister(XmlMXCAFDoc_NoteCommentDriver)

class XmlMXCAFDoc_NoteBalloonDriver(XmlMXCAFDoc_NoteCommentDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        :param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _XmlMXCAFDoc.XmlMXCAFDoc_NoteBalloonDriver_swiginit(self, _XmlMXCAFDoc.new_XmlMXCAFDoc_NoteBalloonDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlMXCAFDoc_NoteBalloonDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlMXCAFDoc.delete_XmlMXCAFDoc_NoteBalloonDriver

# Register XmlMXCAFDoc_NoteBalloonDriver in _XmlMXCAFDoc:
_XmlMXCAFDoc.XmlMXCAFDoc_NoteBalloonDriver_swigregister(XmlMXCAFDoc_NoteBalloonDriver)



