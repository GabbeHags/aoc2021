import cProfile
import pstats


def profile_func(func):
    def inner():
        profiler = cProfile.Profile()
        profiler.enable()
        result = func()
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        return result

    return inner
