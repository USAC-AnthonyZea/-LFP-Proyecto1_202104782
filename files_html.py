import webbrowser

class HtmlFile:

    def create_ResultadosHML(texto, title_operaciones, operaciones, expre, estilo):
        
        # Variables para estilo
        color_title = estilo[0][1]
        tamanio_title = estilo[0][2]
        color_descipt = estilo[1][1]
        tamanio_descript = estilo[1][2]
        color_content = estilo[2][1]
        tamanio_content = estilo[2][2]

        # Variables auxiliares
        color1 = ""
        color2 = ""
        color3 = ""

        # Asignando color 
        if color_title == 'AZUL':
            color1 = 'blue'
        elif color_title == 'VERDE':
            color1 = 'green'
        elif color_title == 'ROJO':
            color1 = 'red'
        elif color_title == 'NEGRO':
            color1 = 'black'
        elif color_title == 'BLANCO':
            color1 = 'white'
        elif color_title == 'GRIS':
            color1 = 'gray'
        elif color_title == 'CELESTE':
            color1 = 'skyblue'
        elif color_title == 'CAFE':
            color1 = 'brown'

        if color_descipt == 'AZUL':
            color2 = 'blue'
        elif color_descipt == 'VERDE':
            color2 = 'green'
        elif color_descipt == 'ROJO':
            color2 = 'red'
        elif color_descipt == 'NEGRO':
            color2 = 'black'
        elif color_descipt == 'BLANCO':
            color2 = 'white'
        elif color_descipt == 'GRIS':
            color2 = 'gray'
        elif color_descipt == 'CELESTE':
            color2 = 'skyblue'
        elif color_descipt == 'CAFE':
            color2 = 'brown'
        

        if color_content == 'AZUL':
            color3 = 'blue'
        elif color_content == 'VERDE':
            color3 = 'green'
        elif color_content == 'ROJO':
            color3 = 'red'
        elif color_content == 'NEGRO':
            color3 = 'black'
        elif color_content == 'BLANCO':
            color3 = 'white'
        elif color_content == 'GRIS':
            color3 = 'gray'
        elif color_content == 'CELESTE':
            color3 = 'skyblue'
        elif color_content == 'CAFE':
            color3 = 'brown'
        
        f = open("htmls/RESULTADOS_202104782.html", 'w')
        message = f'''
            <html>
                <head>
                    <title> RESULTADOS_202104782 </title>
                </head>
                <body>
                    <h1 style = "color: {color1}; font-size: {tamanio_title}px"> {title_operaciones} </h1>
                    <h2 style = "color: {color2}; font-size: {tamanio_descript}px"> {texto} </h2>
        '''

        for num, op in zip(operaciones, expre):
            message += f'''
                    <h2 style = "color: {color3}; font-size: {tamanio_content}px"> {num} </h2>
                    <h3 style = "color: {color3}; font-size: {tamanio_content}px"> {op} </h3>
                '''
        message += f'''
            </body>
        </html>
        '''

        f.write(message)
        f.close()
    
    def create_ErroresHtml(errores):

        f = open("htmls/ERRORES_202104782.html", 'w')

        message = '''
            <html>
                <head>
                    <title> ERRORES_202104782 </title>
                    <style>
                        table, th, td{
                            border: 1px solid black;
                        } 
                    </style>
                </head>
                <body>
                    <table>
                        <tr>
                            <th> Lexema </th>
                            <th> Tipo </th>
                            <th> Fila </th>
                            <th> Columna </th>
                        </tr>
        '''
        n = 1
        for i in range(len(errores)):
            message += '<tr>'
            for j in range(len(errores[i])):
                message += f'<td> {errores[i][j]} </td>'
            message += '</tr>'
        
        message += '''
                    </table>
                </body>
            </html>
        '''
        f.write(message)
        f.close()