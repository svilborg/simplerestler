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
       
        if len(kwargs) != 0:
            src = kwargs.get('src', "")
            text = kwargs.get('text', "")
        elif len(arg) != 0:
            src  = args[0]
            text = args[1]

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

        text = ""
        char = "*"
        underline = ""

        if len(kwargs) != 0:
            text = kwargs.get('text', "")
            char = kwargs.get('type', "*")
        elif len(args) !=0:
            text = args[0]


        length = len(text)

        if len(text) > 0:
            underline = str(char) * length

        self.params = [text, underline]

        self.parent.add('\n')
        self.parent.add(text)
        self.parent.add('\n')
        self.parent.add(underline)
        self.parent.add('\n')

        return self

    def __str__( self ):

        return Element.__str__(self)

class LinkElement(Element):
    """
    Link Element

    `Python <http://www.python.org/>`_ 
"""

    def __init__( self, parent=None): 
        Element.__init__(self, "link", parent)
    
    def __call__( self, *args, **kwargs ):

        text = ""
        href = ""

        if len(kwargs) != 0:
            href = kwargs.get('href', "")
            text = kwargs.get('text', "")
        elif len(arg) != 0:
            href = args[0]
            text = args[1]

        self.params = [text, underline]

        line = "`%s` %s_" % ( text, href )
        self.parent.add(line)

        return self

    def __str__( self ):

        return Element.__str__(self)

class DirectiveElement(Element):
    """
    Directive Element

.. note:: Note

   This is content

"""

    def __init__( self, parent=None): 
        Element.__init__(self, "directive", parent)
    
    def __call__( self, *args, **kwargs ):

        type = ""
        title = ""
        text = ""

        if len(kwargs) != 0:
            type  = kwargs.get('type', "")
            title = kwargs.get('title', "")
            text  = kwargs.get('text', "")
        elif len(arg) != 0:
            type  = args[0]
            title = args[1]
            text  = args[2]

        self.params = [type, title, text]

        line = ".. %s:: %s" % ( text, title )
        self.parent.add(line)
        self.parent.add('\n')
        self.parent.add('    ' + text)
        self.parent.add('\n')

        return self

    def __str__( self ):

        return Element.__str__(self)

class TableElement(Element):
    """
    Directive Element

.. note:: Note

   This is content

"""

    def __init__( self, parent=None): 
        Element.__init__(self, "table", parent)
    
    def __call__( self, *args, **kwargs ):

        data = None

        if len(arg) != 0:
            data  = args[0]

        self.params = args

        table = self.make_table(data)

        self.parent.add('\n')
        self.parent.add(table)
        self.parent.add('\n')

        return self
    
    def make_table(grid):
        max_cols = [max(out) for out in map(list, zip(*[[len(item) for item in row] for row in grid]))]
        rst = self.table_div(max_cols, 1)

        for i, row in enumerate(grid):
            header_flag = False
            if i == 0 or i == len(grid)-1: header_flag = True
            rst += normalize_row(row,max_cols)
            rst += self.table_div(max_cols, header_flag )
        return rst

    def table_div(max_cols, header_flag=1):
        out = ""
        if header_flag == 1:
            style = "="
        else:
            style = "-"

        for max_col in max_cols:
            out += max_col * style + " "

        out += "\n"
        return out

    def normalize_row(row, max_cols):
        r = ""
        for i, max_col in enumerate(max_cols):
            r += row[i] + (max_col  - len(row[i]) + 1) * " "

        return r + "\n"

    def __str__( self ):

        return Element.__str__(self)
