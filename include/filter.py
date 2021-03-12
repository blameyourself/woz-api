innvalidString = ['--',';']

def attribute(attributename: str):
    attrib = str(attributename)
    for row in innvalidString:
        if attrib.upper().find(row.upper()) > 0:
            raise ValueError('Invalid attribute')
    
    return attrib

def table(tablename: str):
    for row in innvalidString:
        if tablename.find(row.upper()) > 0:
            raise ValueError('Invalid  table name')

    return tablename