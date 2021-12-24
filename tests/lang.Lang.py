import sys; sys.path.insert(0, "..")
import pgt
import time

LANG = pgt.Lang()

start_time = time.perf_counter()
LANG.load("test_files/lang_test.lang")
print(time.perf_counter() - start_time)
print(LANG.get("set1_l1.attr1_set1_l1"))
print("---")
print(LANG.get("set1_l1.set1_l2_under_set1_l1.attr1_set1_l2_under_set1_l1"))
print("---")
print(LANG.get("set1_l1.attr2_set1_l1"))
print("---")
print(LANG.get("set2_l1.attr1_set2_l1"))
