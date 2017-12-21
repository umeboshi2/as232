import os
import subprocess
import contextlib
import hashlib

from hornstone.base import chunks, get_sha256sum, get_sha256sum_string
from hornstone.base import trailing_slash, remove_trailing_slash
from hornstone.base import parse_config_lines



@contextlib.contextmanager
def working_directory(directory):
    oldwd = os.getcwd()
    os.chdir(directory)
    try:
        yield
    finally:
        os.chdir(oldwd)
        
def WorkingDirectory(directory):
    import warnings
    msg = "WorkingDirectory is deprecated, use working_directory() instead"
    warnings.warn(msg)
    return working_directory(directory)


# FIXME, this is not useful
def run_command(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    if proc.returncode:
        msg = "%s returned %d" % (' '.join(cmd), proc.returncode)
        raise RuntimeError(msg)
    return proc

def get_command_output(cmd):
    return subprocess.check_output(cmd)

