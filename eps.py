#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Définition de eps
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import *

print "eps en float128 : ", finfo(np.float128).eps