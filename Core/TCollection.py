# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
TCollection module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_tcollection.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _TCollection
else:
    import _TCollection

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _TCollection.SWIG_PyInstanceMethod_New
_swig_new_static_method = _TCollection.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _TCollection.delete_SwigPyIterator
    value = _swig_new_instance_method(_TCollection.SwigPyIterator_value)
    incr = _swig_new_instance_method(_TCollection.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_TCollection.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_TCollection.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_TCollection.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_TCollection.SwigPyIterator_copy)
    next = _swig_new_instance_method(_TCollection.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_TCollection.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_TCollection.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_TCollection.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_TCollection.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_TCollection.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_TCollection.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_TCollection.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_TCollection.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_TCollection.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _TCollection:
_TCollection.SwigPyIterator_swigregister(SwigPyIterator)


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
TCollection_Left = _TCollection.TCollection_Left
TCollection_Right = _TCollection.TCollection_Right
Handle_TCollection_HAsciiString_Create = _TCollection.Handle_TCollection_HAsciiString_Create
Handle_TCollection_HAsciiString_DownCast = _TCollection.Handle_TCollection_HAsciiString_DownCast
Handle_TCollection_HAsciiString_IsNull = _TCollection.Handle_TCollection_HAsciiString_IsNull
Handle_TCollection_HExtendedString_Create = _TCollection.Handle_TCollection_HExtendedString_Create
Handle_TCollection_HExtendedString_DownCast = _TCollection.Handle_TCollection_HExtendedString_DownCast
Handle_TCollection_HExtendedString_IsNull = _TCollection.Handle_TCollection_HExtendedString_IsNull
Handle_TCollection_MapNode_Create = _TCollection.Handle_TCollection_MapNode_Create
Handle_TCollection_MapNode_DownCast = _TCollection.Handle_TCollection_MapNode_DownCast
Handle_TCollection_MapNode_IsNull = _TCollection.Handle_TCollection_MapNode_IsNull
Handle_TCollection_SeqNode_Create = _TCollection.Handle_TCollection_SeqNode_Create
Handle_TCollection_SeqNode_DownCast = _TCollection.Handle_TCollection_SeqNode_DownCast
Handle_TCollection_SeqNode_IsNull = _TCollection.Handle_TCollection_SeqNode_IsNull
class tcollection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    NextPrimeForMap = _swig_new_static_method(_TCollection.tcollection_NextPrimeForMap)

    __repr__ = _dumps_object


    def __init__(self):
        _TCollection.tcollection_swiginit(self, _TCollection.new_tcollection())
    __swig_destroy__ = _TCollection.delete_tcollection

# Register tcollection in _TCollection:
_TCollection.tcollection_swigregister(tcollection)
tcollection_NextPrimeForMap = _TCollection.tcollection_NextPrimeForMap

class TCollection_AsciiString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AssignCat = _swig_new_instance_method(_TCollection.TCollection_AsciiString_AssignCat)
    Capitalize = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Capitalize)
    Cat = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Cat)
    Center = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Center)
    ChangeAll = _swig_new_instance_method(_TCollection.TCollection_AsciiString_ChangeAll)
    Clear = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Clear)
    Copy = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Copy)
    EndsWith = _swig_new_instance_method(_TCollection.TCollection_AsciiString_EndsWith)
    FirstLocationInSet = _swig_new_instance_method(_TCollection.TCollection_AsciiString_FirstLocationInSet)
    FirstLocationNotInSet = _swig_new_instance_method(_TCollection.TCollection_AsciiString_FirstLocationNotInSet)
    HashCode = _swig_new_static_method(_TCollection.TCollection_AsciiString_HashCode)
    Insert = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Insert)
    InsertAfter = _swig_new_instance_method(_TCollection.TCollection_AsciiString_InsertAfter)
    InsertBefore = _swig_new_instance_method(_TCollection.TCollection_AsciiString_InsertBefore)
    IntegerValue = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IntegerValue)
    IsAscii = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsAscii)
    IsDifferent = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsDifferent)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsEmpty)
    IsEqual = _swig_new_static_method(_TCollection.TCollection_AsciiString_IsEqual)
    IsGreater = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsGreater)
    IsIntegerValue = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsIntegerValue)
    IsLess = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsLess)
    IsRealValue = _swig_new_instance_method(_TCollection.TCollection_AsciiString_IsRealValue)
    IsSameString = _swig_new_static_method(_TCollection.TCollection_AsciiString_IsSameString)
    LeftAdjust = _swig_new_instance_method(_TCollection.TCollection_AsciiString_LeftAdjust)
    LeftJustify = _swig_new_instance_method(_TCollection.TCollection_AsciiString_LeftJustify)
    Length = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Length)
    Location = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Location)
    LowerCase = _swig_new_instance_method(_TCollection.TCollection_AsciiString_LowerCase)
    Prepend = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Prepend)
    PrintToString = _swig_new_instance_method(_TCollection.TCollection_AsciiString_PrintToString)
    ReadFromString = _swig_new_instance_method(_TCollection.TCollection_AsciiString_ReadFromString)
    RealValue = _swig_new_instance_method(_TCollection.TCollection_AsciiString_RealValue)
    Remove = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Remove)
    RemoveAll = _swig_new_instance_method(_TCollection.TCollection_AsciiString_RemoveAll)
    RightAdjust = _swig_new_instance_method(_TCollection.TCollection_AsciiString_RightAdjust)
    RightJustify = _swig_new_instance_method(_TCollection.TCollection_AsciiString_RightJustify)
    Search = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Search)
    SearchFromEnd = _swig_new_instance_method(_TCollection.TCollection_AsciiString_SearchFromEnd)
    SetValue = _swig_new_instance_method(_TCollection.TCollection_AsciiString_SetValue)
    Split = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Split)
    StartsWith = _swig_new_instance_method(_TCollection.TCollection_AsciiString_StartsWith)
    SubString = _swig_new_instance_method(_TCollection.TCollection_AsciiString_SubString)
    Swap = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Swap)

    def __init__(self, *args):
        r"""
        * Initializes a AsciiString to an empty AsciiString.
        	:rtype: None* Initializes a AsciiString with a CString.
        	:param message:
        	:type message: char *
        	:rtype: None* Initializes a AsciiString with a CString.
        	:param message:
        	:type message: char *
        	:param aLen:
        	:type aLen: int
        	:rtype: None* Initializes a AsciiString with a single character.
        	:param aChar:
        	:type aChar: Standard_Character
        	:rtype: None* Initializes an AsciiString with <length> space allocated. and filled with <filler>. This is usefull for buffers.
        	:param length:
        	:type length: int
        	:param filler:
        	:type filler: Standard_Character
        	:rtype: None* Initializes an AsciiString with an integer value
        	:param value:
        	:type value: int
        	:rtype: None* Initializes an AsciiString with a real value
        	:param value:
        	:type value: float
        	:rtype: None* Initializes a AsciiString with another AsciiString.
        	:param astring:
        	:type astring: TCollection_AsciiString
        	:rtype: None* Move constructor
        	:param theOther:
        	:type theOther: TCollection_AsciiString
        	:rtype: None* Initializes a AsciiString with copy of another AsciiString concatenated with the message character.
        	:param astring:
        	:type astring: TCollection_AsciiString
        	:param message:
        	:type message: Standard_Character
        	:rtype: None* Initializes a AsciiString with copy of another AsciiString concatenated with the message string.
        	:param astring:
        	:type astring: TCollection_AsciiString
        	:param message:
        	:type message: char *
        	:rtype: None* Initializes a AsciiString with copy of another AsciiString concatenated with the message string.
        	:param astring:
        	:type astring: TCollection_AsciiString
        	:param message:
        	:type message: TCollection_AsciiString
        	:rtype: None* Creation by converting an extended string to an ascii string. If replaceNonAscii is non-null charecter, it will be used in place of any non-ascii character found in the source string. Otherwise, creates UTF-8 unicode string.
        	:param astring:
        	:type astring: TCollection_ExtendedString
        	:param replaceNonAscii: default value is 0
        	:type replaceNonAscii: Standard_Character
        	:rtype: None* Initialize UTF-8 Unicode string from wide-char string considering it as Unicode string (the size of wide char is a platform-dependent - e.g. on Windows wchar_t is UTF-16). //! This constructor is unavailable if application is built with deprecated msvc option '-Zc:wchar_t-', since OCCT itself is never built with this option.
        	:param theStringUtf:
        	:type theStringUtf: Standard_WideChar *
        	:rtype: None
        """
        _TCollection.TCollection_AsciiString_swiginit(self, _TCollection.new_TCollection_AsciiString(*args))
    ToCString = _swig_new_instance_method(_TCollection.TCollection_AsciiString_ToCString)
    Token = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Token)
    Trunc = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Trunc)
    UpperCase = _swig_new_instance_method(_TCollection.TCollection_AsciiString_UpperCase)
    UsefullLength = _swig_new_instance_method(_TCollection.TCollection_AsciiString_UsefullLength)
    Value = _swig_new_instance_method(_TCollection.TCollection_AsciiString_Value)
    __add__ = _swig_new_instance_method(_TCollection.TCollection_AsciiString___add__)

    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self


    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self


    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self


    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self

    __iadd_wrapper__ = _swig_new_instance_method(_TCollection.TCollection_AsciiString___iadd_wrapper__)

    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self


    def __eq__(self, right):
        try:
            return self.__eq_wrapper__(right)
        except:
            return False

    __eq_wrapper__ = _swig_new_instance_method(_TCollection.TCollection_AsciiString___eq_wrapper__)

    def __eq__(self, right):
        try:
            return self.__eq_wrapper__(right)
        except:
            return False

    __gt__ = _swig_new_instance_method(_TCollection.TCollection_AsciiString___gt__)

    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_AsciiString

