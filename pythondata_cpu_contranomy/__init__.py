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
data_git_hash = "6fe4d89ce1e39e4a507cf9deef74b5e0e00197a1"
data_git_describe = "v1.0"
data_git_msg = """\
commit 6fe4d89ce1e39e4a507cf9deef74b5e0e00197a1
Author: Christiaan Baaij <christiaan.baaij@gmail.com>
Date:   Thu Sep 10 23:31:13 2020 +0200

    Correctly handle traps/interrupts and LSU

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
