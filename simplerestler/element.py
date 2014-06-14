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
 
class Ol2Element(Element):
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

class HrElement(Element):
    """Hr or Transaition Element . A transition marker is a horizontal line
of 4 or more repeated punctuation ----- """

    def __init__( self, parent=None): 
        Element.__init__(self, "hr", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = "----"

        self.parent.add('\n')
        self.parent.add('-----------')
        self.parent.add('\n')

        return self

    def __str__( self ):

        return Element.__str__(self)

class ImageElement(Element):
    """Image Element. 
        .. image:: images/ball1.gif 
    """

    def __init__( self, parent=None): 
        Element.__init__(self, "image", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = "image"

        src = kwargs.get('src', None)

        self.parent.add('image:: ' + src)

        return self

    def __str__( self ):

        return Element.__str__(self)
 
class TitleElement(Element):
    """
    Titles 

    Chepter One
    ***********

    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs
"""

    def __init__( self, parent=None): 
        Element.__init__(self, "title", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = "----"

        text = ""
        char = "*"
        underline = ""

        if len(args) == 0:
            text = kwargs.get('text', "")
            char = kwargs.get('type', "*")
        else:
            text = args[0]


        length = len(text)

        if len(text) > 0:
            underline = str(char) * length

        self.params = [text, underline]

        self.parent.add('\n')
        self.parent.add(text)
        self.parent.add(underline)
        self.parent.add('\n')

        return self

    def __str__( self ):

        return Element.__str__(self)