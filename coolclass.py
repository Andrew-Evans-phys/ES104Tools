def scarymath(start, speed, time):
    end = start+speed*time-4.9*time*time
    print(end, "meters from start")
    return end

position = int(input("start height in meters: "))
velocity = int(input("start speed in meters per second: "))
t = int(input("total fall time in seconds: "))

scarymath(position, velocity, t)