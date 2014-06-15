""" Utils """
class Utils(object):
    """Utils - Common functions"""
    
    @staticmethod
    def html_escape(text):
        """Produce entities within text."""
        tag_names = {
        "em": "*",
        
        "b": "**",
        "string": "**",
        }

        for tag, new in tag_names.iteritems():
            text = Utils.ireplace('<' + tag + '>', new, text)
            text = Utils.ireplace('</' + tag + '>', new, text)
        
        return text

    @staticmethod
    def ireplace(old, new, text):
        idx = 0
        while idx < len(text):
            index_l = text.lower().find(old.lower(), idx)
            if index_l == -1:
                return text
            text = text[:index_l] + new + text[index_l + len(old):]
            idx = index_l + len(old)
        return text