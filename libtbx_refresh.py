from __future__ import absolute_import, division, print_function

import i19.util.version as version
import libtbx.pkg_utils

print(version.i19_version())
libtbx.pkg_utils.require('mock', '>=2.0')
libtbx.pkg_utils.require('pytest', '>=3.1')
