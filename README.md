Simple reStler
==============

Simple reStructuredText Builder - A small python library for building reStructuredText 

Example :

```python

    import simplerestler
    
    
    doc = simplerestler.Document()

    doc.title("Title")
    doc.title("Subtitle", "=")
    doc.ul("One", "Two", "Three")
    doc.ol("One", "Two", "Three")

    doc.hr()

    doc.p("<b>Lorem ipsum</b> dolor sit amet, consectetur adipisicing <em>elit</em>, " + 
        "sed do eiusmod tempor " +
        "incididunt ut labore et dolore magna aliqua.<br/> Ut enim ad minim veniam ..")

    doc.pre("Same as      here ")

    doc.flist(title="Book Z", author="JJ Brown")

    doc.image(src="https://avatars2.githubusercontent.com/u/2757518", height="40pt", alt="Icon")

    
    doc.link(href="http://google.com", text="G00g1e")

    doc.directive(type="math", text="10*x + 12*y = z")


    doc.directive(type="sidebar", title="News", subtitle="Sport", text="Gooool!")

    if printable :
       print doc
    else :
       doc.save("/tmp/example.html")
    
    
```
