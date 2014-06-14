""" Elements """

class Element:
    """Element."""

    def __init__( self, name, parent=None):
        self.name  = name
        self.params  = [] 
        self.parent = parent
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        return self

    def __str__( self ):
        
        return self.name + "[" + ", ".join(self.params) + "]"


class UlElement(Element):
    """Ul Element."""

    def __init__( self, parent=None): 
        Element.__init__(self, "ul", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        self.parent.add('\n')

        for arg in args:

            line = "* " + arg
            self.parent.add(line)
            self.parent.add('\n')
        
        self.parent.add('\n')

        return self

    def __str__( self ): 

        return Element.__str__(self)

class OlElement(Element):
    """Ol Element."""

    def __init__( self, parent=None): 
        Element.__init__(self, "ol", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        self.parent.add('\n')

        i = 0
        for arg in args:
            i +=1 
            line = str(i) + ". " + arg
            self.parent.add(line)
            self.parent.add('\n')

        self.parent.add('\n')

        return self

    def __str__( self ):

        return Element.__str__(self)
 