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

def depth_limited_search(initial, goal_state, limit):
	result = rec_dls(initial, goal_state, limit)
	return result

def rec_dls(initial, goal_state, limit):
	print initial, goal_state, limit
	if goal_state == initial:
		return 'successful'
	elif limit == 0:
		return 'cutoff'
	else:
		cutoff_occurred = False
		children = []
		children = road_map[initial].keys()
		print children
		print '\n\n'
		for child in children:
			result = rec_dls(child, goal_state, limit - 1)
			print result
			if result == 'cutoff':
				cutoff_occurred = True
			elif result != 'failure':
				return result
		if cutoff_occurred:
			return 'cutoff'
		else:
			return 'failure'
print depth_limited_search('Arad', 'Bucharest', 0)