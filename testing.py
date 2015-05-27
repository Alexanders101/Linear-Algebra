from utils import *

def determinant_any(m):
    n_dim = m.shape[0]
    perms = array([[perm, 1 if is_even(find_inversions(perm)) else -1] # Create array of permutations and their multipliers
                   for perm in permutations(arange(1, n_dim+1, 1), True)])
    determinant = 0.0
    for permutation in perms: # for every permutation
        determinant += (permutation[1] * # multiplier of given permutation (either 1 or -1) times #
                        prod([m[j, permutation[0][j]-1] for j in xrange(n_dim)])) # product of every a_{nj_n}
    return determinant

def find_minor_matricies(m, column = False, i = 1):
    n_dim = m.shape[0]
    minors = []
    i -= 1
    if not column:
        for j in xrange(n_dim):
            minors.append(array([delete(delete(m, i, 0), j, 1), m[i, j], (-1)**(i+j)]))
    else:
        j = i
        i = None
        for i in xrange(n_dim):
            minors.append(array([delete(delete(m, i, 0), j, 1), m[i, j], (-1)**(i+j)]))
    return array(minors)

def matrix_adjoint(m):
    n_dim = m.shape[0]
    minors = [find_minor_matricies(m, False, row+1) for row in xrange(n_dim)]
    minor_det = matrix([[determinant_any(minor) for minor in min_set] for min_set in minors])
    return minor_det.transpose()
