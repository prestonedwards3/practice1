import docx

file = '/Users/prestonedwards/desktop/Templates/cwdDEF.docx'

document = docx.Document(file)

print(document.paragraphs[0].text)