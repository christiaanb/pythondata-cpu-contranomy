import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/christiaanb/contranomy"

# Module version
version_str = "1.0.0"
version_tuple = (1, 0, 0)
try:
    from packaging.version import Version as V
    pversion = V("1.0.0")
except ImportError:
    pass

# Data version info
data_version_str = "1.0"
data_version_tuple = (1, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0")
except ImportError:
    pass
data_git_hash = "2bb61cb3ce497cb4090893f0e2b5c1fea46a22f3"
data_git_describe = "v1.0"
data_git_msg = """\
commit 2bb61cb3ce497cb4090893f0e2b5c1fea46a22f3
Author: Christiaan Baaij <christiaan.baaij@gmail.com>
Date:   Sat Sep 12 15:50:31 2020 +0200

    LSUnit also finished on misaligned address

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_contranomy."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_contranomy".format(f))
    return fn
