# Sample input:
# [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# ['9:00', '20:00']
# [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# ['10:00', '18:30']
# 30
# Sample output: [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

# Assumptions / Questions?
# * Can we assume the array is sorted?
# * Are the arguments valid non-null strings?
# * Is there a limitation/slot for the duration of the meeting? (min duration 15 min, 30 min slots, etc)
# * Military time and string
# * You can schedule a meeting right at the end of another one (12:30 - 13:00 and 13:00 - 13:30)

# First iteration
# 1. A method to get the free slots of each calendar
# free_slots_1 = [['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']]
# free_slots_2 = [['11:30', '12:30'], ['15:00', '16:00'], ['17:00', '18:30']]

# class Solution:
#     def to_time(self, str_array):
#         pass

#     def to_str(self, time_array):
#         pass

#     def get_free_slots(self, calendar, bounds): # List<List<String>>
#         free_slots = []
#         start_of_day, end_of_day = to_time(bounds)

#         last_meeting = None
#         for meeting in calendar:
#             start, end = to_time(meeting)
#             if last_meeting is None and start - start_of_day > 0:
#                 free_slots.append(start - start_of_day)
#             else:
#                 last_meeting_start, last_meeting_end = to_time(meeting)
#                 if last_meeting_end - start > 0:
#                     free_slots.append(last_meeting_end - start)
#             last_meeting = meeting

#         # Checking last meeting against bound
#         start, end = to_time(last_meeting)
#         if end_of_day - end > 0:
#             free_slots.append(end_of_day - end)
        
#         return free_slots

#     def get_available_slots(self, calendar1, bounds1, calendar2, bounds2, duration):
#         free_slots_cal1 = self.get_free_slots(calendar1, bounds1)
#         free_slots_cal2 = self.get_free_slots(calendar2, bounds2)

#         for s1 in free_slots_cal1:
#             start1, end1 = to_time(s1)
#             for s2 in free_slots_cal2:
#                 start2, end2 = to_time(s2)

#                 if start2 < end1:
                    
# Second iteration
# Assuming the minimun resolution of time is 1 min
# 0. Convert calendars to array of booleans of 1440 elements (each element is a free minute) and
# mark minutes outside of bound as not available
# 2. Iterate from 0 to 1339 and return true only if the element of each array is true (free for both)
# 3. Convert the indices to hours
# 

class Solution:
    def str_time_to_index(self, str_time):
        hours, minutes = str_time.split(':')
        return (int(hours) * 60) + int(minutes)

    def index_to_str_time(self, index):
        hours = index // 60
        minutes = index % 60
        return f'{hours:02}:{minutes:02}'

    def get_calendar_array(self, meetings, bounds):
        calendar = [0] * 1440
        start_of_day = self.str_time_to_index(bounds[0])
        end_of_day = self.str_time_to_index(bounds[1])
        # mark as busy before start of bounds
        for i in range(0, start_of_day):
            calendar[i] = 1

        # mark meetings as busy
        for m in meetings:
            start = self.str_time_to_index(m[0])
            end = self.str_time_to_index(m[1])
            for i in range(start, end):
                calendar[i] = 1
            
        # mark as busy after end of bounds
        for i in range(end_of_day, 1440):
            calendar[i] = 1

        return calendar

    def get_available_slots(self, calendar1, bounds1, calendar2, bounds2, duration):
        cal_arr_1 = self.get_calendar_array(calendar1, bounds1)
        cal_arr_2 = self.get_calendar_array(calendar2, bounds2)

        free_slots = []
        open_slot = None
        for i in range(0, 1440):
            if (cal_arr_1[i] == 0 and cal_arr_2[i] == 0):
                if open_slot is None:
                    open_slot = i
            else:
                if open_slot is not None:
                    free_slots.append([open_slot, i])
                    open_slot = None

        return [[self.index_to_str_time(p[0]), self.index_to_str_time(p[1])] for p in filter(lambda x: x[1] - x[0] >= duration, free_slots)]

        

if __name__ == "__main__":
    s = Solution()
    print(s.get_available_slots(
        [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']],
        ['9:00', '20:00'],
        [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']],
        ['10:00', '18:30'],
        30
    ))