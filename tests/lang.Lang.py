import sys; sys.path.insert(0, "..")
import pgt
import time

start_time = time.perf_counter_ns()
lang = pgt.lang.load("test_files/speed_test.lang")
print(time.perf_counter_ns() - start_time)
print(lang.get("set1_l1.attr1_set1_l1"))
print("---")
print(lang.get("set1_l1.set1_l2_under_set1_l1.attr1_set1_l2_under_set1_l1"))
print("---")
print(lang.get("set1_l1.attr2_set1_l1"))
print("---")
print(lang.get("set2_l1.attr1_set2_l1"))
