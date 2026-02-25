    # Difference Array Technique
    # Calculate seats booked for each flight
    # Time: O(n), Space: O(n)

def corp_flight_bookings(bookings, n):
    flight=[0]*n
    for start,end,seats in bookings:
        flight[start-1]+=seats
        if end<n:
            flight[end]-=seats
    for i in range(1,n):
        flight[i]+=flight[i-1]

    return flight

n = 6
bookings = [
  [1, 2, 10],
  [3, 4, 20],
  [5, 6, 30]
]

print(corp_flight_bookings(bookings,n))