import os

from hydra.core.config_search_path import ConfigSearchPath
from hydra.plugins.search_path_plugin import SearchPathPlugin

class BinSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        """Fixes bin installation issues"""
        search_path.append(
                provider="simple_ml-plugin", path="file://{}".format(os.getcwd())
            )