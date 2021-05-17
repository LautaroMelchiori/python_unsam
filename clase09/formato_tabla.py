# formato_tabla.py

class FormatoTabla():
    def encabezado(self, headers):
        """
        Crea el encabezado de la tabla
        """
        raise NotImplementedError()

    
    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    """
    Generar una tabla en formato HTML
    """
    def encabezado(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f"<th>{h}</th>", end = '')
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>', end = '')
        for e in data_fila:
            print(f"<td>{e}</td>", end = '')
        print('</tr>')

def crear_formateador(fmt):
    """
    Recibe un formato en forma de string
    Devuelve un formateador del tipo pedido
    Formatos disponibles:
    - txt
    - csv
    - html
    """
    if fmt == 'txt':
        return FormatoTablaTXT()
    elif fmt == 'csv':
        return FormatoTablaCSV()
    elif fmt == 'html':
        return FormatoTablaHTML()

def imprimir_tabla(objects, attrs, fmt):
    fmt.encabezado(attrs)
    for object in objects:
        rowdata = []
        for attr in attrs:
            item = getattr(object, attr, None)
            
            # make every item a string and round floats to 2 decimals
            if isinstance(item, float):
                item = f'{item:0.2f}'
            else:
                item = str(item)
                
            rowdata.append(item)
        fmt.fila(rowdata)