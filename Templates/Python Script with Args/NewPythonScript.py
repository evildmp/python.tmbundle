#!/usr/bin/env python
#
#  ${TM_NEW_FILE_BASENAME}
#
#  Created by ${TM_USERNAME} on ${TM_DATE}.
#  Copyright (c) ${TM_YEAR} ${TM_ORGANIZATION_NAME}. All rights reserved.
#
# Replace this comment block as a module docstring, the module docstring
# is used as default usage message i.e. raise Usage(__doc__)
# example:
#
# file([file_type]) -> return_values
#
# Returns a ....

import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hov:", ["help", "output="])
        except getopt.error, msg:
             raise Usage(msg)

        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(__doc__)
            if option in ("-o", "--output"):
                output = value
    
    except Usage, err:
        print >>sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >>sys.stderr, "\t for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())