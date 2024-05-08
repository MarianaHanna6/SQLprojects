#OBS!! under her er koden fra SQL1. (jeg forsøkte å importere fra filen, men fikk det ikke til). Vi forsøker å putte det i en funksjon 
import sqlite3 #Her importerer vi SQLite3
import csv

connect = sqlite3.connect("KundeDatabaseTo.db") #kobler til allerede eksesterende database, hvis den ikke finnes vil det lage en ny database.
cursor = connect.cursor() #cursor er det som henter tabellen og dataen og putter de sammen
cursor.execute("CREATE TABLE IF NOT EXISTS TableToForData (Fornavn, Etternavn, Epost, tlf, Postnummer, PRIMARY KEY (tlf));")
#cursor.execute gjør at vi lager kolonner og gir dem navn slik at dataen som blir importert kan puttes inn riktig.

#Her skal vi lage en type løkke, vi bruker "with" som lar oss handle med filer, lese filer, redigere og lignende. vi legger til "open()" for å åpne filen.
with open('MinSQLfil.csv', 'r') as datafile: #merk at det blir brukt en variabel som vi kaller "datafile"
    dr = csv.DictReader(datafile) #her lager vi en variabel som skal lese gjennom datafilen som er CSV filen
    DataTable_db = [(i['fname'], i['ename'], i['epost'], i['tlf'], i['postnummer']) for i in dr]
    #deretter skal vi lage en variabel som lager en vanlig tabell via python og putter all data-en i den før vi "pusher" det inn i database.

#Her pusher vi dataen som vi samlet opp tidligere med en vanlig tabell og pusher den inn i SQL database
cursor.executemany("INSERT INTO TableToForData (Fornavn, Etternavn, Epost, tlf, Postnummer) VALUES (?, ?, ?, ?, ?)", DataTable_db)
connect.commit() #her "lagrer"/"fullfører" vi det som ble lagt til databasen





#UNDER HER ER RESTEN AV KODEN FOR Å LAGE SQL2. Prikk lik som SQL1 (fordi det er dette som funket best for meg), men selvfølgelig med annen type data.
cursor.execute("CREATE TABLE IF NOT EXISTS TableOfPostTo (Postnummer, Poststed, Kommunenummer, Kommunenavn, Kategori, PRIMARY KEY(Postnummer));")
#cursor.execute gjør at vi lager kolonner og gir dem navn slik at dataen som blir importert kan puttes inn riktig. Forskjellen her er innholdet og tittel på tabellen.

#Her skal vi lage en type løkke, vi bruker "with" som lar oss handle med filer, lese filer, redigere og lignende. vi legger til "open()" for å åpne filen.
with open('Min2SQLfil.csv', 'r') as datafile2: #merk at det blir brukt en variabel som vi kaller "datafile"
    dr2 = csv.DictReader(datafile2) #her lager vi en variabel som skal lese gjennom datafilen som er CSV filen
    DataTable2_db = [(i['Postnummer'], i['Poststed'], i['Kommunenummer'], i['Kommunenavn'], i['Kategori']) for i in dr2] #deretter skal vi lage en variabel som lager en vanlig tabell via python og putter all data-en i den før vi "pusher" det inn i database.

#Her pusher vi dataen som vi samlet opp tidligere med en vanlig tabell og pusher den inn i SQL database
cursor.executemany("INSERT INTO TableOfPostTo (Postnummer, Poststed, Kommunenummer, Kommunenavn, Kategori) VALUES (?, ?, ?, ?, ?);", DataTable2_db)
connect.commit() #her "lagrer"/"fullfører" vi det som ble lagt til databasen
connect.close() #helt til slutt lukker vi "programmet"