"""
This file is intended to use only
if you are going to use sqlite3 DB.
"""

import sqlite3


connection = sqlite3.connect("zip_codes_mx.db")

cursor = connection.cursor()

file = "zip_codes.txt"

def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS zip_codes (
            d_codigo,
            d_asenta,
            d_tipo_asenta,
            D_mnpio,
            d_estado,
            d_ciudad,
            d_CP,
            c_estado,
            c_oficina,
            c_CP,
            c_tipo_asenta,
            c_mnpio,
            id_asenta_cpcons,
            d_zona,
            c_cve_ciudad
        )
    """
    cursor.execute(query)


def skip_first_two_lines(file):
    next(file)
    next(file)


def line_to_list(line):
    return line.split("|")


def insert_values_to_db(converted_line):
    insert_query = """
        INSERT INTO zip_codes (
            d_codigo,
            d_asenta,
            d_tipo_asenta,
            D_mnpio,
            d_estado,
            d_ciudad,
            d_CP,
            c_estado,
            c_oficina,
            c_CP,
            c_tipo_asenta,
            c_mnpio,
            id_asenta_cpcons,
            d_zona,
            c_cve_ciudad
        ) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
        """
    
    d_codigo=converted_line[0]
    d_asenta=converted_line[1]
    d_tipo_asenta=converted_line[2]
    D_mnpio=converted_line[3]
    d_estado=converted_line[4]
    d_ciudad=converted_line[5]
    d_CP=converted_line[6]
    c_estado=converted_line[7]
    c_oficina=converted_line[8]
    c_CP=converted_line[9]
    c_tipo_asenta=converted_line[10]
    c_mnpio=converted_line[11]
    id_asenta_cpcons=converted_line[12]
    d_zona=converted_line[13]
    c_cve_ciudad=converted_line[14]
        
    values = [d_codigo,
            d_asenta,
            d_tipo_asenta,
            D_mnpio,
            d_estado,
            d_ciudad,
            d_CP,
            c_estado,
            c_oficina,
            c_CP,
            c_tipo_asenta,
            c_mnpio,
            id_asenta_cpcons,
            d_zona,
            c_cve_ciudad
    ]

    cursor.execute(insert_query, values)

def open_and_read_file(file):
    with open(file, "r", encoding="latin-1") as file:
        skip_first_two_lines(file)
        for line in file:
            converted_line = line_to_list(line)
            insert_values_to_db(converted_line)
        connection.commit()
        connection.close()
    

def main():
    create_table()
    open_and_read_file(file)


if __name__ == "__main__":
    main()
