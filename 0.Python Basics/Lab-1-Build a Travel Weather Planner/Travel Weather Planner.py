"""
Travel Weather Planner

Determines whether commuting is possible based on:
- Distance to travel
- Weather conditions
- Available transportation options
"""

distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True


# Handle invalid or zero distance
if not distance_mi:
    print(False)

# Short distance (≤ 1 mile)
elif distance_mi <= 1:
    print(not is_raining)

# Medium distance (1–6 miles)
elif distance_mi <= 6:
    print(has_bike and not is_raining)

# Long distance (> 6 miles)
else:
    print(has_car or has_ride_share_app)