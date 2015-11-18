#!/usr/bin/python

with open('../voa-word-book.txt') as wordBookFile:
    with open('wordlist.html', 'w') as indexFile:
        indexFile.write('<!DOCTYPE html>\n')
        indexFile.write('<html lang="en" dir="ltr" class="client-nojs">\n')
        indexFile.write('  <head>\n')
        indexFile.write('    <title>wordlist - special english - auke.klazema.net</title>\n')
        indexFile.write('    <meta name="viewport" content="width=device-width">\n')
        indexFile.write('    <link href="/style.css" rel="stylesheet" type="text/css">\n')
        indexFile.write('  </head>\n')
        indexFile.write('  <body>\n')
        indexFile.write('    <h1>wordlist</h1>\n\n')
        indexFile.write('      <ul>\n')

        for wordLine in wordBookFile:
            parts = wordLine.split(' - ')
            indexFile.write('        <li><a href="/specialenglish/words/' + parts[0] + '.html"/>' + parts[0] + '</a></li>\n')

        indexFile.write('      </u>\n\n')
        indexFile.write('    <p><a href="https://creativecommons.org/publicdomain/zero/1.0/">\n')
        indexFile.write('       <img src="https://i.creativecommons.org/p/zero/1.0/80x15.png"\n')
        indexFile.write('            alt="CC0" /></a><br />\n')
        indexFile.write('       to the extent possible under law, the person named\n')
        indexFile.write('       (<a href="https://auke.klazema.net/">auke l. klazema</a>)\n')
        indexFile.write('       has waived all copyright and related or neighboring rights to\n')
        indexFile.write('       this work. this work is published from the country named\n')
        indexFile.write('       nederland.</p>\n\n')
        indexFile.write('    <hr />\n')
        indexFile.write('    <p><a href="/">home</a> - <a href="/specialenglish/">special english</a> - wordlist</p>\n')
        indexFile.write('  </body>\n')
        indexFile.write('</html>\n')
