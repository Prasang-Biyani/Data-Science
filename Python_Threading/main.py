import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(id_func):
    print('do_something ' ,id_func)
    time.sleep(id_func)
    return 'Done Sleeping for id ' + str(id_func)

# do_something()
# do_something()

# threads = []
# for i in range(10):
#     t = threading.Thread(target=do_something, args=[i])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# with concurrent.futures
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # f1 = executor.submit(do_something, 1)
#     # print(f1.result())
#     results = [executor.submit(do_something, i) for i in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')


