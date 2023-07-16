import importlib.util
import sys


class Config:
    """Load given config file and parse it"""

    def __init__(self, config_path: str):
        """Init class

        Args:
            config_path (str): path to config to load into Python code
        """
        spec = importlib.util.spec_from_file_location("loader.config", config_path)
        config_loaded = importlib.util.module_from_spec(spec)
        sys.modules["loader.config"] = config_loaded
        spec.loader.exec_module(config_loaded)
        self.spreadsheet_id = config_loaded.SPREADSHEET_ID
        self.spreadsheet_tab = config_loaded.SPREADSHEET_TAB
        self.subj = config_loaded.SUBJ
        self.creds_path = config_loaded.CREDS_PATH
        self.template = config_loaded.TEMPLATE
