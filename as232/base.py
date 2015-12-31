import os
import subprocess
import contextlib


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


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def get_sha256sum(fileobj):
    s = hashlib.new('sha256')
    block = fileobj.read(4096)
    while block:
        s.update(block)
        block = fileobj.read(4096)
    return s.hexdigest()

def get_sha256sum_string(string):
    s = hashlib.new('sha256')
    s.update(string)
    return s.hexdigest()

def trailing_slash(dirname):
    if not dirname.endswith('/'):
        return '%s/' % dirname
    return dirname

def remove_trailing_slash(pathname):
    while pathname.endswith('/'):
        pathname = pathname[:-1]
    return pathname

    

def parse_config_lines(filename):
    return [line.strip() for line in file(filename)
            if line.strip() and not line.strip().startswith('#')]


# FIXME, this is not useful
def run_command(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    if proc.returncode:
        msg = "%s returned %d" % (' '.join(cmd), proc.returncode)
        raise RuntimeError, msg
    return proc

def get_command_output(cmd):
    return subprocess.check_output(cmd)

