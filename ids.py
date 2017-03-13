import dls
def iterative_deepening_search(initial, goal_state):
	for depth in xrange(1,10):
		result = dls.depth_limited_search(initial, goal_state, depth)
		print depth, result
		if result != 'cutoff':
			return result
print 'returned value : ', iterative_deepening_search('Arad', 'Bucharest')