# Register TCollection_AsciiString in _TCollection:
_TCollection.TCollection_AsciiString_swigregister(TCollection_AsciiString)
TCollection_AsciiString_HashCode = _TCollection.TCollection_AsciiString_HashCode
TCollection_AsciiString_IsEqual = _TCollection.TCollection_AsciiString_IsEqual
TCollection_AsciiString_IsSameString = _TCollection.TCollection_AsciiString_IsSameString

class TCollection_BaseSequence(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Exchange = _swig_new_instance_method(_TCollection.TCollection_BaseSequence_Exchange)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_BaseSequence_IsEmpty)
    Length = _swig_new_instance_method(_TCollection.TCollection_BaseSequence_Length)
    Reverse = _swig_new_instance_method(_TCollection.TCollection_BaseSequence_Reverse)

    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_BaseSequence

# Register TCollection_BaseSequence in _TCollection:
_TCollection.TCollection_BaseSequence_swigregister(TCollection_BaseSequence)

class TCollection_BasicMap(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Extent = _swig_new_instance_method(_TCollection.TCollection_BasicMap_Extent)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_BasicMap_IsEmpty)
    NbBuckets = _swig_new_instance_method(_TCollection.TCollection_BasicMap_NbBuckets)
    StatisticsToString = _swig_new_instance_method(_TCollection.TCollection_BasicMap_StatisticsToString)

    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_BasicMap

