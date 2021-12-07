# write-html.py
import webbrowser

try:
    file_read = open('appOut.txt', 'r')
    try:
        file_read_input_numbers = open('appIn.txt', 'r')
        file_write = open('ProjektJezykiSkryptowe.html', 'w')

        combinations = file_read.readlines()
        input_numbers = int(float(file_read_input_numbers.readline()))

        empty_line = True

        message_start = """<html lang="pl-PL">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width,initial-scale=1.0">
            <title>Szukanie kombinacji</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    color: rgb(255, 255, 255);
                    background: rgb(192, 192, 192);
                    font-size: 27px;
                }
                p.tytul {
                    font-size: 50px;
                    text-align: center;
                }
                p.autor {
                    font-size: 30px;
                    text-align: center;
                }
                table {
                    width: 50vw;
                    height: 50vh;
                    margin-top: 10vh;
                }
                table,
                td {
                    font-size: 24px;
                    border: 3px solid #333;
                    text-align: center;
                }
                table, th {
                    background: rgb(254, 127, 0);
                }

                thead,
                tfoot {
                    background-color: #333;
                    color: #fff;
                }
                .center {
                    margin-left: auto;
                    margin-right: auto;
                }
                table, th, td {
                    border-collapse: collapse;
                }
                td{
                    border:1px solid black;
                    border-top: none;
                    border-bottom: none;
                }
            </style>
        </head>
        <body>
            <p class="tytul">Szukanie Kombinacji
            <p class="autor"> Autor: Mariusz Wr&#243bel
                <table class="center">"""

        message_end = """</table></p></body>
        </html>"""

        file_write.write(message_start)
        file_write.write('\n')

        for lines in combinations:
            file_write.write("<tr>")
            file_write.write("<td>")
            if empty_line:
                file_write.write(f'n = {input_numbers} &nbsp')
                input_numbers = file_read_input_numbers.readline()
                empty_line = False

            if lines == '\n':
                empty_line = True
            file_write.write("</td>")
            file_write.write("<td>")
            file_write.write(lines)
            file_write.write("<br>")
            file_write.write("</td>")
            file_write.write('\n')

        file_write.write(message_end)

        file_read.close()
        file_read_input_numbers.close()
        file_write.close()

        webbrowser.open_new_tab('ProjektJezykiSkryptowe.html')
        
        print("Skrypt web.py wykonał się poprawnie.")

    except IOError:
        print("Błąd otwierania pliku appIn.txt")
except IOError:
    print("Błąd otwierania pliku appOut.txt")
