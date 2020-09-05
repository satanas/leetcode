# Store the events in an array in a sorted-fashion way
# We could have an array with intervals already double booked

# On insertion, we check the interval against the double booked
# If we detect an intersection there we return False
# Otherwise, we check the existing arrays for possible intersections
# If there are intersections, then we add the resulting interval to the double booked array
# Otherwise, we just add the requested interval to the list of events
# Finally, we return True

# [a ======== b]
# [a === c]
#    [d ==== b]
#  [e == f]
#                 [h ===== g]

class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.double_booked = []

    def book(self, start, end):
        if end < start:
            return False
        
        new_interval = [start, end]
        print("=== Checking double bookings")
        if len(self.check_intersection(self.double_booked, new_interval)) > 0:
            return False

        print("=== Checking events")
        intersections = self.check_intersection(self.events, new_interval)
        if len(intersections) > 0:
            for i in intersections:
                self.double_booked = self.add_interval_sorted(self.double_booked, i)
        
        self.events = self.add_interval_sorted(self.events, new_interval)
        print(f"====== Events: {self.events}")
        return True

    def add_interval_sorted(self, events, interval):
        events.append(interval)
        return sorted(events, key=lambda a: a[0])

    def check_intersection(self, events, interval): # return empty interval is no intersection, or new intersected interval
        results = []
        print(f"Events: {events} - interval: {interval}")
        for ev in events:
            if interval[0] >= ev[1] or interval[1] <= ev[0]:
                continue
            print(f"Evaluating {ev} against {interval}")
            start = max(interval[0], ev[0])
            end = min(interval[1], ev[1])
            results.append([start, end])
        print(f"Intersections: {results}")
        return results
        




if __name__ == "__main__":
    m = MyCalendarTwo()
    # print(m.book(10, 20)); # returns True
    # print(m.book(50, 60)); # returns True
    # print(m.book(10, 40)); # returns True
    # print(m.book(5, 15)); # returns False
    # print(m.book(5, 10)); # returns True
    # print(m.book(25, 55)); # returns True

    response = []
    for n in [[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]:
        if len(n) == 0:
            response.append(None)
        else:
            response.append(m.book(n[0], n[1]))
        #input()

    #print(response)

    expected = [None,True,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False]
    assert(response == expected)

# [null,true,true,true,true,true,true,true,true,false,false,false,false,false,true,false,false,false,true,false,false,false,true,false,false,false,true,true,false,false,false]
# [null,true,true,true,true,true,true,true,true,false,false,false,false,false,true,false,false,false,true,false,false,false,false,false,false,false,false,true,false,false,false]
