# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
XCAFPrs module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_xcafprs.html
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _XCAFPrs
else:
    import _XCAFPrs

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _XCAFPrs.SWIG_PyInstanceMethod_New
_swig_new_static_method = _XCAFPrs.SWIG_PyStaticMethod_New

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
    __swig_destroy__ = _XCAFPrs.delete_SwigPyIterator
    value = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_value)
    incr = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_copy)
    next = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_XCAFPrs.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_XCAFPrs.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _XCAFPrs:
_XCAFPrs.SwigPyIterator_swigregister(SwigPyIterator)


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
import OCC.Core.TDF
import OCC.Core.TCollection
import OCC.Core.TColStd
import OCC.Core.TopLoc
import OCC.Core.gp
import OCC.Core.Quantity
import OCC.Core.AIS
import OCC.Core.SelectMgr
import OCC.Core.PrsMgr
import OCC.Core.Prs3d
import OCC.Core.TColgp
import OCC.Core.Graphic3d
import OCC.Core.BVH
import OCC.Core.Aspect
import OCC.Core.Geom
import OCC.Core.GeomAbs
import OCC.Core.Bnd
import OCC.Core.Image
import OCC.Core.OSD
import OCC.Core.TopoDS
import OCC.Core.Message
import OCC.Core.TopAbs
import OCC.Core.HLRAlgo
import OCC.Core.Poly
import OCC.Core.TShort
import OCC.Core.TopTools
import OCC.Core.V3d
import OCC.Core.SelectBasics
import OCC.Core.Select3D
import OCC.Core.StdSelect
import OCC.Core.DsgPrs
import OCC.Core.TDocStd
import OCC.Core.CDF
import OCC.Core.CDM
import OCC.Core.Resource
import OCC.Core.PCDM
import OCC.Core.Storage
import OCC.Core.TPrsStd
import OCC.Core.TDataXtd
import OCC.Core.TNaming
import OCC.Core.TDataStd
XCAFPrs_DocumentExplorerFlags_None = _XCAFPrs.XCAFPrs_DocumentExplorerFlags_None
XCAFPrs_DocumentExplorerFlags_OnlyLeafNodes = _XCAFPrs.XCAFPrs_DocumentExplorerFlags_OnlyLeafNodes
XCAFPrs_DocumentExplorerFlags_NoStyle = _XCAFPrs.XCAFPrs_DocumentExplorerFlags_NoStyle
Handle_XCAFPrs_AISObject_Create = _XCAFPrs.Handle_XCAFPrs_AISObject_Create
Handle_XCAFPrs_AISObject_DownCast = _XCAFPrs.Handle_XCAFPrs_AISObject_DownCast
Handle_XCAFPrs_AISObject_IsNull = _XCAFPrs.Handle_XCAFPrs_AISObject_IsNull
Handle_XCAFPrs_Driver_Create = _XCAFPrs.Handle_XCAFPrs_Driver_Create
Handle_XCAFPrs_Driver_DownCast = _XCAFPrs.Handle_XCAFPrs_Driver_DownCast
Handle_XCAFPrs_Driver_IsNull = _XCAFPrs.Handle_XCAFPrs_Driver_IsNull
class XCAFPrs_DataMapOfStyleShape(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_begin)
    end = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_end)
    cbegin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_cbegin)
    cend = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_cend)

    def __init__(self, *args):
        _XCAFPrs.XCAFPrs_DataMapOfStyleShape_swiginit(self, _XCAFPrs.new_XCAFPrs_DataMapOfStyleShape(*args))
    Exchange = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Exchange)
    Assign = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Assign)
    Set = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Set)
    ReSize = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_ReSize)
    Bind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Bind)
    Bound = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Bound)
    IsBound = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_IsBound)
    UnBind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_UnBind)
    Seek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Seek)
    Find = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Find)
    ChangeSeek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_ChangeFind)
    __call__ = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape___call__)
    Clear = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Clear)
    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_DataMapOfStyleShape
    Size = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleShape_Size)

# Register XCAFPrs_DataMapOfStyleShape in _XCAFPrs:
_XCAFPrs.XCAFPrs_DataMapOfStyleShape_swigregister(XCAFPrs_DataMapOfStyleShape)

