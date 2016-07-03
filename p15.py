from utils import cache

@cache.deterministic
def grid_routes(width, height):
    if width == 0 and height == 0:
        return 1
    else:
        num_routes = 0
        if width > 0:
            num_routes += grid_routes(width - 1, height)
        if height > 0:
            num_routes += grid_routes(width, height - 1)
        return num_routes

print(grid_routes(20, 20))

