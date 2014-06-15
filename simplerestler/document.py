
""" Document Class """

import element
import errors


class Document:
    """Rest Document."""

    METHODS = (
        "ul", # Unorderd list - # XX
        "ol", # Orderd list - 1. XX
        "link", # Link
        "image", # Image
        "title", # Title
        "para", # Paragraph
        "hr", # Hr
        "directive", #Block 
    )

    def __init__( self ):
        
        self.content = [ ]
        self.delimiter = '\n'

    def add(self, line):
        self.content.append(line)

    def __getattr__( self, method ):

        if method in self.METHODS:
            className = self.getClassName(method)

            if hasattr(element, className):

                instance = getattr(element, className)
                
                return instance(parent=self)
            else:
                raise errors.InvalidElementError(className)
        else:
            raise errors.InvalidMethodError(method)

    def getClassName (self, title):

        return title.capitalize() + "Element"


    def __str__( self ):
        return ''.join(self.content)

    def __call__( self, *args, **kwargs ):
        """Return the document as a string.
        """

        return self.__str__( )