class XCAFPrs_DataMapOfStyleTransient(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_begin)
    end = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_end)
    cbegin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_cbegin)
    cend = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_cend)

    def __init__(self, *args):
        _XCAFPrs.XCAFPrs_DataMapOfStyleTransient_swiginit(self, _XCAFPrs.new_XCAFPrs_DataMapOfStyleTransient(*args))
    Exchange = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Exchange)
    Assign = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Assign)
    Set = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Set)
    ReSize = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_ReSize)
    Bind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Bind)
    Bound = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Bound)
    IsBound = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_IsBound)
    UnBind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_UnBind)
    Seek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Seek)
    Find = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Find)
    ChangeSeek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_ChangeSeek)
    ChangeFind = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_ChangeFind)
    __call__ = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient___call__)
    Clear = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Clear)
    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_DataMapOfStyleTransient
    Size = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_Size)

# Register XCAFPrs_DataMapOfStyleTransient in _XCAFPrs:
_XCAFPrs.XCAFPrs_DataMapOfStyleTransient_swigregister(XCAFPrs_DataMapOfStyleTransient)

class XCAFPrs_IndexedDataMapOfShapeStyle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    begin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_begin)
    end = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_end)
    cbegin = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_cbegin)
    cend = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_cend)

    def __init__(self, *args):
        _XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_swiginit(self, _XCAFPrs.new_XCAFPrs_IndexedDataMapOfShapeStyle(*args))
    Exchange = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Exchange)
    Assign = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Assign)
    Set = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Set)
    ReSize = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_ReSize)
    Add = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Add)
    Contains = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Contains)
    Substitute = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Substitute)
    Swap = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Swap)
    RemoveLast = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_RemoveLast)
    RemoveFromIndex = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_RemoveFromIndex)
    RemoveKey = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_RemoveKey)
    FindKey = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_FindKey)
    FindFromIndex = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_FindFromIndex)
    ChangeFromIndex = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_ChangeFromIndex)
    __call__ = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle___call__)
    FindIndex = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_FindIndex)
    ChangeFromKey = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_ChangeFromKey)
    Seek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Seek)
    ChangeSeek = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_ChangeSeek)
    FindFromKey = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_FindFromKey)
    Clear = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Clear)
    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_IndexedDataMapOfShapeStyle
    Size = _swig_new_instance_method(_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_Size)

# Register XCAFPrs_IndexedDataMapOfShapeStyle in _XCAFPrs:
_XCAFPrs.XCAFPrs_IndexedDataMapOfShapeStyle_swigregister(XCAFPrs_IndexedDataMapOfShapeStyle)

