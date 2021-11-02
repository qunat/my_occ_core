# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
PCDM module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_pcdm.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _PCDM
else:
    import _PCDM

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _PCDM.SWIG_PyInstanceMethod_New
_swig_new_static_method = _PCDM.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _PCDM.delete_SwigPyIterator
    value = _swig_new_instance_method(_PCDM.SwigPyIterator_value)
    incr = _swig_new_instance_method(_PCDM.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_PCDM.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_PCDM.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_PCDM.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_PCDM.SwigPyIterator_copy)
    next = _swig_new_instance_method(_PCDM.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_PCDM.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_PCDM.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_PCDM.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_PCDM.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_PCDM.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_PCDM.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_PCDM.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_PCDM.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_PCDM.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _PCDM:
_PCDM.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.Storage
import OCC.Core.TCollection
import OCC.Core.Message
import OCC.Core.TColStd
import OCC.Core.CDM
import OCC.Core.Resource
PCDM_SS_OK = _PCDM.PCDM_SS_OK
PCDM_SS_DriverFailure = _PCDM.PCDM_SS_DriverFailure
PCDM_SS_WriteFailure = _PCDM.PCDM_SS_WriteFailure
PCDM_SS_Failure = _PCDM.PCDM_SS_Failure
PCDM_SS_Doc_IsNull = _PCDM.PCDM_SS_Doc_IsNull
PCDM_SS_No_Obj = _PCDM.PCDM_SS_No_Obj
PCDM_SS_Info_Section_Error = _PCDM.PCDM_SS_Info_Section_Error
PCDM_TOFD_File = _PCDM.PCDM_TOFD_File
PCDM_TOFD_CmpFile = _PCDM.PCDM_TOFD_CmpFile
PCDM_TOFD_XmlFile = _PCDM.PCDM_TOFD_XmlFile
PCDM_TOFD_Unknown = _PCDM.PCDM_TOFD_Unknown
PCDM_RS_OK = _PCDM.PCDM_RS_OK
PCDM_RS_NoDriver = _PCDM.PCDM_RS_NoDriver
PCDM_RS_UnknownFileDriver = _PCDM.PCDM_RS_UnknownFileDriver
PCDM_RS_OpenError = _PCDM.PCDM_RS_OpenError
PCDM_RS_NoVersion = _PCDM.PCDM_RS_NoVersion
PCDM_RS_NoSchema = _PCDM.PCDM_RS_NoSchema
PCDM_RS_NoDocument = _PCDM.PCDM_RS_NoDocument
PCDM_RS_ExtensionFailure = _PCDM.PCDM_RS_ExtensionFailure
PCDM_RS_WrongStreamMode = _PCDM.PCDM_RS_WrongStreamMode
PCDM_RS_FormatFailure = _PCDM.PCDM_RS_FormatFailure
PCDM_RS_TypeFailure = _PCDM.PCDM_RS_TypeFailure
PCDM_RS_TypeNotFoundInSchema = _PCDM.PCDM_RS_TypeNotFoundInSchema
PCDM_RS_UnrecognizedFileFormat = _PCDM.PCDM_RS_UnrecognizedFileFormat
PCDM_RS_MakeFailure = _PCDM.PCDM_RS_MakeFailure
PCDM_RS_PermissionDenied = _PCDM.PCDM_RS_PermissionDenied
PCDM_RS_DriverFailure = _PCDM.PCDM_RS_DriverFailure
PCDM_RS_AlreadyRetrievedAndModified = _PCDM.PCDM_RS_AlreadyRetrievedAndModified
PCDM_RS_AlreadyRetrieved = _PCDM.PCDM_RS_AlreadyRetrieved
PCDM_RS_UnknownDocument = _PCDM.PCDM_RS_UnknownDocument
PCDM_RS_WrongResource = _PCDM.PCDM_RS_WrongResource
PCDM_RS_ReaderException = _PCDM.PCDM_RS_ReaderException
PCDM_RS_NoModel = _PCDM.PCDM_RS_NoModel
Handle_PCDM_ReadWriter_Create = _PCDM.Handle_PCDM_ReadWriter_Create
Handle_PCDM_ReadWriter_DownCast = _PCDM.Handle_PCDM_ReadWriter_DownCast
Handle_PCDM_ReadWriter_IsNull = _PCDM.Handle_PCDM_ReadWriter_IsNull
Handle_PCDM_Reader_Create = _PCDM.Handle_PCDM_Reader_Create
Handle_PCDM_Reader_DownCast = _PCDM.Handle_PCDM_Reader_DownCast
Handle_PCDM_Reader_IsNull = _PCDM.Handle_PCDM_Reader_IsNull
Handle_PCDM_ReferenceIterator_Create = _PCDM.Handle_PCDM_ReferenceIterator_Create
Handle_PCDM_ReferenceIterator_DownCast = _PCDM.Handle_PCDM_ReferenceIterator_DownCast
Handle_PCDM_ReferenceIterator_IsNull = _PCDM.Handle_PCDM_ReferenceIterator_IsNull
Handle_PCDM_Writer_Create = _PCDM.Handle_PCDM_Writer_Create
Handle_PCDM_Writer_DownCast = _PCDM.Handle_PCDM_Writer_DownCast
Handle_PCDM_Writer_IsNull = _PCDM.Handle_PCDM_Writer_IsNull
Handle_PCDM_ReadWriter_1_Create = _PCDM.Handle_PCDM_ReadWriter_1_Create
Handle_PCDM_ReadWriter_1_DownCast = _PCDM.Handle_PCDM_ReadWriter_1_DownCast
Handle_PCDM_ReadWriter_1_IsNull = _PCDM.Handle_PCDM_ReadWriter_1_IsNull
Handle_PCDM_RetrievalDriver_Create = _PCDM.Handle_PCDM_RetrievalDriver_Create
Handle_PCDM_RetrievalDriver_DownCast = _PCDM.Handle_PCDM_RetrievalDriver_DownCast
Handle_PCDM_RetrievalDriver_IsNull = _PCDM.Handle_PCDM_RetrievalDriver_IsNull
Handle_PCDM_StorageDriver_Create = _PCDM.Handle_PCDM_StorageDriver_Create
Handle_PCDM_StorageDriver_DownCast = _PCDM.Handle_PCDM_StorageDriver_DownCast
Handle_PCDM_StorageDriver_IsNull = _PCDM.Handle_PCDM_StorageDriver_IsNull
class PCDM_SequenceOfDocument(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_begin)
    end = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_end)
    cbegin = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_cbegin)
    cend = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_cend)

    def __init__(self, *args):
        _PCDM.PCDM_SequenceOfDocument_swiginit(self, _PCDM.new_PCDM_SequenceOfDocument(*args))
    Size = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Size)
    Length = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Length)
    Lower = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Lower)
    Upper = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Upper)
    IsEmpty = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_IsEmpty)
    Reverse = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Reverse)
    Exchange = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Exchange)
    delNode = _swig_new_static_method(_PCDM.PCDM_SequenceOfDocument_delNode)
    Clear = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Clear)
    Assign = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Assign)
    Set = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Set)
    Remove = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Remove)
    Append = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Append)
    Prepend = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Prepend)
    InsertBefore = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_InsertBefore)
    InsertAfter = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_InsertAfter)
    Split = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Split)
    First = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_First)
    ChangeFirst = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_ChangeFirst)
    Last = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Last)
    ChangeLast = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_ChangeLast)
    Value = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_Value)
    ChangeValue = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_ChangeValue)
    __call__ = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument___call__)
    SetValue = _swig_new_instance_method(_PCDM.PCDM_SequenceOfDocument_SetValue)
    __swig_destroy__ = _PCDM.delete_PCDM_SequenceOfDocument

