""" This plugin will write the md files for each publication found in diag.bib
 
"""
import os
import time

from bibtex import bibtexlib
from bibtex import bibtexformatter
from pelican import signals

def register():
    signals.initialized.connect(generate_md_bibitem)
    
def generate_md_bibitem(sender):
    out_dir = r'../../content/pages/publications'
    bib_file = 'plugins/bibtex/diag.bib'
    print('Bibtex plugin loaded')
    start_time = time.clock()
    index, global_index, string_rules = bibtexlib.read_bibtex_file(bib_file)
    html_format = bibtexformatter.HTML_Formatter(string_rules)
    time_diagbib = time.clock() - start_time
    start_time = time.clock()

    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    list_bibs_error = []

    for bibitem in global_index.keys():
        md_format = ''

        if 'author' not in global_index[bibitem].entry or 'title' not in global_index[bibitem].entry:
            continue
        md_format += 'title: ' + global_index[bibitem].entry['title'] + '\n'
        md_format += '\n## ' + global_index[bibitem].entry['author'] + '\n'

        if 'journal' in global_index[bibitem].entry:
            md_format += global_index[bibitem].entry['journal'] + '\n\n'
        elif 'booktitle' in global_index[bibitem].entry:
            md_format += global_index[bibitem].entry['booktitle'] + '\n\n'

        if 'doi' in global_index[bibitem].entry:
            url_doi = '\"https://doi.org/' + global_index[bibitem].entry['doi'] + '\"'
            md_format += '<a href=' + url_doi + '>DOI</a>\n'

        if 'abstract' in global_index[bibitem].entry:
            md_format += '\n## Abstract\n'
            md_format += global_index[bibitem].entry['abstract'] + '\n\n'

        if 'file' in global_index[bibitem].entry:
            md_format += 'A <b>pdf file</b> of this publication is available for personal use.'
            md_format += 'Enter your e-mail address in the box below and press the button. '
            md_format += 'You will receive an e-mail message with a link to the pdf file.\n'

            md_format += '<form action=\"sender.php\">'
            md_format += '  <input type=\"text\" name=\"email\">'
            md_format += '  <input type=\"submit\" value=\"Send ' + global_index[bibitem].entry[
                'file'] + ' by e-mail\">'
            md_format += '</form>'

        md_format = md_format.replace('{', '').replace('}', '')
        md_format = md_format.replace('\\', '')  # To remove the backslash mainly from abstract '\%'
        out_path = os.path.join(out_dir, bibitem + '.md')
        file = open(out_path, 'w')

        try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
            file.write(md_format)
            file.close()
            print(bibitem + ' done')
        except UnicodeEncodeError:
            list_bibs_error.append(bibitem)

    print('\nTime to process diag.bib ', time_diagbib)
    print('Time to create ' + str(len(global_index)) + ' MD files ', time.clock() - start_time)
    print('List of bibkeys returning UnicodeEncodeError')

    for bib in list_bibs_error:
        print(bib)


