'''
@Author: Rahul
@Date: 2024-07-27
@Last Modified by: Rahul
@Last Modified: 2024-07-27
@Title: Demonstration of StopWatch
'''

import time
class StopWatch:
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.elapsed_time = 0
        self.paused_time = None
        self.is_paused = False

    def start(self):
        """
        Description: 
            Function to demonstrate a start function of the stopwatch.
        parameters:
            None    
        Returns:
            None
        """
        if self.start_time is None:
            self.start_time = time.time()
            self.is_paused = False
            print("StopWatch Started")
        elif self.is_paused:
            self.start_time = time.time() - self.elapsed_time
            self.is_paused = False
            print("StopWatch Resumed")
        else:
            print("StopWatch is already running.")

    def stop(self):
        """
        Description: 
            Function to demonstrate stop function of the stopwatch and calculate elapsed time.
        Parameters:
            None    
        Returns:
            None
        """
        if self.start_time is not None and not self.is_paused:
            self.stop_time = time.time()
            self.elapsed_time = self.stop_time - self.start_time
            self.start_time = None
            print(f"StopWatch Stopped. Elapsed time: {self.elapsed_time:.2f} seconds")
        elif self.is_paused:
            print(f"StopWatch Stopped. Elapsed time: {self.elapsed_time:.2f} seconds")
            self.is_paused = False
            self.start_time = None
        else:
            print("StopWatch is not running.")

def main():
    stopwatch = StopWatch()
    while True:
        watch = int(input("PRESS 1. START  2. STOP 3. EXIT\n"))
        if watch == 1:
            stopwatch.start()
        elif watch == 2:
            stopwatch.stop()
        elif watch == 3:
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