# Register PCDM_SequenceOfDocument in _PCDM:
_PCDM.PCDM_SequenceOfDocument_swigregister(PCDM_SequenceOfDocument)
PCDM_SequenceOfDocument_delNode = _PCDM.PCDM_SequenceOfDocument_delNode

class PCDM_SequenceOfReference(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_begin)
    end = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_end)
    cbegin = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_cbegin)
    cend = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_cend)

    def __init__(self, *args):
        _PCDM.PCDM_SequenceOfReference_swiginit(self, _PCDM.new_PCDM_SequenceOfReference(*args))
    Size = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Size)
    Length = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Length)
    Lower = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Lower)
    Upper = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Upper)
    IsEmpty = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_IsEmpty)
    Reverse = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Reverse)
    Exchange = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Exchange)
    delNode = _swig_new_static_method(_PCDM.PCDM_SequenceOfReference_delNode)
    Clear = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Clear)
    Assign = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Assign)
    Set = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Set)
    Remove = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Remove)
    Append = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Append)
    Prepend = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Prepend)
    InsertBefore = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_InsertBefore)
    InsertAfter = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_InsertAfter)
    Split = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Split)
    First = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_First)
    ChangeFirst = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_ChangeFirst)
    Last = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Last)
    ChangeLast = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_ChangeLast)
    Value = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_Value)
    ChangeValue = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_ChangeValue)
    __call__ = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference___call__)
    SetValue = _swig_new_instance_method(_PCDM.PCDM_SequenceOfReference_SetValue)
    __swig_destroy__ = _PCDM.delete_PCDM_SequenceOfReference

