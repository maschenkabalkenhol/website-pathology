from string import Formatter

def authors_to_string(authors):
    '''
    authors: list of author tuples
    '''
    def parse_author(author):
        first, von, last, jr = author
        
        if len(first)>=2 and first[1]=='.':
            # first probably contains initials
            initials = first
        else:
            initials = '.'.join(x[0] for x in first.split(' ') if x)
            if len(initials):
                initials += '.'
            
        result = initials        
        if not von == '':
            if len(von)>=2 and von[1]=='.':
                # von probably contains some initials
                result += von
            else:
                result += ' ' + von
        result += ' ' +last
        if not jr == '':
            result += ' ' + jr
        return result
    
    names = [parse_author(a) for a in authors]
    if len(names) == 1:
        return names[0]
    else:
        return ', '.join(names[:-1]) + ' and ' + names[-1] 


class BaseFormatter:
    
    def __init__(self, string_rules):
        self.string_rules = string_rules

    def apply_format(self, output, bib_item, **kwargs):
        def get_val(k):
            if k in kwargs:
                return kwargs[k]
            
            if not k in bib_item.entry:
                return ''
            
            value = getattr(bib_item, k)
            
            if k in ('journal', 'booktitle') and value in self.string_rules:
                return self.string_rules[value].replace('_', ' ').strip()
            else:
                return value
            
        field_names = [field_name for _, field_name, _, _ in Formatter().parse(output)]
        
        return output.format(**{k: get_val(k) for k in field_names})

    def format_proceedings(self):
        pass
    
    def format_abstract(self):
        pass
    
    def format_article(self):
        pass
    
    def format_thesis(self):
        pass
    
    def format_patent(self):
        pass
    
    def apply(self, bib_item):
        type_formatters = {
            '@InProceedings': self.format_proceedings,
            '@Conference': self.format_abstract,
            '@Article': self.format_article,
            '@PhdThesis': self.format_thesis,
            '@Mastersthesis': self.format_thesis,
            '@Patent': self.format_patent
        }
        if bib_item.entry_type in type_formatters:
            return type_formatters[bib_item.entry_type](bib_item)
        
class HTML_Formatter(BaseFormatter):
    
    def __init__(self, string_rules):
        super().__init__(string_rules)
        
    def format_proceedings(self, bib_item):
        authors = authors_to_string(bib_item.author)
        year_number_pages = ''
        for k in 'year', 'number', 'pages':
            value = getattr(bib_item, k)
            if value: 
                year_number_pages += ', ' + value
                
        output = '{authors}. "{title}" in: <i>{booktitle}</i>, volume {volume} of {series}{year_number_pages}'
        return  self.apply_format(output, bib_item, authors=authors, year_number_pages=year_number_pages)
        
    def format_abstract(self, bib_item):
        authors = authors_to_string(bib_item.author)
        output = '{authors}. "{title}" in: {booktitle}, {year}'
        return self.apply_format(output, bib_item, authors=authors)

    def format_article(self, bib_item):
        authors = authors_to_string(bib_item.author)
        nr = '({number})' if getattr(bib_item, 'number') else ''
 
        output = '{authors}. "{title}", {journal}{year};{volume}{nr}{pages}'
        return self.apply_format(output, bib_item, authors=authors, nr=nr)

    def format_thesis(self, bib_item):
        authors = authors_to_string(bib_item.author)
        
        if bib_item.entry_type == '@PhdThesis':
            name = '<i>PhD thesis</i>'
        elif bib_item.entry_type == '@Mastersthesis':
            name = '<i>Mastersthesis</i>'
        else:
            name = '?'
        school = getattr(bib_item, 'school')
        if school:
            school = ', ' + school            
        output = authors +'. "{title}" ' + name + school + ', {year}'
        return self.apply_format(output, bib_item)


    def format_patent(self, bib_item):
        authors = authors_to_string(bib_item.author)
        output = '{authors}. "{title}" {year}, {nationality}, patent number {optnumber}'
        return self.apply_format(output, bib_item, authors=authors)
    
    
    