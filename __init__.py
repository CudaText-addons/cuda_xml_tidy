import re
import xml.dom.minidom
from cudatext import *

def do_format(source, indent_text, eol):
    try:
        parsedCheck = xml.dom.minidom.parseString(source)            
    except xml.parsers.expat.ExpatError as e:
        msg_box(str(e), MB_OK+MB_ICONERROR)
        return
        
    re_compile = re.compile("<.*?>")
    result = re_compile.findall(source)
    source = ''.join(result)
    
    parsed = parsedCheck    
    lines = parsed.toprettyxml(indent=indent_text).split('\n')
    source = eol.join([line for line in lines if line.strip()])
    return source
    
class Command:
    def run(self):
        text = ed.get_text_all()
        eol = '\n'
        indent = ' '*ed.get_prop(PROP_TAB_SIZE)
        
        text = do_format(text, indent, eol)
        if text:
            ed.set_text_all(text)
            msg_status('XML formatted')