# Register PCDM_SequenceOfReference in _PCDM:
_PCDM.PCDM_SequenceOfReference_swigregister(PCDM_SequenceOfReference)
PCDM_SequenceOfReference_delNode = _PCDM.PCDM_SequenceOfReference_delNode

class pcdm(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FileDriverType = _swig_new_static_method(_PCDM.pcdm_FileDriverType)

    __repr__ = _dumps_object


    def __init__(self):
        _PCDM.pcdm_swiginit(self, _PCDM.new_pcdm())
    __swig_destroy__ = _PCDM.delete_pcdm

# Register pcdm in _PCDM:
_PCDM.pcdm_swigregister(pcdm)
pcdm_FileDriverType = _PCDM.pcdm_FileDriverType

class PCDM_ReadWriter(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    FileFormat = _swig_new_static_method(_PCDM.PCDM_ReadWriter_FileFormat)
    Open = _swig_new_static_method(_PCDM.PCDM_ReadWriter_Open)
    ReadDocumentVersion = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_ReadDocumentVersion)
    ReadExtensions = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_ReadExtensions)
    ReadReferenceCounter = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_ReadReferenceCounter)
    ReadReferences = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_ReadReferences)
    Reader = _swig_new_static_method(_PCDM.PCDM_ReadWriter_Reader)
    Version = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_Version)
    WriteExtensions = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_WriteExtensions)
    WriteFileFormat = _swig_new_static_method(_PCDM.PCDM_ReadWriter_WriteFileFormat)
    WriteReferenceCounter = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_WriteReferenceCounter)
    WriteReferences = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_WriteReferences)
    WriteVersion = _swig_new_instance_method(_PCDM.PCDM_ReadWriter_WriteVersion)
    Writer = _swig_new_static_method(_PCDM.PCDM_ReadWriter_Writer)


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_ReadWriter_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_ReadWriter

# Register PCDM_ReadWriter in _PCDM:
_PCDM.PCDM_ReadWriter_swigregister(PCDM_ReadWriter)
PCDM_ReadWriter_FileFormat = _PCDM.PCDM_ReadWriter_FileFormat
PCDM_ReadWriter_Open = _PCDM.PCDM_ReadWriter_Open
PCDM_ReadWriter_Reader = _PCDM.PCDM_ReadWriter_Reader
PCDM_ReadWriter_WriteFileFormat = _PCDM.PCDM_ReadWriter_WriteFileFormat
PCDM_ReadWriter_Writer = _PCDM.PCDM_ReadWriter_Writer

