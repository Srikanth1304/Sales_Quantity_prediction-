
# -*- coding: utf-8 -*-
import re
import sys

from astropy.samp.hub_script import hub_script

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(hub_script())
