def elapsed_time_in_minutes (number_of_layers, elapsed_bake_time):
    q = number_of_layers * 2
    return elapsed_bake_time + q


print(elapsed_time_in_minutes(3,20))