class PCDM_Reader(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    CreateDocument = _swig_new_instance_method(_PCDM.PCDM_Reader_CreateDocument)
    GetStatus = _swig_new_instance_method(_PCDM.PCDM_Reader_GetStatus)
    Read = _swig_new_instance_method(_PCDM.PCDM_Reader_Read)


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_Reader_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_Reader

# Register PCDM_Reader in _PCDM:
_PCDM.PCDM_Reader_swigregister(PCDM_Reader)

class PCDM_Reference(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DocumentVersion = _swig_new_instance_method(_PCDM.PCDM_Reference_DocumentVersion)
    FileName = _swig_new_instance_method(_PCDM.PCDM_Reference_FileName)

    def __init__(self, *args):
        r"""
        :rtype: None:param aReferenceIdentifier:
        	:type aReferenceIdentifier: int
        	:param aFileName:
        	:type aFileName: TCollection_ExtendedString
        	:param aDocumentVersion:
        	:type aDocumentVersion: int
        	:rtype: None
        """
        _PCDM.PCDM_Reference_swiginit(self, _PCDM.new_PCDM_Reference(*args))
    ReferenceIdentifier = _swig_new_instance_method(_PCDM.PCDM_Reference_ReferenceIdentifier)

    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_Reference

# Register PCDM_Reference in _PCDM:
_PCDM.PCDM_Reference_swigregister(PCDM_Reference)

class PCDM_ReferenceIterator(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Init = _swig_new_instance_method(_PCDM.PCDM_ReferenceIterator_Init)
    LoadReferences = _swig_new_instance_method(_PCDM.PCDM_ReferenceIterator_LoadReferences)

    def __init__(self, *args):
        r"""
        * Warning! The constructor does not initialization.
        	:param theMessageDriver:
        	:type theMessageDriver: Message_Messenger
        	:rtype: None
        """
        _PCDM.PCDM_ReferenceIterator_swiginit(self, _PCDM.new_PCDM_ReferenceIterator(*args))


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_ReferenceIterator_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_ReferenceIterator

# Register PCDM_ReferenceIterator in _PCDM:
_PCDM.PCDM_ReferenceIterator_swigregister(PCDM_ReferenceIterator)

class PCDM_Writer(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Write = _swig_new_instance_method(_PCDM.PCDM_Writer_Write)


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_Writer_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_Writer

# Register PCDM_Writer in _PCDM:
_PCDM.PCDM_Writer_swigregister(PCDM_Writer)

class PCDM_ReadWriter_1(PCDM_ReadWriter):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r""":rtype: None"""
        _PCDM.PCDM_ReadWriter_1_swiginit(self, _PCDM.new_PCDM_ReadWriter_1(*args))


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_ReadWriter_1_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_ReadWriter_1

# Register PCDM_ReadWriter_1 in _PCDM:
_PCDM.PCDM_ReadWriter_1_swigregister(PCDM_ReadWriter_1)

class PCDM_RetrievalDriver(PCDM_Reader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    DocumentVersion = _swig_new_static_method(_PCDM.PCDM_RetrievalDriver_DocumentVersion)
    GetFormat = _swig_new_instance_method(_PCDM.PCDM_RetrievalDriver_GetFormat)
    ReferenceCounter = _swig_new_static_method(_PCDM.PCDM_RetrievalDriver_ReferenceCounter)
    SetFormat = _swig_new_instance_method(_PCDM.PCDM_RetrievalDriver_SetFormat)


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_RetrievalDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _PCDM.delete_PCDM_RetrievalDriver

# Register PCDM_RetrievalDriver in _PCDM:
_PCDM.PCDM_RetrievalDriver_swigregister(PCDM_RetrievalDriver)
PCDM_RetrievalDriver_DocumentVersion = _PCDM.PCDM_RetrievalDriver_DocumentVersion
PCDM_RetrievalDriver_ReferenceCounter = _PCDM.PCDM_RetrievalDriver_ReferenceCounter

class PCDM_StorageDriver(PCDM_Writer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetFormat = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_GetFormat)
    GetStoreStatus = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_GetStoreStatus)
    IsError = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_IsError)
    Make = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_Make)
    SetFormat = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_SetFormat)
    SetIsError = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_SetIsError)
    SetStoreStatus = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_SetStoreStatus)
    Write = _swig_new_instance_method(_PCDM.PCDM_StorageDriver_Write)


    @staticmethod
    def DownCast(t):
      return Handle_PCDM_StorageDriver_DownCast(t)


    __repr__ = _dumps_object


    def __init__(self):
        _PCDM.PCDM_StorageDriver_swiginit(self, _PCDM.new_PCDM_StorageDriver())
    __swig_destroy__ = _PCDM.delete_PCDM_StorageDriver

# Register PCDM_StorageDriver in _PCDM:
_PCDM.PCDM_StorageDriver_swigregister(PCDM_StorageDriver)



