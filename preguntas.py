x = open("data.csv", "r").readlines()
x = [z.replace("\t", " ") for z in x]
x = [z.replace("\n", "") for z in x]
x = [z.split(" ") for z in x]
"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Extrae la columna 2
    colum_dos= ([z[1] for z in x[0:]])
    # Pasamos la columna 2 a int
    colum_dos_int = ([int(x) for x in colum_dos])
    #Suma de la columna 2
    suma_de_notas = 0
    for nota in colum_dos_int:
        suma_de_notas  += nota


    return suma_de_notas


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    colum_uno= ([z[0] for z in x[0:]])
    my_dict = {i:colum_uno.count(i) for i in colum_uno}
    registros = list(my_dict.items())
    registros_or = sorted(registros)
  
    return registros_or


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    colum_dos= ([z[1] for z in x[0:]])
    colum_dos_int = ([int(x) for x in colum_dos])
    colum_uno= ([z[0] for z in x[0:]])
    zipped_uno_dos = zip(colum_uno, colum_dos_int)
    uno_dos=list(zipped_uno_dos)
    result = {}
    for st, value in uno_dos:
      total = result.get(st, 0) + value
      result[st] = total
    uno_dos_list = sorted(list(result.items()))
    
    return uno_dos_list


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    colum_tres= ([z[2] for z in x[0:]])
    colum_tres = [z.split("-") for z in colum_tres]
    colum_tres_month = ([z[1] for z in colum_tres[0:]])
    my_dict_tres = {i:colum_tres_month.count(i) for i in colum_tres_month}
    registros_tres = list(my_dict_tres.items())
    registros_tres_or = sorted(registros_tres)
    return registros_tres_or


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    colum_dos= ([z[1] for z in x[0:]])
    colum_dos_int = ([int(x) for x in colum_dos])
    colum_uno= ([z[0] for z in x[0:]])
    zipped_uno_dos = zip(colum_uno, colum_dos_int)
    uno_dos=list(zipped_uno_dos)

    A_col1_col2 = [z for z in uno_dos if z[0] == "A"]
    A_max = max(A_col1_col2)
    A_min = min(A_col1_col2)
    A_max_min = (list(A_max + A_min))
    del A_max_min[2]

    B_col1_col2 = [z for z in uno_dos if z[0] == "B"]
    B_max = max(B_col1_col2)
    B_min = min(B_col1_col2)
    B_max_min = (list(B_max + B_min))
    del B_max_min[2]

    C_col1_col2 = [z for z in uno_dos if z[0] == "C"]
    C_max = max(C_col1_col2)
    C_min = min(C_col1_col2)
    C_max_min = (list(C_max + C_min))
    del C_max_min[2]

    D_col1_col2 = [z for z in uno_dos if z[0] == "D"]
    D_max = max(D_col1_col2)
    D_min = min(D_col1_col2)
    D_max_min = (list(D_max + D_min))
    del D_max_min[2]

    E_col1_col2 = [z for z in uno_dos if z[0] == "E"]
    E_max = max(E_col1_col2)
    E_min = min(E_col1_col2)
    E_max_min = (list(E_max + E_min))
    del E_max_min[2]

    Col1_max_min_t = (tuple(A_max_min),tuple(B_max_min),tuple(C_max_min),tuple(D_max_min),tuple(E_max_min))
    Col1_max_min_t = list(Col1_max_min_t)
    return Col1_max_min_t


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    colum_cinco= ([z[4] for z in x[0:]])
    colum_cinco
    aa = str(colum_cinco)
    aa = aa.replace('[', '')
    aa = aa.replace("'", "")
    aa = aa.replace(" ", "")
    aa = aa.replace(']', '')
    aa = aa.split(",")

    col_5_sp_t = [z.split(":") for z in aa]

    col_5_1 = str([item[0].split(",") for item in col_5_sp_t])
    col_5_1 = col_5_1 .replace('[', '')
    col_5_1 = col_5_1 .replace(']', '')
    col_5_1 = col_5_1 .replace("'", "")
    col_5_1 = col_5_1 .replace(" ", "")
    col_5_1 = col_5_1.split(",")

    col_5_0 = str(([item[1].split(",") for item in col_5_sp_t]))
    col_5_0 = col_5_0 .replace('[', '')
    col_5_0 = col_5_0 .replace(']', '')
    col_5_0 = col_5_0 .replace("'", "")
    col_5_0 = col_5_0 .replace(" ", "")
    col_5_0 = col_5_0.split(",")

    colum_dos_5_int = ([int(x) for x in col_5_0])

    zipped_5_uno_dos = zip(col_5_1, colum_dos_5_int)
    col_5_sp =list(zipped_5_uno_dos)


    col5_aaa = [z for z in col_5_sp if z[0] == "aaa"]
    aaa_max = max(col5_aaa)
    aaa_min = min(col5_aaa)
    aaa_max_min = (list(aaa_min + aaa_max))
    del aaa_max_min[2]

    col5_bbb = [z for z in col_5_sp if z[0] == "bbb"]
    bbb_max = max(col5_bbb)
    bbb_min = min(col5_bbb)
    bbb_max_min = (list(bbb_min + bbb_max))
    del bbb_max_min[2]

    col5_ccc = [z for z in col_5_sp if z[0] == "ccc"]
    ccc_max = max(col5_ccc)
    ccc_min = min(col5_ccc)
    ccc_max_min = (list(ccc_min + ccc_max))
    del ccc_max_min[2]

    col5_ddd = [z for z in col_5_sp if z[0] == "ddd"]
    ddd_max = max(col5_ddd)
    ddd_min = min(col5_ddd)
    ddd_max_min = (list(ddd_min + ddd_max))
    del ddd_max_min[2]

    col5_eee = [z for z in col_5_sp if z[0] == "eee"]
    eee_max = max(col5_eee)
    eee_min = min(col5_eee)
    eee_max_min = (list(eee_min + eee_max))
    del eee_max_min[2]

    col5_fff = [z for z in col_5_sp if z[0] == "fff"]
    fff_max = max(col5_fff)
    fff_min = min(col5_fff)
    fff_max_min = (list(fff_min + fff_max))
    del fff_max_min[2]

    col5_ggg = [z for z in col_5_sp if z[0] == "ggg"]
    ggg_max = max(col5_ggg)
    ggg_min = min(col5_ggg)
    ggg_max_min = (list(ggg_min + ggg_max))
    del ggg_max_min[2]

    col5_hhh = [z for z in col_5_sp if z[0] == "hhh"]
    hhh_max = max(col5_hhh)
    hhh_min = min(col5_hhh)
    hhh_max_min = (list(hhh_min + hhh_max))
    del hhh_max_min[2]

    col5_iii = [z for z in col_5_sp if z[0] == "iii"]
    iii_max = max(col5_iii)
    iii_min = min(col5_iii)
    iii_max_min = (list(iii_min + iii_max))
    del iii_max_min[2]

    col5_jjj = [z for z in col_5_sp if z[0] == "jjj"]
    jjj_max = max(col5_jjj)
    jjj_min = min(col5_jjj)
    jjj_max_min = (list(jjj_min + jjj_max))
    del jjj_max_min[2]

    Col5_min_max_t = (tuple(aaa_max_min),tuple(bbb_max_min),tuple(ccc_max_min),tuple(ddd_max_min),tuple(eee_max_min),tuple(fff_max_min),tuple(ggg_max_min),tuple(hhh_max_min),tuple(iii_max_min),tuple(jjj_max_min))
    Col5_min_max_t = list(Col5_min_max_t)

    return Col5_min_max_t


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    colum_dos= ([z[1] for z in x[0:]])
    colum_dos_int = ([int(x) for x in colum_dos])
    colum_uno= ([z[0] for z in x[0:]])
    zipped_dos_uno = zip(colum_dos_int, colum_uno)
    dos_uno=list(zipped_dos_uno)

    zero = []
    for num, le in dos_uno:
      if num == 0:
        zero.append (le)
    zero = (0,zero)

    uno = []
    for num, le in dos_uno:
      if num == 1:
        uno.append (le)
    uno = (1,uno)

    dos = []
    for num, le in dos_uno:
      if num == 2:
        dos.append (le)
    dos = (2,dos)

    tres = []
    for num, le in dos_uno:
      if num == 3:
        tres.append (le)
    tres = (3,tres)

    cuatro = []
    for num, le in dos_uno:
      if num == 4:
        cuatro.append (le)
    cuatro = (4,cuatro)

    cinco = []
    for num, le in dos_uno:
      if num == 5:
        cinco.append (le)
    cinco = (5,cinco)

    seis = []
    for num, le in dos_uno:
      if num == 6:
        seis.append (le)
    seis = (6,seis)

    siete = []
    for num, le in dos_uno:
      if num == 7:
        siete.append (le)
    siete = (7,siete)

    ocho = []
    for num, le in dos_uno:
      if num == 8:
        ocho.append (le)
    ocho = (8,ocho)

    nueve = []
    for num, le in dos_uno:
      if num == 9:
        nueve.append (le)
    nueve = (9,nueve)

    dos_uno_t = (tuple(zero),tuple(uno),tuple(dos),tuple(tres),tuple(cuatro),tuple(cinco),tuple(seis),tuple(siete),tuple(ocho),tuple(nueve))
    dos_uno_t = list(dos_uno_t)

    return dos_uno_t


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    colum_dos= ([z[1] for z in x[0:]])
    colum_dos_int = ([int(x) for x in colum_dos])
    colum_uno= ([z[0] for z in x[0:]])
    zipped_dos_uno = zip(colum_dos_int, colum_uno)
    dos_uno=list(zipped_dos_uno)

    zero = []
    for num, le in dos_uno:
      if num == 0:
        zero.append (le)
    zero = sorted(list(dict.fromkeys(zero)))
    zero = (0,zero)

    uno = []
    for num, le in dos_uno:
      if num == 1:
        uno.append (le)
    uno = sorted(list(dict.fromkeys(uno)))
    uno = (1,uno)

    dos = []
    for num, le in dos_uno:
      if num == 2:
        dos.append (le)
    dos = sorted(list(dict.fromkeys(dos)))
    dos = (2,dos)

    tres = []
    for num, le in dos_uno:
      if num == 3:
        tres.append (le)
    tres = sorted(list(dict.fromkeys(tres)))
    tres = (3,tres)

    cuatro = []
    for num, le in dos_uno:
      if num == 4:
        cuatro.append (le)
    cuatro = sorted(list(dict.fromkeys(cuatro)))
    cuatro = (4,cuatro)

    cinco = []
    for num, le in dos_uno:
      if num == 5:
        cinco.append (le)

    cinco = sorted(list(dict.fromkeys(cinco)))
    cinco = (5,cinco)

    seis = []
    for num, le in dos_uno:
      if num == 6:
        seis.append (le)
    seis = sorted(list(dict.fromkeys(seis)))
    seis = (6,seis)

    siete = []
    for num, le in dos_uno:
      if num == 7:
        siete.append (le)
    siete = sorted(list(dict.fromkeys(siete)))
    siete = (7,siete)

    ocho = []
    for num, le in dos_uno:
      if num == 8:
        ocho.append (le)
    ocho = sorted(list(dict.fromkeys(ocho)))
    ocho = (8,ocho)

    nueve = []
    for num, le in dos_uno:
      if num == 9:
        nueve.append (le)
    nueve = sorted(list(dict.fromkeys(nueve)))
    nueve = (9,nueve)

    dos_uno_t_or = (tuple(zero),tuple(uno),tuple(dos),tuple(tres),tuple(cuatro),tuple(cinco),tuple(seis),tuple(siete),tuple(ocho),tuple(nueve))
    dos_uno_t_or = list(dos_uno_t_or)

    return dos_uno_t_or


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    colum_cinco= ([z[4] for z in x[0:]])
    colum_cinco
    aa = str(colum_cinco)
    aa = aa.replace('[', '')
    aa = aa.replace("'", "")
    aa = aa.replace(" ", "")
    aa = aa.replace(']', '')
    aa = aa.split(",")

    col_5_sp_t = [z.split(":") for z in aa]

    col_5_1 = str([item[0].split(",") for item in col_5_sp_t])
    col_5_1 = col_5_1 .replace('[', '')
    col_5_1 = col_5_1 .replace(']', '')
    col_5_1 = col_5_1 .replace("'", "")
    col_5_1 = col_5_1 .replace(" ", "")
    col_5_1 = col_5_1.split(",")
    col_5_1 = sorted(col_5_1)

    my_dict = {i:col_5_1.count(i) for i in col_5_1}

    return my_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    uno= ([z[0] for z in x[0:]])
    cuatro = ([z[3] for z in x[0:]])
    cinco = ([z[4] for z in x[0:]])

    uno_cuatro_cinco = list(zip(uno, cuatro, cinco))
    cuatro_c = []
    cinco_c = []
    for uno, cuatro, cinco in uno_cuatro_cinco:
      cuatro_c.append(cuatro.count(",") + 1)
      cinco_c.append(cinco.count(",") + 1)
    uno= ([z[0] for z in x[0:]])

    final_10 = list(zip(uno, cuatro_c, cinco_c))

    return final_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    colum_cuatro = ([z[3] for z in x[0:]])
    colum_dos = ([z[1] for z in x[0:]])
    colum_dos = ([int(x) for x in colum_dos])
    cuatro_dos = list(zip(colum_cuatro, colum_dos))

    aa = 0
    for cuatro, dos in cuatro_dos:
          if "a" in cuatro:
            aa = aa + dos
    bb = 0
    for cuatro, dos in cuatro_dos:
          if "b" in cuatro:
            bb = bb + dos
    cc = 0
    for cuatro, dos in cuatro_dos:
          if "c" in cuatro:
            cc = cc + dos

    dd = 0
    for cuatro, dos in cuatro_dos:
          if "d" in cuatro:
            dd = dd + dos

    ee = 0
    for cuatro, dos in cuatro_dos:
          if "e" in cuatro:
            ee = ee + dos

    ff = 0
    for cuatro, dos in cuatro_dos:
          if "f" in cuatro:
            ff = ff + dos

    gg = 0
    for cuatro, dos in cuatro_dos:
          if "g" in cuatro:
            gg = gg + dos

    my_dict_11 = {"a": aa, "b": bb, "c": cc, "d": dd, "e": ee, "f": ff, "g": gg}

    return my_dict_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    colum_cinco = ([z[4] for z in x[0:]])
    colum_uno = ([z[0] for z in x[0:]])
    colum_cinco
    s = []

    import re

    out = [re.sub(r'\D', ' ', s) for s in colum_cinco]
    out = [z.replace("    ", "") for z in out]
    out = [z.replace(" ", ",") for z in out]
    out = [z.split(",") for z in out]

    lst = [[int(num) for num in lstt[:]] for lstt in out]

    lst = [sum(x) for x in lst]

    uno_cinco = list(zip(colum_uno, lst))

    aa = 0
    for cinco, uno in uno_cinco:
          if "A" in cinco:
            aa = aa + uno
    bb = 0
    for cinco, uno in uno_cinco:
          if "B" in cinco:
            bb = bb + uno
    cc = 0
    for cinco, uno in uno_cinco:
          if "C" in cinco:
            cc = cc + uno

    dd = 0
    for cinco, uno in uno_cinco:
          if "D" in cinco:
            dd = dd + uno

    ee = 0
    for cinco, uno in uno_cinco:
          if "E" in cinco:
            ee = ee + uno



    my_dict_12 = {"A": aa, "B": bb, "C": cc, "D": dd, "E": ee}

    return my_dict_12
