<<<<<<< before updating
class TestSearchpathPlugin:
    def test_discover_self(self):
        import hydra_plugins.lerna.searchpath
=======
from nbprint_example_plugin import *
>>>>>>> after updating

        assert "nbprint-example-plugin" in hydra_plugins.lerna.searchpath._searchpaths_pkg
