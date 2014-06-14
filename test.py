

import simplerestler
if __name__ == '__main__':
    d = simplerestler.Document()
    ul = d.ul("One", "Two", "Three")
    ol = d.ol("Uno", "Dos", "Tres")
    
    print d

    print "----------"
    print ul
    print "----------"
    print ol

    print simplerestler.__doc__
    # import sys
    # sys.stdout.write( __doc__ )