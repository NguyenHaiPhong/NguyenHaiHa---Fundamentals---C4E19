number_of_bacteria_B = int(input("How many B bacterias are there? "))
times = int(input("How much time in minutes will we wait? "))
for i in range(1, times, 2):
    number_of_bacteria_B *= 2    
print("After {0} minutes, we would have {1} bacteria(s).".format(times, number_of_bacteria_B))