import operator
road_map = dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75, Craiova=120),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99, Bucharest=211),
    Giurgiu=dict(Bucharest=90),
    Hirsova=dict(Urziceni=98, Eforie=86),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Mehadia=dict(Lugoj=70, Drobeta=75),
    Neamt=dict(Iasi=87),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97, Craiova=138, Bucharest=101),
    Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
    Sibiu=dict(Oradea=151, Arad=140, Rimnicu=80, Fagaras=99),
    Timisoara=dict(Arad=118, Lugoj=111),
    Urziceni=dict(Vaslui=142, Bucharest=85, Hirsova=98),
    Vaslui=dict(Urziceni=142, Iasi=92),
    Zerind=dict(Arad=75, Oradea=71))

def uniform_cost_search(initial, initial_cost, goal_state):
	frontier = {}
	frontier[initial] = initial_cost
	print frontier
	explored = []
	solution = []
	while True:
		print '\n\n'
		if (not frontier) == True:
			return
		node = sorted(frontier.items(), key=operator.itemgetter(1)).pop(0)
		frontier.pop(node[0])
		print node
		if goal_state == node[0]:
			solution.append(node[0])
			return node[0]
		explored.append(node[0])
		
		children = []
		children = road_map[node[0]]
		print children
		print 'frontier', frontier
		print 'explored', explored
		
		for child in children.keys():
			print '\n currently for child', child
			if child not in explored and child not in frontier:
				frontier[child] = children[child] + node[1]
			elif child in frontier and frontier[child] > children[child] + node[1]:
				frontier[child] = children[child] + node[1]
# print road_map['Arad']
# print not[]
# cities = road_map.keys()
# for x in cities:
# 	print x, min(road_map[x], key = road_map[x].get)
print uniform_cost_search('Arad', 0, 'Bucharest')
