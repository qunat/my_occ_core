# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
XmlLDrivers module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_xmlldrivers.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _XmlLDrivers
else:
    import _XmlLDrivers

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _XmlLDrivers.SWIG_PyInstanceMethod_New
_swig_new_static_method = _XmlLDrivers.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _XmlLDrivers.delete_SwigPyIterator
    value = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_value)
    incr = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_copy)
    next = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_XmlLDrivers.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _XmlLDrivers:
_XmlLDrivers.SwigPyIterator_swigregister(SwigPyIterator)


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
Handle_XmlLDrivers_DocumentRetrievalDriver_Create = _XmlLDrivers.Handle_XmlLDrivers_DocumentRetrievalDriver_Create
Handle_XmlLDrivers_DocumentRetrievalDriver_DownCast = _XmlLDrivers.Handle_XmlLDrivers_DocumentRetrievalDriver_DownCast
Handle_XmlLDrivers_DocumentRetrievalDriver_IsNull = _XmlLDrivers.Handle_XmlLDrivers_DocumentRetrievalDriver_IsNull
Handle_XmlLDrivers_DocumentStorageDriver_Create = _XmlLDrivers.Handle_XmlLDrivers_DocumentStorageDriver_Create
Handle_XmlLDrivers_DocumentStorageDriver_DownCast = _XmlLDrivers.Handle_XmlLDrivers_DocumentStorageDriver_DownCast
Handle_XmlLDrivers_DocumentStorageDriver_IsNull = _XmlLDrivers.Handle_XmlLDrivers_DocumentStorageDriver_IsNull
class XmlLDrivers_SequenceOfNamespaceDef(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_begin)
    end = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_end)
    cbegin = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_cbegin)
    cend = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_cend)

    def __init__(self, *args):
        _XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_swiginit(self, _XmlLDrivers.new_XmlLDrivers_SequenceOfNamespaceDef(*args))
    Size = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Size)
    Length = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Length)
    Lower = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Lower)
    Upper = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Upper)
    IsEmpty = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_IsEmpty)
    Reverse = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Reverse)
    Exchange = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Exchange)
    delNode = _swig_new_static_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_delNode)
    Clear = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Clear)
    Assign = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Assign)
    Set = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Set)
    Remove = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Remove)
    Append = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Append)
    Prepend = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Prepend)
    InsertBefore = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_InsertBefore)
    InsertAfter = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_InsertAfter)
    Split = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Split)
    First = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_First)
    ChangeFirst = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_ChangeFirst)
    Last = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Last)
    ChangeLast = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_ChangeLast)
    Value = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_Value)
    ChangeValue = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_ChangeValue)
    __call__ = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef___call__)
    SetValue = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_SetValue)
    __swig_destroy__ = _XmlLDrivers.delete_XmlLDrivers_SequenceOfNamespaceDef

# Register XmlLDrivers_SequenceOfNamespaceDef in _XmlLDrivers:
_XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_swigregister(XmlLDrivers_SequenceOfNamespaceDef)
XmlLDrivers_SequenceOfNamespaceDef_delNode = _XmlLDrivers.XmlLDrivers_SequenceOfNamespaceDef_delNode

class xmlldrivers(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AttributeDrivers = _swig_new_static_method(_XmlLDrivers.xmlldrivers_AttributeDrivers)
    CreationDate = _swig_new_static_method(_XmlLDrivers.xmlldrivers_CreationDate)
    DefineFormat = _swig_new_static_method(_XmlLDrivers.xmlldrivers_DefineFormat)
    Factory = _swig_new_static_method(_XmlLDrivers.xmlldrivers_Factory)
    StorageVersion = _swig_new_static_method(_XmlLDrivers.xmlldrivers_StorageVersion)

    __repr__ = _dumps_object


    def __init__(self):
        _XmlLDrivers.xmlldrivers_swiginit(self, _XmlLDrivers.new_xmlldrivers())
    __swig_destroy__ = _XmlLDrivers.delete_xmlldrivers

# Register xmlldrivers in _XmlLDrivers:
_XmlLDrivers.xmlldrivers_swigregister(xmlldrivers)
xmlldrivers_AttributeDrivers = _XmlLDrivers.xmlldrivers_AttributeDrivers
xmlldrivers_CreationDate = _XmlLDrivers.xmlldrivers_CreationDate
xmlldrivers_DefineFormat = _XmlLDrivers.xmlldrivers_DefineFormat
xmlldrivers_Factory = _XmlLDrivers.xmlldrivers_Factory
xmlldrivers_StorageVersion = _XmlLDrivers.xmlldrivers_StorageVersion

class XmlLDrivers_DocumentRetrievalDriver(OCC.Core.PCDM.PCDM_RetrievalDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AttributeDrivers = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver_AttributeDrivers)
    Read = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver_Read)

    def __init__(self, *args):
        r""":rtype: None"""
        _XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver_swiginit(self, _XmlLDrivers.new_XmlLDrivers_DocumentRetrievalDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlLDrivers_DocumentRetrievalDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlLDrivers.delete_XmlLDrivers_DocumentRetrievalDriver

# Register XmlLDrivers_DocumentRetrievalDriver in _XmlLDrivers:
_XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver_swigregister(XmlLDrivers_DocumentRetrievalDriver)

class XmlLDrivers_DocumentStorageDriver(OCC.Core.PCDM.PCDM_StorageDriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AttributeDrivers = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_DocumentStorageDriver_AttributeDrivers)
    Write = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_DocumentStorageDriver_Write)

    def __init__(self, *args):
        r"""
        :param theCopyright:
        	:type theCopyright: TCollection_ExtendedString
        	:rtype: None
        """
        _XmlLDrivers.XmlLDrivers_DocumentStorageDriver_swiginit(self, _XmlLDrivers.new_XmlLDrivers_DocumentStorageDriver(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XmlLDrivers_DocumentStorageDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XmlLDrivers.delete_XmlLDrivers_DocumentStorageDriver

# Register XmlLDrivers_DocumentStorageDriver in _XmlLDrivers:
_XmlLDrivers.XmlLDrivers_DocumentStorageDriver_swigregister(XmlLDrivers_DocumentStorageDriver)

class XmlLDrivers_NamespaceDef(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Prefix = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_NamespaceDef_Prefix)
    URI = _swig_new_instance_method(_XmlLDrivers.XmlLDrivers_NamespaceDef_URI)

    def __init__(self, *args):
        r"""
        :rtype: None:param thePrefix:
        	:type thePrefix: TCollection_AsciiString
        	:param theURI:
        	:type theURI: TCollection_AsciiString
        	:rtype: None
        """
        _XmlLDrivers.XmlLDrivers_NamespaceDef_swiginit(self, _XmlLDrivers.new_XmlLDrivers_NamespaceDef(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _XmlLDrivers.delete_XmlLDrivers_NamespaceDef

# Register XmlLDrivers_NamespaceDef in _XmlLDrivers:
_XmlLDrivers.XmlLDrivers_NamespaceDef_swigregister(XmlLDrivers_NamespaceDef)


