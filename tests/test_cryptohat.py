import time
import numpy as np
from cryptohat.algorithm import hat_tiles_algorithm

def get_edge(tile, direction):
    if direction == 'top':
        return tile[0]
    elif direction == 'right':
        return tile[:, -1]
    elif direction == 'bottom':
        return tile[-1]
    elif direction == 'left':
        return tile[:, 0]
    else:
        raise ValueError('Invalid direction')

def test_hat_tiles_algorithm():
    tiles = hat_tiles_algorithm(3, iterations=1)
    print(tiles)

    # Check that all tiles are unique
    unique_tiles = set(tuple(map(tuple, row)) for row in tiles)
    assert len(unique_tiles) == 10**2

    # Check that adjacent tiles match
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < len(tiles) and 0 <= nj < len(tiles) and tiles[i][j] is not None and tiles[ni][nj] is not None:
                    assert np.array_equal(get_edge(tiles[i][j], di), get_edge(tiles[ni][nj], -di))
    
    # Check that the algorithm terminates in a reasonable amount of time
    max_iterations = 10000
    for i in range(2, 11):
        start_time = time.time()
        hat_tiles_algorithm(i, iterations=10)
        elapsed_time = time.time() - start_time
        assert elapsed_time < max_iterations, f"Algorithm took too long to terminate with tile size {i}"


def _test_hat_tiles_algorithm():
    tile_size = 50
    iterations = 50
    start_time = time.time()
    tiles = hat_tiles_algorithm(tile_size, iterations)
    end_time = time.time()
    print(tiles)
    assert tiles is not None
    assert len(tiles) == tile_size
    assert len(tiles[0]) == tile_size
    for row in tiles:
        for tile in row:
            assert tile is not None
            assert tile.shape == (11, 2)
    print(f"hat_tiles_algorithm() took {end_time - start_time:.2f} seconds to generate {tile_size ** 2} tiles")

