import abc

# server provided
class ExporterABC(abc.ABC):
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
    def register_object_type(object_type: ObjectTypeABC) -> None:
        pass

# user extends this
class PluginABC(abc.ABC):    
    @abc.abstractmethod
    def register_into(callback: CallbackABC) -> None:
        pass
