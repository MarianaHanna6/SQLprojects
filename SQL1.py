import sqlite3  #Her importerer vi SQLite3
import csv

connect = sqlite3.connect("KundeDatabase.db") #kobler til allerede eksesterende database, hvis den ikke finnes vil det lage en ny database.
cursor = connect.cursor() #cursor er det som henter tabellen og dataen og putter de sammen
cursor.execute("CREATE TABLE IF NOT EXISTS TableForData (Fornavn, Etternavn, Epost, Mobilnummer, Postnummer, PRIMARY KEY (Mobilnummer));")
#cursor.execute gjør at vi lager kolonner og gir dem navn slik at dataen som blir importert kan puttes inn riktig.

#Her skal vi lage en type løkke, vi bruker "with" som lar oss handle med filer, lese filer, redigere og lignende. vi legger til "open()" for å åpne filen.
with open('MinSQLfil.csv', 'r') as datafile: #merk at det blir brukt en variabel som vi kaller "datafile"
    dr = csv.DictReader(datafile) #her lager vi en variabel som skal lese gjennom datafilen som er CSV filen
    DataTable_db = [(i['fname'], i['ename'], i['epost'], i['tlf'], i['postnummer']) for i in dr] #deretter skal vi lage en variabel som lager en vanlig tabell via python og putter all data-en i den før vi "pusher" det inn i database.

#Her pusher vi dataen som vi samlet opp tidligere med en vanlig tabell og pusher den inn i SQL database
cursor.executemany("INSERT INTO TableForData (Fornavn, Etternavn, Epost, Mobilnummer, Postnummer) VALUES (?, ?, ?, ?, ?)", DataTable_db)
connect.commit() #her "lagrer"/"fullfører" vi det som ble lagt til databasen
connect.close() #helt til slutt lukker vi "programmet"
