import sys
from cStringIO import StringIO
import traceback


def eval_code(code):
    try:
        compiled = compile(code, '<string>', 'single')
    except:
        pass
    try:
        old_stdout = sys.stdout
        sys.stdout = strstdout = StringIO()
        try:
            exec compiled
        finally:
            sys.stdout = old_stdout
            return strstdout.getvalue().strip('\n')
    except:
        #return traceback.format_exc()
        pass


def lambda_handler(event, context):
    code = event.get('code').replace('\r\n', '\n')
    code += '\n\n'
    rrr = ['chr', 'app', '__', 'flask', 'import', 'wsgi', 'rrr', 'sys', 'getattr', 'bytearray', 'open', 'nepo', 'read', 'dear',
    'var', 'rav', 'globals', 'locals', 'truncate', 'remove', 'eval', 'exec', '.py', 'pypie', 'exit', 'request', 'os ', ' os.']
    if not any(word in code for word in rrr):
        return eval_code(code)
    else:
        pass
