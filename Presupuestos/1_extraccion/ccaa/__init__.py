"""Sub-pipelines de extracción y transformación por CCAA."""
from ._common.dispatcher import dispatch, get_extractor, get_transformer

__all__ = ["dispatch", "get_extractor", "get_transformer"]
