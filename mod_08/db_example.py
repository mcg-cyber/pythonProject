def hae_lentoketta_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    # print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    return kursori.fetchone()

code = input('Syötä lentokentän ICAO koodi: ')
lentokentta = hae_lentoketta_icao_koodilla(code)
if lentokentta is not None:
    print(f"{lentokentta['name']} on paikkakunnalla {lentokentta['municipality']}")
else:
    print('lentokenttää ei löytynyt')
