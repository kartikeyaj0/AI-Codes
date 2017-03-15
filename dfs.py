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

def depth_first_search(initial, goal_state):
	initial_cost = 0;	
	frontier = []
	frontier.insert(0, initial)
	print 'frontier', ffrontier
	explored = []
	solution = []
	while True:
		print '\n'
		if (not frontier) == True:
			print 'error'
			return
		node = frontier.pop(0)
		print node
		if node == goal_state:
			return
		explored.append(node)
		children = []
		children = road_map[node].keys()
		print 'children', children
		print 'frontier', frontier
		print 'explored', explored
		for child in children:
			print '\nfound child', child
			if child not in explored and child not in frontier:
				frontier.insert(0,child)
		print 'frontier modified', frontier
# print not[]
# cities = road_map.keys()
# for x in cities:
# 	print x, min(road_map[x], key = road_map[x].get)
depth_first_search('Arad', 'Bucharest')
