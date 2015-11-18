#!/usr/bin/python

with open('../voa-word-book.txt') as wordBookFile:
    for wordLine in wordBookFile:
        parts = wordLine.split(' - ')
        with open('../pages/' + parts[0] + '.html', 'w') as wordFile:
            wordFile.write('<!DOCTYPE html>\n')
            wordFile.write('<html lang="en" dir="ltr" class="client-nojs">\n')
            wordFile.write('  <head>\n')
            wordFile.write('    <title>' + parts[0] + ' - special english - auke.klazema.net</title>\n')
            wordFile.write('    <meta name="viewport" content="width=device-width">\n')
            wordFile.write('    <link href="/style.css" rel="stylesheet" type="text/css">\n')
            wordFile.write('  </head>\n')
            wordFile.write('  <body>\n')
            wordFile.write('    <h1>' + parts[0] + '</h1>\n\n')
            wordFile.write('    <p>' + parts[1].strip() + '</p>\n\n')
            wordFile.write('    <p><a href="https://creativecommons.org/publicdomain/zero/1.0/">\n')
            wordFile.write('       <img src="https://i.creativecommons.org/p/zero/1.0/80x15.png"\n')
            wordFile.write('            alt="CC0" /></a><br />\n')
            wordFile.write('       to the extent possible under law, the person named\n')
            wordFile.write('       (<a href="https://auke.klazema.net/">auke l. klazema</a>)\n')
            wordFile.write('       has waived all copyright and related or neighboring rights to\n')
            wordFile.write('       this work. this work is published from the country named\n')
            wordFile.write('       nederland.</p>\n\n')
            wordFile.write('    <hr />\n')
            wordFile.write('    <p><a href="/">home</a> - <a href="/specialenglish/">special english</a> - <a href="/specialenglish/wordlist.html">wordlist</a> - ' + parts[0] + '</p>\n')
            wordFile.write('  </body>\n')
            wordFile.write('</html>\n')
