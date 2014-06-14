
""" Document Class """

import element
import errors


class Document:
    """Rest Document."""

    def __init__( self ):
        
        self.content = [ ]
        self.class_= self
        self.delimiter = '\n'
        methods = [ 
        "ul", # Unorderd list - # XX
        "ol", # Orderd list - 1. XX
        "link", # Link
        "image", # Image
        "title", # Title
        "hr", # Hr
        ]

    def add(self, line):
        self.content.append(line)

    def __getattr__( self, method ):
        if method == "ul" :
            return element.UlElement( parent=self )
        elif method == "ol":
            return element.OlElement( parent=self ) 
        elif method == "image":
            return element.ImageElement( parent=self )
        elif method == "title":
            return element.TitleElement( parent=self )
        elif method == "hr":
            return element.HrElement( parent=self )
        else:
            raise errors.InvalidMethodError(method)

    def __str__( self ):
        
        return ''.join(self.content)

    def __call__( self, *args, **kwargs ):
        """Return the document as a string.
        """

        return self.__str__( )