# Register TCollection_BasicMap in _TCollection:
_TCollection.TCollection_BasicMap_swigregister(TCollection_BasicMap)

class TCollection_BasicMapIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    More = _swig_new_instance_method(_TCollection.TCollection_BasicMapIterator_More)
    Next = _swig_new_instance_method(_TCollection.TCollection_BasicMapIterator_Next)
    Reset = _swig_new_instance_method(_TCollection.TCollection_BasicMapIterator_Reset)

    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_BasicMapIterator

# Register TCollection_BasicMapIterator in _TCollection:
_TCollection.TCollection_BasicMapIterator_swigregister(TCollection_BasicMapIterator)

class TCollection_ExtendedString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AssignCat = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_AssignCat)
    Cat = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Cat)
    ChangeAll = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_ChangeAll)
    Clear = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Clear)
    Copy = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Copy)
    EndsWith = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_EndsWith)
    HashCode = _swig_new_static_method(_TCollection.TCollection_ExtendedString_HashCode)
    Insert = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Insert)
    IsAscii = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_IsAscii)
    IsDifferent = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_IsDifferent)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_IsEmpty)
    IsEqual = _swig_new_static_method(_TCollection.TCollection_ExtendedString_IsEqual)
    IsGreater = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_IsGreater)
    IsLess = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_IsLess)
    Length = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Length)
    LengthOfCString = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_LengthOfCString)
    PrintToString = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_PrintToString)
    Remove = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Remove)
    RemoveAll = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_RemoveAll)
    Search = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Search)
    SearchFromEnd = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_SearchFromEnd)
    SetValue = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_SetValue)
    Split = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Split)
    StartsWith = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_StartsWith)
    Swap = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Swap)

    def __init__(self, *args):
        r"""
        * Initializes a ExtendedString to an empty ExtendedString.
        	:rtype: None* Creation by converting a CString to an extended string. If <isMultiByte> is true then the string is treated as having UTF-8 coding. If it is not a UTF-8 then <isMultiByte> is ignored and each character is copied to ExtCharacter.
        	:param astring:
        	:type astring: char *
        	:param isMultiByte: default value is Standard_False
        	:type isMultiByte: bool
        	:rtype: None* Creation by converting an ExtString to an extended string.
        	:param astring:
        	:type astring: Standard_ExtString
        	:rtype: None* Initialize from wide-char string considering it as Unicode string (the size of wide char is a platform-dependent - e.g. on Windows wchar_t is UTF-16). //! This constructor is unavailable if application is built with deprecated msvc option '-Zc:wchar_t-', since OCCT itself is never built with this option.
        	:param theStringUtf:
        	:type theStringUtf: Standard_WideChar *
        	:rtype: None* Initializes a AsciiString with a single character.
        	:param aChar:
        	:type aChar: Standard_Character
        	:rtype: None* Initializes a ExtendedString with a single character.
        	:param aChar:
        	:type aChar: Standard_ExtCharacter
        	:rtype: None* Initializes a ExtendedString with <length> space allocated. and filled with <filler>.This is useful for buffers.
        	:param length:
        	:type length: int
        	:param filler:
        	:type filler: Standard_ExtCharacter
        	:rtype: None* Initializes an ExtendedString with an integer value
        	:param value:
        	:type value: int
        	:rtype: None* Initializes an ExtendedString with a real value
        	:param value:
        	:type value: float
        	:rtype: None* Initializes a ExtendedString with another ExtendedString.
        	:param astring:
        	:type astring: TCollection_ExtendedString
        	:rtype: None* Move constructor
        	:param theOther:
        	:type theOther: TCollection_ExtendedString
        	:rtype: None* Creation by converting an Ascii string to an extended string. The string is treated as having UTF-8 coding. If it is not a UTF-8 then each character is copied to ExtCharacter.
        	:param astring:
        	:type astring: TCollection_AsciiString
        	:rtype: None
        """
        _TCollection.TCollection_ExtendedString_swiginit(self, _TCollection.new_TCollection_ExtendedString(*args))
    ToExtString = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_ToExtString)
    ToUTF8CString = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_ToUTF8CString)
    Token = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Token)
    Trunc = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Trunc)
    Value = _swig_new_instance_method(_TCollection.TCollection_ExtendedString_Value)
    __add__ = _swig_new_instance_method(_TCollection.TCollection_ExtendedString___add__)
    __iadd_wrapper__ = _swig_new_instance_method(_TCollection.TCollection_ExtendedString___iadd_wrapper__)

    def __iadd__(self, right):
        self.__iadd_wrapper__(right)
        return self


    def __eq__(self, right):
        try:
            return self.__eq_wrapper__(right)
        except:
            return False

    __eq_wrapper__ = _swig_new_instance_method(_TCollection.TCollection_ExtendedString___eq_wrapper__)

    def __eq__(self, right):
        try:
            return self.__eq_wrapper__(right)
        except:
            return False

    __gt__ = _swig_new_instance_method(_TCollection.TCollection_ExtendedString___gt__)

    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_ExtendedString

