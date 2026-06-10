import time      # A PRECISE COUNTDOWN TIMER THAT REDUCES ANY TIME ERROR ACCUMULATION USING time.time()

while True : 
    duration = (input("Enter the Timer Count in seconds: "))
    if not duration.isdigit() :       #  MAKES SURE ONLY WORDS ARE ENTERED
        print(f"Words are not allowed.")
    else: 
        break
x = int(duration)
uniclock = time.time()

for (i) in range(x, 0, -1): 
    seconds = i% 60
    minutes = int(i / 60) % 60
    hours = int( i / 60) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    next_tick= uniclock + (x - i + 1 )  # the update in the uniclock that adds the seconds passed to the uniclock 
    error_in_time = next_tick - time.time() 
    if error_in_time > 0: #makes sure the program runs immediately after a freeze or lag if the lag happens around the ending of countdown
        time.sleep(error_in_time)
print("COUNTDOWN FINISH!")
