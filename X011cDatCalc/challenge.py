import time
# help(time.time())
# help(time.perf_counter())
# help(time.monotonic())
# help(time.process_time())

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