# Register TCollection_ExtendedString in _TCollection:
_TCollection.TCollection_ExtendedString_swigregister(TCollection_ExtendedString)
TCollection_ExtendedString_HashCode = _TCollection.TCollection_ExtendedString_HashCode
TCollection_ExtendedString_IsEqual = _TCollection.TCollection_ExtendedString_IsEqual

class TCollection_HAsciiString(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AssignCat = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_AssignCat)
    Capitalize = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Capitalize)
    Cat = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Cat)
    Center = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Center)
    ChangeAll = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_ChangeAll)
    Clear = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Clear)
    FirstLocationInSet = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_FirstLocationInSet)
    FirstLocationNotInSet = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_FirstLocationNotInSet)
    Insert = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Insert)
    InsertAfter = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_InsertAfter)
    InsertBefore = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_InsertBefore)
    IntegerValue = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IntegerValue)
    IsAscii = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsAscii)
    IsDifferent = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsDifferent)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsEmpty)
    IsGreater = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsGreater)
    IsIntegerValue = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsIntegerValue)
    IsLess = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsLess)
    IsRealValue = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsRealValue)
    IsSameState = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsSameState)
    IsSameString = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_IsSameString)
    LeftAdjust = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_LeftAdjust)
    LeftJustify = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_LeftJustify)
    Length = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Length)
    Location = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Location)
    LowerCase = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_LowerCase)
    Prepend = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Prepend)
    PrintToString = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_PrintToString)
    RealValue = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_RealValue)
    Remove = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Remove)
    RemoveAll = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_RemoveAll)
    RightAdjust = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_RightAdjust)
    RightJustify = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_RightJustify)
    Search = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Search)
    SearchFromEnd = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_SearchFromEnd)
    SetValue = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_SetValue)
    Split = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Split)
    String = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_String)
    SubString = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_SubString)

    def __init__(self, *args):
        r"""
        * Initializes a HAsciiString to an empty AsciiString.
        	:rtype: None* Initializes a HAsciiString with a CString.
        	:param message:
        	:type message: char *
        	:rtype: None* Initializes a HAsciiString with a single character.
        	:param aChar:
        	:type aChar: Standard_Character
        	:rtype: None* Initializes a HAsciiString with <length> space allocated. and filled with <filler>.This is useful for buffers.
        	:param length:
        	:type length: int
        	:param filler:
        	:type filler: Standard_Character
        	:rtype: None* Initializes a HAsciiString with an integer value
        	:param value:
        	:type value: int
        	:rtype: None* Initializes a HAsciiString with a real value
        	:param value:
        	:type value: float
        	:rtype: None* Initializes a HAsciiString with a HAsciiString.
        	:param aString:
        	:type aString: TCollection_AsciiString
        	:rtype: None* Initializes a HAsciiString with a HAsciiString.
        	:param aString:
        	:type aString: TCollection_HAsciiString
        	:rtype: None* Initializes a HAsciiString with a HAsciiString. If replaceNonAscii is non-null charecter, it will be used in place of any non-ascii character found in the source string. Otherwise, raises OutOfRange exception if at least one character in the source string is not in the 'Ascii range'.
        	:param aString:
        	:type aString: TCollection_HExtendedString
        	:param replaceNonAscii:
        	:type replaceNonAscii: Standard_Character
        	:rtype: None
        """
        _TCollection.TCollection_HAsciiString_swiginit(self, _TCollection.new_TCollection_HAsciiString(*args))
    ToCString = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_ToCString)
    Token = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Token)
    Trunc = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Trunc)
    UpperCase = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_UpperCase)
    UsefullLength = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_UsefullLength)
    Value = _swig_new_instance_method(_TCollection.TCollection_HAsciiString_Value)


    @staticmethod
    def DownCast(t):
      return Handle_TCollection_HAsciiString_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_HAsciiString

