from core import debug
from config import settings
from catalogapp.engine.engine import CatalogEngine

debug = debug.Debug(settings.OUTPUT)
engine = CatalogEngine(debug.trace)