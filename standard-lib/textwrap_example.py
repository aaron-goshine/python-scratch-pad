sample_text = '''
The text warp module can be used to format text for out put in
situations where pretty-printing is desired. It offers programmatic
functionality similar to the paragraph wrapping or filling features
found in many text editors.
'''

import textwarp

print 'No dedent:\n'
print textwarp.fill(sample_text, width = 50)

