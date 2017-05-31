import string

t = string.Template('$var')

d = { 'with_underscore': 'replaced',
        'notunderscored': 'not replaced',
    }

class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<name>[_a-z][_a-z0-9]*)\}\}|
    {(?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

t = MyTemplate('''{{{{ {{var}}''')
print 'MATCHES:', t.pattern.findall(t.template)
print 'SUBSTITUTE:', t.safe_substitute(var='replacement')


