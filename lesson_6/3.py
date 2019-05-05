
import random

@profile
def get_sum_between_min_max_2(a):
    min_pos = a.index(min(a))
    max_pos = a.index(max(a))

    if min_pos < max_pos:
        return sum(a[min_pos + 1:max_pos])
    else:
        return sum(a[max_pos + 1:min_pos])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    get_sum_between_min_max_2(a)        


# $ python -m memory_profiler 3.py
# Filename: 3.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#      4   14.410 MiB   14.410 MiB   @profile
#      5                             def get_sum_between_min_max_2(a):
#      6   14.410 MiB    0.000 MiB       min_pos = a.index(min(a))
#      7   14.410 MiB    0.000 MiB       max_pos = a.index(max(a))
#      8
#      9   14.410 MiB    0.000 MiB       if min_pos < max_pos:
#     10                                     return sum(a[min_pos + 1:max_pos])
#     11                                 else:
#     12   14.410 MiB    0.000 MiB           return sum(a[max_pos + 1:min_pos])
