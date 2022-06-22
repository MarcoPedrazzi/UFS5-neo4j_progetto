from neo4j import GraphDatabase


class PercosiMontanari:

    def __init__(self, neo4j_uri='bolt://localhost:7687', neo4j_username='', neo4j_password=''):

        print(f"Collegandosi al database {neo4j_uri}.")
        self.driver = GraphDatabase.driver(
            neo4j_uri, auth=(neo4j_username, neo4j_password))
        print(f"Collegato al database {neo4j_uri}.")

    def close(self):
        if self.driver:
            self.driver.close()

    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]

    def delete_one(self, id, nodo=True):
        with self.driver.session() as session:
            if nodo:
                return session.run("match (n) where id(n)="+str(id)+" detach delete n return count(n)").single()[0]
            else:
                return session.run("match ()-[n]-()where id(n)="+str(id)+" detach delete n return count(n)").single()[0]

    node_template = {
        'nome': '',
        'cap_max': '',
        'label': [],
        'altitudine': ''
    }

    def create_node(self, data=node_template):
        if data['label'][0] == 'rifugio' and data['label'][1] == 'Partenza':
            temp = 'CREATE (rifugio:Rifugio:Partenza{nome:$name, capacita:$cap_max}) return rifugio'
        else:
            temp = 'CREATE (rifugio:Rifugio{nome:$name, capacita:$cap_max}) return rifugio'
        if ['label'][0] == "panoramico" and data['label'][1] == 'Partenza':
            temp = 'CREATE (pp:Punto_panoramico:Partenza{nome:$name, altitudine:$altitude}) return pp'
        else:
            temp = 'CREATE (pp:Punto_panoramico{nome:$name, altitudine:$altitude}) return pp'
        if ['label'][0] == "interesse" and data['label'][1] == 'Partenza':
            temp = 'CREATE (pi:Punto_di_interesse:Partenza{nome:$name, altitudine:$altitude}) return pi'
        else:
            temp = 'CREATE (pi:Punto_di_interesse{nome:$name, altitudine:$altitude}) return pi'

        print(data)

        with self.driver.session() as session:
            result = session.run(temp,
                                 name=data["nome"],
                                 max=data["cap_max"],
                                 altitude=data['altitudine'])
            return result.single()[0].id

    node_template_mod = {
        'nome': '',
        'altitudine': 0,
        'capacita': 0}

    def modify_node(self,node_id, data=node_template_mod):
        temp="MATCH (p) WHERE id(p)="+str(node_id)+" SET "
        for e in data.keys():
            temp+="p."+e+" = '"+str(data[e])+"', "
        temp = temp.rstrip(", ")
        with self.driver.session() as session:
            result = session.run(temp+"RETURN p")
            return dict(result.single()[0])

    def get_node(self, id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (a) WHERE id(a) = "+str(id)+" RETURN a")
            temp = result.single()[0]
            if temp:
                return dict(temp)
            else:
                return None

    arc_template = {
        'durate': 0,
        'codice': '',
        'difficolta': ''
    }

    def crate_arc(self, codice, durate, difficolta, start_id, end_id):
        with self.driver.session() as session:
            result = session.run("create(id($start))-[s:Sentiero{codice:$c, durata:$p, difficolta:$d})->($end) return id(c)",
                                 c=codice,
                                 p=durate,
                                 d=difficolta,
                                 start=start_id,
                                 end=end_id)
            return result.single()[0]

    def modify_arc(self, data=arc_template):
        with self.driver.session() as session:
            result = session.run("create(s:Sentiero{codice:$code, durata:$d, difficolta:$diff}) return id(c)",
                                 code=data['codice'],
                                 d=data['durate'],
                                 diff=data['difficolta'])
            return result.single()[0]

    def get_arc(self, data=arc_template, id=None):
        with self.driver.session() as session:
            if id != None:
                result = session.run(
                    "MATCH ()-[a]-() WHERE id(a) = "+str(id)+" RETURN a")
            else:
                if data['durata'] and data['codice'] and data['difficolta']:
                    result = session.run("MATCH ()-[a{durata:$d,codice:$c,difficolta:$diff}]-() RETURN a",
                                         c=data['codice'], d=data['durate'], diff=data['difficolta'])
                elif data['durata']:
                    result = session.run(
                        "MATCH ()-[a{durata:$d}]-() RETURN a", d=data['durate'])
                elif data['codice']:
                    result = session.run(
                        "MATCH ()-[a{codice:$c}]-() RETURN a", c=data['codice'])
                elif data['difficolta']:
                    result = session.run(
                        "MATCH ()-[a{difficolta:$diff}]-() RETURN a", diff=data['difficolta'])
        return result.single()[0]

    def demo(self):
        with self.driver.session() as session:
            session.run("""CREATE (pp1:Punto_panoramico {nome:'Vista San ANDREA', altitudine:2000, capacita:0})CREATE (pp2:Punto_panoramico {nome:'Vista San LAURA', altitudine:2000})
CREATE (pp3:Punto_panoramico:Partenza{nome:'Vista San GIUSEPPE', altitudine:1400, capacita:0})
CREATE (pp4:Punto_panoramico{nome:'Vista San GIORGIO', altitudine:1200, capacita:0})
CREATE (pp5:Punto_panoramico{nome:'Vista San CARLO', altitudine:1600, capacita:0})
CREATE (pp6:Punto_panoramico{nome:'Vista San MARIA', altitudine:1550, capacita:0})
CREATE (pp7:Punto_panoramico{nome:'Vista San CEPPATO', altitudine:1800, capacita:0})
CREATE (pp8:Punto_panoramico:Partenza{nome:'Vista San LUCA', altitudine:1650, capacita:0})
CREATE (rifugio1:Rifugio {nome:'RIFUGIO SAN MARCO', capacita:2, altitudine:1650})
CREATE (rifugio2:Rifugio:Partenza{nome:'RIFUGIO SAN GIULIA ', capacita:5, altitudine:1550})
CREATE (rifugio3:Rifugio{nome:'RIFUGIO SAN SAMUELE', capacita:7, altitudine:1500})
CREATE (rifugio4:Rifugio:Partenza{nome:'RIFUGIO SAN PIETRO', capacita:3, altitudine:1700})
CREATE (pi1:Punto_interesse:Partenza {nome:'localita San Gabriele', altitudine: 1300, capacita:0})
CREATE (pi2:Punto_interesse:Partenza{nome:'localita San Leonardo', altitudine: 1000, capacita:0})
CREATE (pi3:Punto_interesse:Partenza{nome:'localita Carona', altitudine: 1200, capacita:0})
CREATE (pi4:Punto_interesse:Partenza{nome:'localita San Fedele', altitudine: 1000, capacita:0})
CREATE (pi5:Punto_interesse:Partenza{nome:'localita Fontanella', altitudine: 1100, capacita:0})
CREATE (pi6:Punto_interesse{nome:'localita Merano', altitudine: 1700, capacita:0})
CREATE (pi7:Punto_interesse:Partenza{nome:'localita Ponte di legno', altitudine: 1300, capacita:0})
CREATE (pi8:Punto_interesse{nome:'Vetta del Pellegrino', altitudine: 1900, capacita:0})
CREATE (rifugio1)-[:SENTIERO {codice:'K205',durata:330,diff:'medio'}]->(pp1),
(pi1)-[:SENTIERO {codice:'K203',durata:150,diff:'medio'}]->(rifugio1),
(pi2)-[:SENTIERO {codice:'K300',durata:300,diff:'difficile'}]->(rifugio2),
(pi3)-[:SENTIERO {codice:'K301',durata:120,diff:'medio'}]->(rifugio2),
(pi3)-[:SENTIERO {codice:'K302',durata:180,diff:'facile'}]->(rifugio3),
(pi7)-[:SENTIERO {codice:'K303',durata:150,diff:'facile'}]->(rifugio3),
(rifugio3)-[:SENTIERO {codice:'K304',durata:80,diff:'facile'}]->(pp8),
(rifugio3)-[:SENTIERO {codice:'K305',durata:150,diff:'facile'}]->(rifugio2),
(rifugio3)-[:SENTIERO {codice:'K306',durata:90,diff:'facile'}]->(pp5),
(rifugio3)-[:SENTIERO {codice:'K307',durata:30,diff:'facile'}]->(pp6),
(pp6)-[:SENTIERO {codice:'K308',durata:70,diff:'facile'}]->(pi6),
(pp5)-[:SENTIERO {codice:'K309',durata:80,diff:'facile'}]->(pi6),
(rifugio2)-[:SENTIERO {codice:'K310',durata:60,diff:'facile'}]->(pp5),
(pp5)-[:SENTIERO {codice:'K311',durata:120,diff:'facile'}]->(rifugio4),
(rifugio4)-[:SENTIERO {codice:'K312',durata:100,diff:'facile'}]->(pp7),
(pi4)-[:SENTIERO {codice:'K201',durata:120,diff:'medio'}]->(pp3),
(pi5)-[:SENTIERO {codice:'K202',durata:90,diff:'facile'}]->(pp4),
(pp4)-[:SENTIERO {codice:'K204',durata:120,diff:'facile'}]->(pp3),
(pp3)-[:SENTIERO {codice:'K207',durata:150,diff:'medio'}]->(rifugio1),
(rifugio1)-[:SENTIERO {codice:'K206',durata:270,diff:'difficile'}]->(pp2),
(rifugio1)-[:SENTIERO {codice:'K401',durata:70,diff:'medio'}]->(pp7),
(pp7)-[:SENTIERO {codice:'K402',durata:90,diff:'facile'}]->(pi8),
(pp1)-[:SENTIERO {codice:'K200',durata:120,diff:'facile'}]->(pp2)""")
        session.close()
# restrizzioni su:
#       tempo
#       difficoltà
#       n° persone
#       rifugi
#       viste panoramiche

    def percorso(self, durata_max=200, durata_min=0):
        with self.driver.session() as session:
            res = """MATCH percorso=(origin:Partenza)-[:SENTIERO*]-() 
            with reduce(tempo=0, tratta in relationships(percorso) | tempo + tratta.durata) as tempototale, 
            reduce(descr='', tratta in relationships(percorso) | descr +'/'+ tratta.codice) as descrizione, 
            reduce(descrizione='', punti in nodes(percorso) | descrizione + '/' + punti.nome ) as punti,
            reduce(descr='', tratta in relationships(percorso) |  descr +'/'+  tratta.diff) as difficolta,
            reduce(descrizione='', punti in nodes(percorso) | descrizione + '/' + punti.capacita) as capacita
            where tempototale <=$tempo_massimo and tempototale>=$ tempo_minimo
            return tempototale, descrizione, punti, difficolta,capacita
            order by tempototale
            """
            result = session.run(
                res, tempo_massimo=durata_max, tempo_minimo=durata_min)
            return result.data()
# ------------------------------------------------------------------

if __name__== '__main__':
    percorsi_montanari = PercosiMontanari()
    # percorsi_montanari.demo()

    node_get = percorsi_montanari.get_node(0)
    print(node_get)

    temp = {
    'nome': 'Vista-San',
    'cap_max': '0',
    'label': ['panoramico'],
    'altitudine': '10000'
    }
    node_create =percorsi_montanari.create_node(temp)
    print(node_create)
    percorsi_montanari.delete_one(node_create)

    node_moify =percorsi_montanari.modify_node(0,{'altitudine': 10000, 'nome': 'Vista-San'})
    print(node_moify)
    node_moify =percorsi_montanari.modify_node(0,{'altitudine': 2000, 'nome': 'Vista San ANDREA'})
    print(node_moify)

    # percorsi=percorsi_montanari.percorso(durata_max=300,durata_min=200)
    # percorsi_montanari.empty_database()
