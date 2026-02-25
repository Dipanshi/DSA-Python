    # Check if car can complete all trips
    # Time: O(n + max_location), Space: O(max_location)
    
def car_pooling(trips, capacity):
    max_location=max(trip[2] for trip in trips)
    pool=[0]*max_location
    for passenger,fro,to in trips:
        pool[fro-1]+=passenger
        pool[to-1]-=passenger

    for i in range(1,max_location):
        pool[i]+=pool[i-1]
        if pool[i]>capacity:
            return False
        
    return True



# trips = [[2, 1, 5],[3, 3, 7]]
# capacity = 5
# trips = [[2, 1, 5],[3, 3, 7]]
# capacity = 4
# trips = [[3, 2, 5],[4, 6, 8]]
# capacity = 4
# trips = [[4, 2, 6],[3, 4, 7],[2, 5, 8]]
# capacity = 7
# trips = [[5, 1, 5],[3, 5, 7]]
# capacity = 5
trips = [
  [3, 1, 4],
  [4, 2, 5]
]
capacity = 6

print(car_pooling(trips,capacity))