# Register TCollection_HAsciiString in _TCollection:
_TCollection.TCollection_HAsciiString_swigregister(TCollection_HAsciiString)

class TCollection_HExtendedString(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    AssignCat = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_AssignCat)
    Cat = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Cat)
    ChangeAll = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_ChangeAll)
    Clear = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Clear)
    Insert = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Insert)
    IsAscii = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_IsAscii)
    IsEmpty = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_IsEmpty)
    IsGreater = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_IsGreater)
    IsLess = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_IsLess)
    IsSameState = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_IsSameState)
    Length = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Length)
    PrintToString = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_PrintToString)
    Remove = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Remove)
    RemoveAll = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_RemoveAll)
    Search = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Search)
    SearchFromEnd = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_SearchFromEnd)
    SetValue = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_SetValue)
    Split = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Split)
    String = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_String)

    def __init__(self, *args):
        r"""
        * Initializes a HExtendedString to an empty ExtendedString.
        	:rtype: None* Initializes a HExtendedString with a CString.
        	:param message:
        	:type message: char *
        	:rtype: None* Initializes a HExtendedString with an ExtString.
        	:param message:
        	:type message: Standard_ExtString
        	:rtype: None* Initializes a HExtendedString with a single character.
        	:param aChar:
        	:type aChar: Standard_ExtCharacter
        	:rtype: None* Initializes a HExtendedString with <length> space allocated. and filled with <filler>.This is usefull for buffers.
        	:param length:
        	:type length: int
        	:param filler:
        	:type filler: Standard_ExtCharacter
        	:rtype: None* Initializes a HExtendedString with a HExtendedString.
        	:param aString:
        	:type aString: TCollection_ExtendedString
        	:rtype: None* Initializes a HExtendedString with an HAsciiString.
        	:param aString:
        	:type aString: TCollection_HAsciiString
        	:rtype: None* Initializes a HExtendedString with a HExtendedString.
        	:param aString:
        	:type aString: TCollection_HExtendedString
        	:rtype: None
        """
        _TCollection.TCollection_HExtendedString_swiginit(self, _TCollection.new_TCollection_HExtendedString(*args))
    ToExtString = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_ToExtString)
    Token = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Token)
    Trunc = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Trunc)
    Value = _swig_new_instance_method(_TCollection.TCollection_HExtendedString_Value)


    @staticmethod
    def DownCast(t):
      return Handle_TCollection_HExtendedString_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_HExtendedString

