import networkx as nx
import matplotlib.pyplot as plt



districts = [
'Adilabad','Bhadradri','Hyderabad','Jagtial','Jangaon','Jayashankar',
'Jogulamba','Kamareddy','Karimnagar','Khammam','KomaramBheem',
'Mahabubabad','Mahabubnagar','Mancherial','Medak','Medchal',
'Mulugu','Nagarkurnool','Nalgonda','Narayanpet','Nirmal',
'Nizamabad','Peddapalli','Rajanna','Rangareddy','Sangareddy',
'Siddipet','Suryapet','Vikarabad','Wanaparthy','WarangalRural',
'WarangalUrban','Yadadri'
]

colors = ['red','green','blue','yellow']


neighbors = {
'Hyderabad':['Rangareddy','Medchal'],
'Rangareddy':['Hyderabad','Medchal','Vikarabad','Mahabubnagar'],
'Medchal':['Hyderabad','Rangareddy','Siddipet'],
'Sangareddy':['Medak','Vikarabad','Rangareddy'],
'Vikarabad':['Rangareddy','Sangareddy'],
'Medak':['Sangareddy','Siddipet'],
'Siddipet':['Medak','Medchal','Karimnagar'],
'Karimnagar':['Siddipet','Peddapalli','Rajanna'],
'Peddapalli':['Karimnagar','Mancherial'],
'Mancherial':['Peddapalli','KomaramBheem'],
'KomaramBheem':['Mancherial','Adilabad'],
'Adilabad':['KomaramBheem','Nirmal'],
'Nirmal':['Adilabad','Nizamabad'],
'Nizamabad':['Nirmal','Kamareddy'],
'Kamareddy':['Nizamabad','Rajanna'],
'Rajanna':['Karimnagar','Kamareddy'],
'WarangalUrban':['WarangalRural','Jangaon'],
'WarangalRural':['WarangalUrban','Mulugu'],
'Mulugu':['WarangalRural','Jayashankar'],
'Jayashankar':['Mulugu','Bhadradri'],
'Bhadradri':['Jayashankar','Khammam'],
'Khammam':['Bhadradri','Mahabubabad','Suryapet'],
'Mahabubabad':['Khammam','Jangaon'],
'Jangaon':['Mahabubabad','WarangalUrban','Yadadri'],
'Yadadri':['Jangaon','Nalgonda'],
'Nalgonda':['Yadadri','Suryapet','Nagarkurnool'],
'Suryapet':['Nalgonda','Khammam'],
'Mahabubnagar':['Rangareddy','Narayanpet','Wanaparthy'],
'Narayanpet':['Mahabubnagar','Jogulamba'],
'Jogulamba':['Narayanpet','Wanaparthy'],
'Wanaparthy':['Jogulamba','Mahabubnagar','Nagarkurnool'],
'Nagarkurnool':['Wanaparthy','Nalgonda']
}

for d in districts:
    if d not in neighbors:
        neighbors[d] = []



def is_valid(assign):
    for d in assign:
        for n in neighbors[d]:
            if n in assign and assign[d] == assign[n]:
                return False
    return True

def backtrack(assign):
    if len(assign) == len(districts):
        return assign

    for d in districts:
        if d not in assign:
            var = d
            break

    for c in colors:
        assign[var] = c
        if is_valid(assign):
            res = backtrack(assign)
            if res:
                return res
        del assign[var]

    return None

solution = backtrack({})



G = nx.Graph()

for d in districts:
    G.add_node(d)

for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d, n)



pos = {
'Adilabad': (1,6), 'Nirmal': (2,6), 'Nizamabad': (3,6), 'Kamareddy': (4,5),

'KomaramBheem': (1,5), 'Mancherial': (2,5), 'Jagtial': (3,5), 'Rajanna': (4,4),
'Karimnagar': (5,4), 'Peddapalli': (3,4),

'Siddipet': (6,3), 'Medak': (6,2), 'Sangareddy': (7,1),

'Medchal': (7,3), 'Hyderabad': (8,3), 'Rangareddy': (8,2),

'Vikarabad': (7,0), 'Mahabubnagar': (8,0),

'Narayanpet': (7,-1), 'Jogulamba': (8,-2),
'Wanaparthy': (9,-1), 'Nagarkurnool': (10,0),

'Nalgonda': (10,2), 'Suryapet': (11,2),

'WarangalUrban': (6,4), 'WarangalRural': (7,5),
'Mulugu': (8,6), 'Jayashankar': (7,6),
'Bhadradri': (9,5), 'Khammam': (10,4),
'Mahabubabad': (8,4), 'Jangaon': (6,3),
'Yadadri': (9,3)
}




print("\nTelangana Map Coloring Solution:\n")
for k, v in solution.items():
    print(f"{k} -> {v}")

color_map = [solution[node] for node in G.nodes()]

plt.figure(figsize=(14,10))

nx.draw(G, pos,
        with_labels=True,
        node_color=color_map,
        node_size=1200,
        font_size=7,
        font_weight='bold',
        edge_color='black')

plt.title("Telangana Map Coloring (CSP - Clean Layout)")
plt.savefig("telangana_final.png", dpi=300)

plt.show()