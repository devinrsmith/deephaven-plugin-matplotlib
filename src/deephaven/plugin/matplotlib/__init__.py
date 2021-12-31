__version__ = "0.0.1.dev1"

from deephaven.plugin.abc import CallbackABC, PluginBase
from deephaven.plugin.matplotlib.figure_type import FigureType

class MatplotlibPlugin(PluginBase):
    @classmethod
    def register_object_types_into(cls, callback: CallbackABC):
        # Either will work
        # callback.register_object_type(FigureType)
        callback.register_object_type(FigureType())
