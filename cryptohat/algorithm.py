import numpy as np
import random

class HatTile:
    def __init__(self, vertices):
        self.vertices = np.array(vertices)

    def random_rotation(self):
        """
        This implementation creates a rotation matrix based on a random angle of either pi/2 or 3*pi/2, 
        applies the matrix to each vertex individually, 
        and then returns a new HatTile object with the rotated vertices.
        """
        theta = np.random.choice([np.pi/2, 3*np.pi/2])
        c, s = np.cos(theta), np.sin(theta)
        rotation_matrix = np.array([[c, -s], [s, c]])
        rotated_vertices = np.empty_like(self.vertices)
        for i, vertex in enumerate(self.vertices):
            rotated_vertices[i] = rotation_matrix @ vertex
        return HatTile(rotated_vertices.tolist())

    def __getitem__(self, index):
        return self.vertices[index]

HAT_TILE = HatTile([[0, 1], [1, 1], [1, 0], [0, 0], [0.5, -1],
                    [1.5, -1], [2, 0], [2, 1], [1.5, 2],
                    [0.5, 2], [0, 1]])

def hat_tiles_algorithm(tile_size, iterations):
    print(f"Hat Tiles Algorithm creating tiles of size {tile_size} using {iterations} iterations.")
    tiles = np.empty((tile_size, tile_size), dtype=object)
    tiles[:] = None

    # Set the center tile randomly
    tiles[tile_size // 2][tile_size // 2] = HAT_TILE.random_rotation()

    # Try to place each subsequent tile
    for _ in range(iterations):
        placed_tile = False
        while not placed_tile:
            empty_tiles = np.argwhere(tiles == None)
            if len(empty_tiles) == 0:
                break
            print(f"Empty Tile count: {len(empty_tiles)}")
            i, j = random.choice(empty_tiles)
            for candidate in [HAT_TILE.random_rotation() for _ in range(4)]:
                matches = 0
                if i > 0 and tiles[i-1][j] is not None:
                    if np.array_equal(tiles[i-1][j][2], candidate[0]):
                        matches += 1
                if j > 0 and tiles[i][j-1] is not None:
                    if np.array_equal(tiles[i][j-1][1], candidate[2]):
                        matches += 1
                if i < tile_size-1 and tiles[i+1][j] is not None:
                    if np.array_equal(tiles[i+1][j][0], candidate[2]):
                        matches += 1
                if j < tile_size-1 and tiles[i][j+1] is not None:
                    if np.array_equal(tiles[i][j+1][3], candidate[1]):
                        matches += 1
                if matches >= 2:
                    tiles[i][j] = candidate
                    placed_tile = True
                    print(f"Placed tile in {i},{j}")
                    break

    return tiles
