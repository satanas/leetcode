from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def overlapping(intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(len(intervals) - 1):
        if intervals[i + 1].start <= intervals[i].end:
            return True
    return False

if __name__ == "__main__":
    print(overlapping([Interval(1,4), Interval(2,5), Interval(7,9)]))
    print(overlapping([Interval(6,7), Interval(2,4), Interval(9, 11)]))
    print(overlapping([Interval(1,4), Interval(2,6), Interval(3,5)]))
    print(overlapping([Interval(1,2), Interval(11, 14), Interval(3,5), Interval(6, 8)]))