# Register TCollection_HExtendedString in _TCollection:
_TCollection.TCollection_HExtendedString_swigregister(TCollection_HExtendedString)

class TCollection_MapNode(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Next = _swig_new_instance_method(_TCollection.TCollection_MapNode_Next)

    def __init__(self, *args):
        r"""
        :param n:
        	:type n: TCollection_MapNodePtr
        	:rtype: None
        """
        _TCollection.TCollection_MapNode_swiginit(self, _TCollection.new_TCollection_MapNode(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TCollection_MapNode_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_MapNode

# Register TCollection_MapNode in _TCollection:
_TCollection.TCollection_MapNode_swigregister(TCollection_MapNode)

class TCollection_SeqNode(OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Next = _swig_new_instance_method(_TCollection.TCollection_SeqNode_Next)
    Previous = _swig_new_instance_method(_TCollection.TCollection_SeqNode_Previous)

    def __init__(self, *args):
        r"""
        :param n:
        	:type n: TCollection_SeqNodePtr
        	:param p:
        	:type p: TCollection_SeqNodePtr
        	:rtype: None
        """
        _TCollection.TCollection_SeqNode_swiginit(self, _TCollection.new_TCollection_SeqNode(*args))


    @staticmethod
    def DownCast(t):
      return Handle_TCollection_SeqNode_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _TCollection.delete_TCollection_SeqNode

# Register TCollection_SeqNode in _TCollection:
_TCollection.TCollection_SeqNode_swigregister(TCollection_SeqNode)



