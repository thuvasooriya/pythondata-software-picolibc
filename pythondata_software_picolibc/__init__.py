import os.path

__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.8.10.post0"
version_tuple = (1, 8, 10, 0)
try:
    from packaging.version import Version as V

    pversion = V("1.8.10.post0")
except ImportError:
    pass

# Data version info
data_version_str = "1.8.10.post0"
data_version_tuple = (1, 8, 10, 0)
try:
    from packaging.version import Version as V

    pdata_version = V("1.8.10.post0")
except ImportError:
    pass
data_git_hash = "51a8b32857e75345c37652a80b5cda98b28d69e5"
data_git_describe = "1.7.9-39-gf165dc22f"
data_git_msg = """\
commit 51a8b32857e75345c37652a80b5cda98b28d69e5
Author: Keith Packard <keithp@keithp.com>
Date: Mon Apr 14 09:50:00 2025 - 0700

    Version 1.8.10

    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post143"
tool_version_tuple = (0, 0, 143)
try:
    from packaging.version import Version as V

    ptool_version = V("0.0.post143")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc")
    return fn
