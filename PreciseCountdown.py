import time      # A PRECISE COUNTDOWN TIMER THAT REDUCES ANY TIME ERROR ACCUMULATION USING time.time()
duration = int((input("Enter the Timer Count: ")))
uniclock = time.time()

for (i) in range(duration, 0, -1): 
    seconds = i% 60
    minutes = int(i / 60) % 60
    hours = int( i / 60) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    next_tick= uniclock + (duration - i + 1 )  # the update in the uniclock that adds the seconds passed to the uniclock 
    error_in_time = next_tick - time.time() 
    if error_in_time > 0: #makes sure the program runs immediately after a freeze or lag if the lag happens around the ending of countdown
        time.sleep(error_in_time)
print("COUNTDOWN FINISH!")
