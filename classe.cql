CREATE (pp1:Punto_panoramico {nome:'Vista San ANDREA', altitudine:2000})
CREATE (pp2:Punto_panoramico {nome:'Vista San LAURA', altitudine:2000})
CREATE (pp3:Punto_panoramico:Partenza{nome:'Vista San GIUSEPPE', altitudine:1400})
CREATE (pp4:Punto_panoramico{nome:'Vista San GIORGIO', altitudine:1200})
CREATE (pp5:Punto_panoramico{nome:'Vista San CARLO', altitudine:1600})
CREATE (pp6:Punto_panoramico{nome:'Vista San MARIA', altitudine:1550})
CREATE (pp7:Punto_panoramico{nome:'Vista San CEPPATO', altitudine:1800})
CREATE (pp8:Punto_panoramico:Partenza{nome:'Vista San LUCA', altitudine:1650})
CREATE (rifugio1:Rifugio {nome:'RIFUGIO SAN MARCO', capacita:2, altitudine:1650})
CREATE (rifugio2:Rifugio:Partenza{nome:'RIFUGIO SAN GIULIA ', capacita:5, altitudine:1550})
CREATE (rifugio3:Rifugio{nome:'RIFUGIO SAN SAMUELE', capacita:7, altitudine:1500})
CREATE (rifugio4:Rifugio:Partenza{nome:'RIFUGIO SAN PIETRO', capacita:3, altitudine:1700})
CREATE (pi1:Punto_interesse:Partenza {nome:'localita San Gabriele', altitudine: 1300})
CREATE (pi2:Punto_interesse:Partenza{nome:'localita San Leonardo', altitudine: 1000})
CREATE (pi3:Punto_interesse:Partenza{nome:'localita Carona', altitudine: 1200})
CREATE (pi4:Punto_interesse:Partenza{nome:'localita San Fedele', altitudine: 1000})
CREATE (pi5:Punto_interesse:Partenza{nome:'localita Fontanella', altitudine: 1100})
CREATE (pi6:Punto_interesse{nome:'localita Merano', altitudine: 1700})
CREATE (pi7:Punto_interesse:Partenza{nome:'localita Ponte di legno', altitudine: 1300})
CREATE (pi8:Punto_interesse{nome:'Vetta del Pellegrino', altitudine: 1900})
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
(pp1)-[:SENTIERO {codice:'K200',durata:120,diff:'facile'}]->(pp2)

