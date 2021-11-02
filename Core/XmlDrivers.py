# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
XmlDrivers module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_xmldrivers.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _XmlDrivers
else:
    import _XmlDrivers

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _XmlDrivers.SWIG_PyInstanceMethod_New
_swig_new_static_method = _XmlDrivers.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _XmlDrivers.delete_SwigPyIterator
    value = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_value)
    incr = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_copy)
    next = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_XmlDrivers.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_XmlDrivers.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _XmlDrivers:
_XmlDrivers.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Message
import OCC.Core.XmlMDF
import OCC.Core.TDF
import OCC.Core.TCollection
import OCC.Core.TColStd
import OCC.Core.XmlObjMgt
import OCC.Core.LDOM
import OCC.Core.gp
import OCC.Core.Storage
import OCC.Core.TDocStd
import OCC.Core.CDF
import OCC.Core.CDM
import OCC.Core.Resource
import OCC.Core.PCDM
import OCC.Core.XmlLDrivers
Handle_XmlDrivers_DocumentRetrievalDriver_Create = _XmlDrivers.Handle_XmlDrivers_DocumentRetrievalDriver_Create
Handle_XmlDrivers_DocumentRetrievalDriver_DownCast = _XmlDrivers.Handle_XmlDrivers_DocumentRetrievalDriver_DownCast
Handle_XmlDrivers_DocumentRetrievalDriver_IsNull = _XmlDrivers.Handle_XmlDrivers_DocumentRetrievalDriver_IsNull
Handle_XmlDrivers_DocumentStorageDriver_Create = _XmlDrivers.Handle_XmlDrivers_DocumentStorageDriver_Create
Handle_XmlDrivers_DocumentStorageDriver_DownCast = _XmlDrivers.Handle_XmlDrivers_DocumentStorageDriver_DownCast
Handle_XmlDrivers_DocumentStorageDriver_IsNull = _XmlDrivers.Handle_XmlDrivers_DocumentStorageDriver_IsNull
class xmldrivers(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AttributeDrivers = _swig_new_static_method(_XmlDrivers.xmldrivers_AttributeDrivers)
    DefineFormat = _swig_new_static_method(_XmlDrivers.xmldrivers_DefineFormat)
    Factory = _swig_new_static_method(_XmlDrivers.xmldrivers_Factory)

    __repr__ = _dumps_object


    def __init__(self):
        _XmlDrivers.xmldrivers_swiginit(self, _XmlDrivers.new_xmldrivers())
    __swig_destroy__ = _XmlDrivers.delete_xmldrivers

# Register xmldrivers in _XmlDrivers:
_XmlDrivers.xmldrivers_swigregister(xmldrivers)
xmldrivers_AttributeDrivers = _XmlDrivers.xmldrivers_AttributeDrivers
xmldrivers_DefineFormat = _XmlDrivers.xmldrivers_DefineFormat
xmldrivers_Factory = _XmlDrivers.xmldrivers_Factory

class XmlDrivers_DocumentRetrievalDriver(OCC.Core.XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ReadShapeSection = _swig_new_instance_method(_XmlDrivers.XmlDrivers_DocumentRetrievalDriver_ReadShapeSection)
    ShapeSetCleaning = _swig_new_instance_method(_XmlDrivers.XmlDrivers_DocumentRetrievalDriver_ShapeSetCleaning)

    def __init__(self, *args):
        r""":rtype: None"""
        _XmlDrivers.XmlDrivers_DocumentRetrievalDriver_swiginit(self, _XmlDrivers.new_XmlDrivers_DocumentRetrievalDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlDrivers_DocumentRetrievalDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlDrivers.delete_XmlDrivers_DocumentRetrievalDriver

# Register XmlDrivers_DocumentRetrievalDriver in _XmlDrivers:
_XmlDrivers.XmlDrivers_DocumentRetrievalDriver_swigregister(XmlDrivers_DocumentRetrievalDriver)

class XmlDrivers_DocumentStorageDriver(OCC.Core.XmlLDrivers.XmlLDrivers_DocumentStorageDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    WriteShapeSection = _swig_new_instance_method(_XmlDrivers.XmlDrivers_DocumentStorageDriver_WriteShapeSection)

    def __init__(self, *args):
        r"""
        :param theCopyright:
        	:type theCopyright: TCollection_ExtendedString
        	:rtype: None
        """
        _XmlDrivers.XmlDrivers_DocumentStorageDriver_swiginit(self, _XmlDrivers.new_XmlDrivers_DocumentStorageDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlDrivers_DocumentStorageDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlDrivers.delete_XmlDrivers_DocumentStorageDriver

# Register XmlDrivers_DocumentStorageDriver in _XmlDrivers:
_XmlDrivers.XmlDrivers_DocumentStorageDriver_swigregister(XmlDrivers_DocumentStorageDriver)



