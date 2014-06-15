""" Exceptions """

class DocumentError( Exception ):
    """All module's exceptions subclass this class."""
    def __str__( self ):
        return self.message

class InvalidMethodError( DocumentError ):
    def __init__( self, method):
        self.message = "Invalid method - '%s' ." % ( method )

class InvalidElementError( DocumentError ):
    def __init__( self, name):
        self.message = "Invalid Element - '%s' ." % ( name )

class ArgumentError( DocumentError ):
    def __init__( self, el ):
        self.message = "Invalid argument - '%s' ." % el