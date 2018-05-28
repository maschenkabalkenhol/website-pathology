"""
This plugin writes the md files for each publication found in bib_file (diag.bib by default)
It writes the output in 'out_dir'

@author Gabriel (ghumpire)
"""
import os
import glob
import json
import time
import hashlib
import _pickle as pickle

from bibtex import bibtexlib
from bibtex import bibtexformatter
# from pelican import signals
# from pelican.readers import BaseReader
#

def get_md5_hex(bibitem):
    # PYTHONHASHSEED should be set to zero to prevent random comparisons
    bib_md5 = hashlib.md5()
    pdata = pickle.dumps(bibitem)
    bib_md5.update(pdata)
    return bib_md5.hexdigest()


def get_md5s(global_index):
    dict_md5 = {}
    for bibkey in sorted(global_index.keys()):
        bibitem = global_index[bibkey].entry
        data_md5 = get_md5_hex(bibitem)
        dict_md5[bibkey] = data_md5

    return dict_md5


def save_dict2json(json_path, dict_md5):
    with open(json_path, 'w') as fp:
        json.dump(dict_md5, fp)


def load_json2dict(json_path):
    if os.path.exists(json_path):
        json_file = open(json_path)
        json_data = json.load(json_file)
    else:
        json_data = None

    return json_data

    
def get_publications_by_author(global_index, list_researchers):
    from collections import defaultdict
    author_index = defaultdict(set)
    filtered_publications = []
    for bib_key, bib_item in global_index.items():
        authors = bib_item.author

        for researcher_names in list_researchers:
            lastname = researcher_names[-1]
            for first, von, last, jr in authors:
                if last.lower() == lastname:
                    author_index[lastname].add(bib_key)
                    pvon = von.replace(' ', '').replace('.', '')
                    
                    if len(pvon) > 3:
                        author_index[von].add(bib_key)
                    if bib_key not in filtered_publications:
                        filtered_publications.append(bib_key)
    return author_index, filtered_publications
    
    
def generate_md_bibitem(writer=None):

    base_dir = os.path.dirname(os.path.abspath(__file__))

    out_dir = os.path.join(base_dir, '..', 'content/pages/publications')
    bib_file = os.path.join(base_dir, '..', 'content/diag.bib')
    json_path = os.path.join(base_dir, '..', 'output/md5s.json')

    print('Bibtex plugin loaded')
    print('Output dirs: {}'.format((out_dir, bib_file, json_path)))

    start_time = time.clock()
    index, global_index, string_rules = bibtexlib.read_bibtex_file(bib_file)
    # html_format = bibtexformatter.HTML_Formatter(string_rules)
    time_diagbib = time.clock() - start_time
    start_time = time.clock()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # os.chdir('../')
    list_researchers = get_list_people()
    print(list_researchers)
    author_index, filtered_publications = get_publications_by_author(global_index, list_researchers)
    
    write_single_publication_md(global_index, filtered_publications, out_dir, json_path)
    print('\nTime to process diag.bib ', time_diagbib)
    print('Time to create ' + str(len(global_index)) + ' MD files ', time.clock() - start_time)

    write_author_publications_md(global_index, author_index, list_researchers, out_dir, string_rules)


def write_author_publications_md(global_index, author_index, list_researchers, out_dir, string_rules):
    list_bibs_error = []
    html_format = bibtexformatter.HTML_Formatter(string_rules)
    
    for researcher_names in list_researchers:
        full_name = "-".join(researcher_names)
        title_md = " ".join(researcher_names).title()  # camel case
        md_format = 'title: Publications of ' + title_md + '\n\n'
        md_format += '<ul>\n'

        for author_name in author_index.keys():
            if researcher_names[-1] == author_name.lower():
                for bib_key in author_index[author_name]:
                    print(bib_key, 'Bibkey added')
                    bib_item = global_index[bib_key]
                    html_to_write = html_format.apply(bib_item)
                    md_format += '<li>'
                    md_format += html_to_write
                    md_format += '</li>\n'
              
                    md_format = md_format.replace('{', '').replace('}', '')

        md_format += '</ul>\n'
        out_path = os.path.join(out_dir, full_name + '.md')
        file = open(out_path, 'w')
        print(out_path, 'out_path author')
        
        try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
            file.write(md_format)
            file.close()
        except UnicodeEncodeError:
            list_bibs_error.append(full_name)

    print('List of bibkeys returning UnicodeEncodeError')

    for bib in list_bibs_error:
        print(bib)


def write_single_publication_md(global_index, filtered_publications, out_dir, json_path):
    print(filtered_publications, 'list pubs')

    # Loads json file with md5 value of bibitems of the previous version
    prev_md5s = load_json2dict(json_path)
    # Obtains the md5 values of the current bibitems in diag.bib
    md5s = get_md5s(global_index)
    
    list_bibs_error = []
    for bibitem in filtered_publications:  # global_index.keys():
        # Compares per bibitem whether are changes by comparing the md5s
        if prev_md5s is not None and bibitem in prev_md5s and bibitem in md5s and prev_md5s[bibitem] == md5s[bibitem]:
            print("skipping {}".format(bibitem))
            continue
        print(bibitem, "###")
        md_format = ''

        if 'author' not in global_index[bibitem].entry or 'title' not in global_index[bibitem].entry:
            # It skips bibitems with absence of authors or title
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

            md_format += '<form action=\"sender.php\">'  # TODO implement sender.php
            md_format += '  <input type=\"text\" name=\"email\">'
            md_format += '  <input type=\"submit\" value=\"Send ' + global_index[bibitem].entry[
              'file'] + ' by e-mail\">'
            md_format += '</form>'

        md_format = md_format.replace('{', '').replace('}', '')
        out_path = os.path.join(out_dir, bibitem + '.md')
        file = open(out_path, 'w')
        print(out_path,'####')
        try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
            file.write(md_format)
            file.close()
        except UnicodeEncodeError:
            list_bibs_error.append(bibitem)

    save_dict2json(json_path, md5s)
    print('List of bibkeys returning UnicodeEncodeError')

    for bib in list_bibs_error:
        print(bib)

#
# def register():
#     signals.finalized.connect(generate_md_bibitem)


def get_list_people():
    base_dir = os.getcwd()
    people_dir = '{}/content/pages/people'.format(base_dir)
    print(people_dir, '##')
    list_researchers = []
    
    for people_md_path in glob.glob(people_dir+'/*.md'):
        bname = os.path.basename(people_md_path).replace('.md', '')
        full_name = bname.split('-')
        list_researchers.append(full_name)
    
    return list_researchers


if __name__ == '__main__':
    # os.chdir('../')
    # get_list_people()
    generate_md_bibitem()

