from io import BytesIO
from matplotlib.figure import Figure

from deephaven.plugin.abc import ExporterABC, ObjectTypeABC

NAME = "matplotlib.figure.Figure"

class FigureType(ObjectTypeABC):
    @property
    def name(self) -> str:
        return NAME

    def is_type(self, object) -> bool:
        return isinstance(object, Figure)

    def to_bytes(self, exporter: ExporterABC, figure: Figure) -> bytes:
        buf = BytesIO()
        figure.savefig(buf, format='PNG')
        return buf.getvalue()
