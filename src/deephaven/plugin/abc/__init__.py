import abc

# server provider
class ExportABC(abc.ABC):
    @property
    @abc.abstractmethod
    def item(self):
        pass

    @property
    @abc.abstractmethod
    def export_id(self) -> bytes:
        pass

# server provided
class ExporterABC(abc.ABC):
    @abc.abstractmethod
    def new_server_side_export(self, object) -> ExportABC:
        pass

# user extends this
class ObjectTypeABC(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def is_type(self, object) -> bool:
        pass

    @abc.abstractmethod
    def to_bytes(self, exporter: ExporterABC, object) -> bytes:
        pass

# server provided
class CallbackABC(abc.ABC):
    @abc.abstractmethod
    def register_object_type(self, object_type: ObjectTypeABC) -> None:
        pass

# user extends this
class PluginABC(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def register_into(cls, callback: CallbackABC) -> None:
        pass

class PluginBase(PluginABC):
    @classmethod
    def register_into(cls, callback: CallbackABC) -> None:
        cls.register_object_types_into(callback)

    @classmethod
    @abc.abstractmethod
    def register_object_types_into(cls, callback: CallbackABC) -> None:
        pass
