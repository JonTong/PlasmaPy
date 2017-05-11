"""
PlasmaPy is a community-developed and community-driven core Python
package for plasma physics.
"""

import sys
import warnings

if sys.version_info[:2] < (3, 6):
    warnings.warn("PlasmaPy does not support Python 3.5 and below")

from .classes import Plasma
from . import constants
from . import analytic


