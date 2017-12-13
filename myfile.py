def  JordanUniversitiesAfterYear(certainYear):
    import json
    from SPARQLWrapper import SPARQLWrapper, JSON

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery("""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT  ?Instance_dungeonLabel ?inception WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      ?Instance_dungeon wdt:P31 wd:Q3918.
      ?Instance_dungeon wdt:P17 wd:Q810.
      OPTIONAL { ?Instance_dungeon wdt:P571 ?inception. }
    }""")
    sparql.setReturnFormat(JSON)
    results = json.dumps(sparql.query().convert(), indent=4)

    english =open('jsontest.json', 'w')
    english.write(results)
    english.close()

    data = json.load(open('jsontest.json','r'))
    for i in range(0,34):
        x = data['results']['bindings'][i]['inception']['value']
        if (x[:4] >= str(certainYear)):
            print(data['results']['bindings'][i]['Instance_dungeonLabel']['value'])

JordanUniversitiesAfterYear(2005)
