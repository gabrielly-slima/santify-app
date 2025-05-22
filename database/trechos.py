import sqlite3

conn = sqlite3.connect("trechos.db")

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS frases (id INTEGER PRIMARY KEY, santo TEXT, frase TEXT)')

conn.commit()
conn.close()

def lista_de_trechos():
    trechos = [
        {
            "frase":"Não nos esqueçamos que santo não é o que não cai, mas o que se levanta sempre, com humildade e com santa teimosia", "autor":"Padre Francisco Faus"
        },
        {
            "frase":"Fracassaste? - Tu (estás bem convencido) não podes fracassar.Não fracassaste; adquiriste experiência. - Para a frente!", "autor":"São Josemaria Escrivá"
        },
        {
            "frase":"Aquele que vai subindo jamais cessa de progredir, de começo em começo, através de começos que não têm fim.","autor":"Padre Francisco Faus"
        },
        {
            "frase":"Não fiques nunca satisfeito com aquilo que és, se queres chegar ao que ainda não és. Porque onde te consideraste satisfeito, lá mesmo ficaste parado. Se disseres: já basta, morreste. Cresce sempre, progride sempre, avança sempre", "autor":"Padre Francisco Faus"
        },
        {
            "frase":"Se andas, se te esforças, se tens o pensamento no que está por vir, lança no esquecimento o passado, não voltes o olhar para aquilo, para que não fiques no mesmo ponto onde te detiveste para olhar","autor":"Padre Francisco Faus"
        },
        {
            "frase":"As barreiras, as dificuldades, são o teste da firmeza das nossas decisões","autor":"Padre Francisco Faus"
        },
        {
            "frase":"Quando queremos mesmo, enfrentamos os problemas com força. Assim, os obstáculos que ameaçam impedir- nos de chegar à meta– mesmo os da nossa fraqueza, das nossas debilidades ou quedas pessoais–, em vez de nos paralisar, nos estimulam a reagir, a rezar mais e a empenhar- nos mais.","autor":"Padre Francisco Faus"
        },
        {
            "frase":"Para se chegar, onde quer que seja, é preciso, antes de mais nada, querer».─ «O pior naufrágio é não partir.","autor":"Padre Francisco Faus"
        },
        {
            "frase":"Uma faca enferrujada pode servir para furar bem ou mal uma caixa de papelão, mas não serve para uma cirurgia cardíaca de que depende uma vida.","autor":"Padre Francisco Faus"
        },
        {
           "frase":"Nem as qualificações acadêmicas, nem as capacitações técnicas, nem um alto grau de especialização e experiência setorial definem o “valor humano” de uma pessoa. Ela poderá até chegar ao pináculo da sua “especialidade”, mas fracassará na “vida” como ser humano.", "autor":"Padre Francisco Faus"
        },
        {
            "frase":"Não pretendas desviar o coração de Deus, que é sempre reto, para que se acomode à perversidade do teu.","autor":"Padre Francisco Faus"
        },
        {
            "frase":"A prudência é o amor que sabe discernir bem que coisas nos ajudam a caminhar para Deus, e quais nos podem impedir de fazê- lo","autor":"Padre Francisco Faus"
        }
]

