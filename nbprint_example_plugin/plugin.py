from hydra.core.config_search_path import ConfigSearchPath
from hydra.core.config_store import ConfigStore
from hydra.plugins.search_path_plugin import SearchPathPlugin


class NBPrintExampleSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        inst = ConfigStore.instance()
        inst.store(name="nbprint-example-plugin", node=None, group="nbprint_example_plugin", provider="nbprint-example-plugin")
        search_path.append(provider="nbprint-example-plugin", path="pkg://nbprint_example_plugin/config")
