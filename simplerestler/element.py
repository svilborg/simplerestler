""" Elements """
import errors
from utils import Utils

NL = "\n"

class Element:
    """Element."""

    def __init__( self, name, parent=None):
        self.name    = name
        self.params  = [] 
        self.parent  = parent
        self.content = []
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        return self

    def add (self, line):
        self.content.append(line)

        if self.parent is not None:
            self.parent.add(line) 


        return line

    def __str__( self ):
        return ''.join(self.content)


class UlElement(Element):
    """Ul Element."""

    def __init__( self, parent=None): 
        Element.__init__(self, "ul", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        self.add(NL)

        for arg in args:

            line = "* " + Utils.html_rest(arg)
            self.add(line)
            self.add(NL)
        
        self.add(NL)

        return self

    def __str__( self ): 

        return Element.__str__(self)

class OlElement(Element):
    """Ol Element."""

    def __init__( self, parent=None): 
        Element.__init__(self, "ol", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        self.add(NL)

        i = 0
        for arg in args:
            i +=1 
            line = str(i) + ". " + Utils.html_rest(arg)
            self.add(line)
            self.add(NL)

        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)

class FlistElement(Element):
    """Field List Element.

        :Date: 2001-08-16
        :Version: 1
        :Authors: - Me
                  - Myself
                  - I
        :Indentation: Since the field marker may be quite long, the second
           and subsequent lines of the field body do not have to line up

    """

    def __init__( self, parent=None): 
        Element.__init__(self, "flist", parent)
    
    def __call__( self, *args, **kwargs ):

        self.params = args

        if len(kwargs) == 0:
            raise errors.DocumentError("No list fields.")

        self.add(NL)

        if len(kwargs) > 1:
            for field in sorted(kwargs):
                value = Utils.html_rest(kwargs[field])

                self.add(':'+ field +': ' + value)
                self.add(NL)

        self.add(NL)

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

        self.add(NL)
        self.add('-----------')
        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)

class PElement(Element):
    """Paragraph """

    def __init__( self, parent=None): 
        Element.__init__(self, "p", parent)
    
    def __call__( self, *args, **kwargs ):
        
        text = ""

        if len(kwargs) != 0:
            text = kwargs.get('text', "")
        elif len(args) != 0:
            text = args[0]

        text = Utils.html_rest(text)
        text = Utils.br_rest(text)

        self.add(NL)
        self.add(text)
        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)

class PreElement(Element):
    """Pre - Literal Block """

    def __init__( self, parent=None): 
        Element.__init__(self, "pre", parent)
    
    def __call__( self, *args, **kwargs ):
        
        text = ""

        if len(kwargs) != 0:
            text = kwargs.get('text', "")
        elif len(args) != 0:
            text = args[0]

        self.add(NL)
        self.add('::')
        self.add(NL)
        self.add(NL)
        self.add(' ')
        self.add(text)
        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)

class LineblockElement(Element):
    """Line Block 
        | These lines are
        | broken exactly like in
        | the source file.
    """

    def __init__( self, parent=None): 
        Element.__init__(self, "pre", parent)
    
    def __call__( self, *args, **kwargs ):
        
        block = ""

        if len(args) != 0:
            self.add(NL)
    
            for arg in args:
                block += "| " + arg + NL

            self.add(block)

        return self

    def __str__( self ):

        return Element.__str__(self)


class CommentElement(Element):
    """Comment

        .. This text will not be shown
           Second line

     """

    def __init__( self, parent=None): 
        Element.__init__(self, "comment", parent)
    
    def __call__( self, *args, **kwargs ):

        if len(kwargs) != 0:
            text = kwargs.get('text', "")
        elif len(args) > 0:
            text = args[0]

        if text is None:
            raise errors.InvalidElementError("text")

        self.add(NL)
        self.add(NL)
        self.add('.. ' + text)
        self.add(NL)
        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)
     
class ImageElement(Element):
    """Image Element. 

        .. image::images/ball1.tiff 
           :height: 100px
           :width: 200 px
           :scale: 50 %
           :alt: alternate text
           :align: right
    """

    def __init__( self, parent=None): 
        Element.__init__(self, "image", parent)
    
    def __call__( self, *args, **kwargs ):
       
        src = None
        options = {}

        if len(kwargs) != 0:
            src = kwargs.get('src', None)
        elif len(args) > 0:
            src  = args[0]

        if src is None:
            raise errors.InvalidElementError("src")

        self.add(NL)
        self.add('.. image:: ' + src)

        if len(kwargs) > 1:
            for option in sorted(kwargs):
                if option != "src":
                    self.add(NL)
                    self.add('   :'+option+': ' + kwargs[option])
                pass

        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)
 
class TitleElement(Element):
    """
    Titles 
        # with overline, for parts
        * with overline, for chapters
        =, for sections
        -, for subsections
        ^, for subsubsections
        ", for paragraphs
    """

    def __init__( self, parent = None): 

        Element.__init__(self, "title", parent)
    
    def __call__( self, *args, **kwargs ):

        text = ""
        char = "*"
        underline = ""

        if len(kwargs) != 0:
            text = kwargs.get('text', "")
            char = kwargs.get('type', "*")
        elif len(args) > 0:
            text = args[0]
            if len(args) > 1:
                char =  args[1]

        underline = str(char) * len(text)

        self.params = [text, underline]

        self.add(NL)
        self.add(text)
        self.add(NL)
        self.add(underline)
        self.add(NL)

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
        elif len(args) != 0:
            href = args[0]
            text = args[1]

        self.params = [text, href]

        self.add(NL)
        self.add("`%s <%s>`_" % ( text, href ))
        self.add(NL)

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
        elif len(args) > 0:
            type  = args[0]
            
            if len(args) > 1:
                title = args[1]

            if len(args) > 2:
                text  = args[2]

        self.params = [type, title, text]


        self.add(NL)
        self.add(".. %s:: %s" % ( type, title))
        self.add(NL)

        if len(kwargs) > 1:
            for option in sorted(kwargs):
                if option != "type" and option != "text" and option != "title":
                    self.add('   :'+option+': ' + kwargs[option])
                    self.add(NL)
                pass

        self.add(NL)
        self.add('    ' + text)
        self.add(NL)

        return self

    def __str__( self ):

        return Element.__str__(self)

class TableElement(Element):
    """
    Table Element


    """

    def __init__( self, parent=None): 
        Element.__init__(self, "table", parent)
    
    def __call__( self, *args, **kwargs ):

        data = None

        if len(args) > 0:
            data  = args[0]
            
            if len(data) > 0:
                self.params = args

                table = self.make_table(data)

                self.add(NL)
                self.add(table)
                self.add(NL)

        return self
    
    def make_table(self, grid):
        max_cols = [max(out) for out in map(list, zip(*[[len(item) for item in row] for row in grid]))]
        rst = self.table_div(max_cols, 1)

        for i, row in enumerate(grid):
            header_flag = False
            if i == 0 or i == len(grid)-1: header_flag = True
            rst += self.normalize_row(row,max_cols)
            rst += self.table_div(max_cols, header_flag )
        return rst

    def table_div(self, max_cols, header_flag=1):
        out = ""
        if header_flag == 1:
            style = "="
        else:
            style = "-"

        for max_col in max_cols:
            out += max_col * style + " "

        out += "\n"
        return out

    def normalize_row(self, row, max_cols):
        r = ""
        for i, max_col in enumerate(max_cols):
            r += row[i] + (max_col  - len(row[i]) + 1) * " "

        return r + "\n"

    def __str__( self ):

        return Element.__str__(self)
