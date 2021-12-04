import cProfile
import pstats


def profile_func(func):
    def inner(*args, **kwargs):
        profiler = cProfile.Profile()
        print(f"Function name: {func.__name__}")
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        return result

    return inner
