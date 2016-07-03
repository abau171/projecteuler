def deterministic(func):
    result_cache = dict()
    def wrapper(*args, **kwargs):
        key = repr(args) + repr(kwargs)
        if key in result_cache:
            return result_cache[key]
        else:
            result = func(*args, **kwargs)
            result_cache[key] = result
            return result
    return wrapper

def _gen_or_cache(gen, gen_cache):
    i = 0
    while True:
        if i < len(gen_cache):
            yield gen_cache[i]
        else:
            next_result = next(gen)
            gen_cache.append(next_result)
            yield next_result
        i += 1

def deterministic_gen(func):
    gen_caches = dict()
    def wrapper(*args, **kwargs):
        key = repr(args) + repr(kwargs)
        if key in gen_caches:
            gen, gen_cache = gen_caches[key]
        else:
            gen = func(*args, **kwargs)
            gen_cache = []
            gen_caches[key] = (gen, gen_cache)
        return _gen_or_cache(gen, gen_cache)
    return wrapper

