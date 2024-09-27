from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        # Initialize a SortedDict to keep track of booking times.
        # Keys are the start or end of an event, and values are the net number
        # of events starting or ending at that time.
        self.booking_counts = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # Increment the count for the start time of the new event.
        self.booking_counts[start] = self.booking_counts.get(start, 0) + 1
        # Decrement the count for the end time of the new event.
        self.booking_counts[end] = self.booking_counts.get(end, 0) - 1

        # Initialize a running sum to track number of simultaneous events.
        running_sum = 0

        # Iterate over all booked time points (both start and end times).
        for count in self.booking_counts.values():
            # Update the running sum which represents the count of current
            # overlapping events at the current time.
            running_sum += count

            # If there are more than 2 simultaneous events, it's a conflict.
            if running_sum > 2:
                # Revert the increment and decrement for the start and end time.
                self.booking_counts[start] -= 1
                self.booking_counts[end] += 1
                # Return False indicating the booking was unsuccessful.
                return False

        # If no conflicts were found, return True indicating successful booking.
        return True

# Example usage of the MyCalendarTwo class:
# calendar = MyCalendarTwo()
# if calendar.book(10, 20):
#     print("Booking from 10 to 20 is successful.")
# else:
#     print("Booking from 10 to 20 is unsuccessful.")
