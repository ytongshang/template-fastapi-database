import os
import sys

from clio import hack_json, Workspace

from clio.utils.log import console_handler, default_logger, file_handler
from dotenv import load_dotenv

from example.config.config import get_log_dir

_current_dir = os.path.dirname(os.path.abspath(__file__))


def _load_env():
    _env_file_path = os.path.join(_current_dir, "../.env")
    load_dotenv(dotenv_path=_env_file_path, verbose=True)


def _init_workspace():
    workspace = os.getenv(
        "WORKSPACE_ROOT", os.path.join(_current_dir, "../dist/workspace")
    )
    Workspace.set_default_workspace(
        Workspace.make_workspace(workspace, restrict_to_workspace=True)
    )


def _init_log():
    logger = default_logger
    console_handler(logger)
    file_handler(logger, get_log_dir())


_load_env()
_init_workspace()
_init_log()
hack_json()