class xcafprs(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CollectStyleSettings = _swig_new_static_method(_XCAFPrs.xcafprs_CollectStyleSettings)
    GetViewNameMode = _swig_new_static_method(_XCAFPrs.xcafprs_GetViewNameMode)
    SetViewNameMode = _swig_new_static_method(_XCAFPrs.xcafprs_SetViewNameMode)

    __repr__ = _dumps_object


    def __init__(self):
        _XCAFPrs.xcafprs_swiginit(self, _XCAFPrs.new_xcafprs())
    __swig_destroy__ = _XCAFPrs.delete_xcafprs

# Register xcafprs in _XCAFPrs:
_XCAFPrs.xcafprs_swigregister(xcafprs)
xcafprs_CollectStyleSettings = _XCAFPrs.xcafprs_CollectStyleSettings
xcafprs_GetViewNameMode = _XCAFPrs.xcafprs_GetViewNameMode
xcafprs_SetViewNameMode = _XCAFPrs.xcafprs_SetViewNameMode

class XCAFPrs_AISObject(OCC.Core.AIS.AIS_ColoredShape):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DispatchStyles = _swig_new_instance_method(_XCAFPrs.XCAFPrs_AISObject_DispatchStyles)
    GetLabel = _swig_new_instance_method(_XCAFPrs.XCAFPrs_AISObject_GetLabel)
    SetLabel = _swig_new_instance_method(_XCAFPrs.XCAFPrs_AISObject_SetLabel)

    def __init__(self, *args):
        r"""
        * Creates an object to visualise the shape label.
        	:param theLabel:
        	:type theLabel: TDF_Label
        	:rtype: None
        """
        _XCAFPrs.XCAFPrs_AISObject_swiginit(self, _XCAFPrs.new_XCAFPrs_AISObject(*args))


    @staticmethod
    def DownCast(t):
      return Handle_XCAFPrs_AISObject_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_AISObject

# Register XCAFPrs_AISObject in _XCAFPrs:
_XCAFPrs.XCAFPrs_AISObject_swigregister(XCAFPrs_AISObject)

class XCAFPrs_DocumentExplorer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChangeCurrent = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_ChangeCurrent)
    Current = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_Current)
    CurrentDepth = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_CurrentDepth)
    DefineChildId = _swig_new_static_method(_XCAFPrs.XCAFPrs_DocumentExplorer_DefineChildId)
    FindLabelFromPathId = _swig_new_static_method(_XCAFPrs.XCAFPrs_DocumentExplorer_FindLabelFromPathId)
    FindShapeFromPathId = _swig_new_static_method(_XCAFPrs.XCAFPrs_DocumentExplorer_FindShapeFromPathId)
    Init = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_Init)
    More = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_More)
    Next = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentExplorer_Next)

    def __init__(self, *args):
        r"""
        * Empty constructor.
        	:rtype: None* Constructor for exploring the whole document. @param theDocument document to explore @param theFlags iteration flags @param theDefStyle default style for nodes with undefined style
        	:param theDocument:
        	:type theDocument: TDocStd_Document
        	:param theFlags:
        	:type theFlags: int
        	:param theDefStyle: default value is XCAFPrs_Style()
        	:type theDefStyle: XCAFPrs_Style
        	:rtype: None* Constructor for exploring specified list of root shapes in the document. @param theDocument document to explore @param theRoots root labels to explore within specified document @param theFlags iteration flags @param theDefStyle default style for nodes with undefined style
        	:param theDocument:
        	:type theDocument: TDocStd_Document
        	:param theRoots:
        	:type theRoots: TDF_LabelSequence
        	:param theFlags:
        	:type theFlags: int
        	:param theDefStyle: default value is XCAFPrs_Style()
        	:type theDefStyle: XCAFPrs_Style
        	:rtype: None
        """
        _XCAFPrs.XCAFPrs_DocumentExplorer_swiginit(self, _XCAFPrs.new_XCAFPrs_DocumentExplorer(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_DocumentExplorer

# Register XCAFPrs_DocumentExplorer in _XCAFPrs:
_XCAFPrs.XCAFPrs_DocumentExplorer_swigregister(XCAFPrs_DocumentExplorer)
XCAFPrs_DocumentExplorer_DefineChildId = _XCAFPrs.XCAFPrs_DocumentExplorer_DefineChildId
XCAFPrs_DocumentExplorer_FindLabelFromPathId = _XCAFPrs.XCAFPrs_DocumentExplorer_FindLabelFromPathId
XCAFPrs_DocumentExplorer_FindShapeFromPathId = _XCAFPrs.XCAFPrs_DocumentExplorer_FindShapeFromPathId

class XCAFPrs_DocumentIdIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    More = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentIdIterator_More)
    Next = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentIdIterator_Next)
    Value = _swig_new_instance_method(_XCAFPrs.XCAFPrs_DocumentIdIterator_Value)

    def __init__(self, *args):
        r"""
        * Main constructor.
        	:param thePath:
        	:type thePath: TCollection_AsciiString
        	:rtype: None
        """
        _XCAFPrs.XCAFPrs_DocumentIdIterator_swiginit(self, _XCAFPrs.new_XCAFPrs_DocumentIdIterator(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_DocumentIdIterator

# Register XCAFPrs_DocumentIdIterator in _XCAFPrs:
_XCAFPrs.XCAFPrs_DocumentIdIterator_swigregister(XCAFPrs_DocumentIdIterator)

class XCAFPrs_DocumentNode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Id = property(_XCAFPrs.XCAFPrs_DocumentNode_Id_get, _XCAFPrs.XCAFPrs_DocumentNode_Id_set)
    Label = property(_XCAFPrs.XCAFPrs_DocumentNode_Label_get, _XCAFPrs.XCAFPrs_DocumentNode_Label_set)
    RefLabel = property(_XCAFPrs.XCAFPrs_DocumentNode_RefLabel_get, _XCAFPrs.XCAFPrs_DocumentNode_RefLabel_set)
    Style = property(_XCAFPrs.XCAFPrs_DocumentNode_Style_get, _XCAFPrs.XCAFPrs_DocumentNode_Style_set)
    Location = property(_XCAFPrs.XCAFPrs_DocumentNode_Location_get, _XCAFPrs.XCAFPrs_DocumentNode_Location_set)
    LocalTrsf = property(_XCAFPrs.XCAFPrs_DocumentNode_LocalTrsf_get, _XCAFPrs.XCAFPrs_DocumentNode_LocalTrsf_set)
    ChildIter = property(_XCAFPrs.XCAFPrs_DocumentNode_ChildIter_get, _XCAFPrs.XCAFPrs_DocumentNode_ChildIter_set)
    IsAssembly = property(_XCAFPrs.XCAFPrs_DocumentNode_IsAssembly_get, _XCAFPrs.XCAFPrs_DocumentNode_IsAssembly_set)

    def __init__(self, *args):
        r"""
        * //!< flag indicating that this label is assembly
        	:rtype: None
        """
        _XCAFPrs.XCAFPrs_DocumentNode_swiginit(self, _XCAFPrs.new_XCAFPrs_DocumentNode(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_DocumentNode

# Register XCAFPrs_DocumentNode in _XCAFPrs:
_XCAFPrs.XCAFPrs_DocumentNode_swigregister(XCAFPrs_DocumentNode)

class XCAFPrs_Driver(OCC.Core.TPrsStd.TPrsStd_Driver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetID = _swig_new_static_method(_XCAFPrs.XCAFPrs_Driver_GetID)


    @staticmethod
    def DownCast(t):
      return Handle_XCAFPrs_Driver_DownCast(t)


    __repr__ = _dumps_object


    def __init__(self):
        _XCAFPrs.XCAFPrs_Driver_swiginit(self, _XCAFPrs.new_XCAFPrs_Driver())
    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_Driver

# Register XCAFPrs_Driver in _XCAFPrs:
_XCAFPrs.XCAFPrs_Driver_swigregister(XCAFPrs_Driver)
XCAFPrs_Driver_GetID = _XCAFPrs.XCAFPrs_Driver_GetID

class XCAFPrs_Style(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DumpJsonToString = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_DumpJsonToString)
    GetColorCurv = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_GetColorCurv)
    GetColorSurf = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_GetColorSurf)
    GetColorSurfRGBA = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_GetColorSurfRGBA)
    HashCode = _swig_new_static_method(_XCAFPrs.XCAFPrs_Style_HashCode)
    IsEqual = _swig_new_static_method(_XCAFPrs.XCAFPrs_Style_IsEqual)
    IsSetColorCurv = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_IsSetColorCurv)
    IsSetColorSurf = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_IsSetColorSurf)
    IsVisible = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_IsVisible)
    SetColorCurv = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_SetColorCurv)
    SetColorSurf = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_SetColorSurf)
    SetVisibility = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_SetVisibility)
    UnSetColorCurv = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_UnSetColorCurv)
    UnSetColorSurf = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style_UnSetColorSurf)

    def __init__(self, *args):
        r"""
        * Empty constructor - colors are unset, visibility is True.
        	:rtype: None
        """
        _XCAFPrs.XCAFPrs_Style_swiginit(self, _XCAFPrs.new_XCAFPrs_Style(*args))
    __eq_wrapper__ = _swig_new_instance_method(_XCAFPrs.XCAFPrs_Style___eq_wrapper__)

    def __eq__(self, right):
        try:
            return self.__eq_wrapper__(right)
        except:
            return False


    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFPrs.delete_XCAFPrs_Style

# Register XCAFPrs_Style in _XCAFPrs:
_XCAFPrs.XCAFPrs_Style_swigregister(XCAFPrs_Style)
XCAFPrs_Style_HashCode = _XCAFPrs.XCAFPrs_Style_HashCode
XCAFPrs_Style_IsEqual = _XCAFPrs.XCAFPrs_Style_IsEqual



