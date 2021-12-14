from heap import *

length = 8
values = [18, 6, 7, -3, 44, 10, 6]

heap = MinHeap(length)

num_tests_passed = 0
num_tests_failed = 0
num_tests = 0


print("====================================")
print("PART 1")
print("Initializing with values", values)
print("====================================")

print("====================================")
print("Test Case 1")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == [None, None, None, None, None, None, None, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 2")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

if heap.get_heap_array() == [-3, 6, 6, 18, 44, 10, 7, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 3")
print("Correct Extraction")
print("====================================")

num_tests += 1

if heap.extract_min() == -3:
    if heap.get_heap_array() == [6, 7, 6, 18, 44, 10, None, None]:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")
    num_tests_failed += 1

print()

length = 8
values = [3, 3, 8, 6, 4, 2, 8, 1]

print("====================================")
print("PART 2")
print("Initializing with values", values)
print("====================================")


heap = MinHeap(length)

print("====================================")
print("Test Case 4")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == [None, None, None, None, None, None, None, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 5")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

if heap.get_heap_array() == [1, 2, 3, 3, 4, 8, 8, 6]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 6")
print("Correct Extraction")
print("====================================")

num_tests += 1

if heap.extract_min() == 1:
    if heap.get_heap_array() == [2, 3, 3, 6, 4, 8, 8, None]:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")
    num_tests_failed += 1

print()

length = 8
values = [None, None, None, None, None, None, None, None]

print("====================================")
print("PART 3")
print("Initializing with values", values)
print("====================================")


heap = MinHeap(length)

print("====================================")
print("Test Case 7")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == [None, None, None, None, None, None, None, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 8")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

if heap.get_heap_array() == [None, None, None, None, None, None, None, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 9")
print("Correct Extraction")
print("====================================")

num_tests += 1

if heap.extract_min() == None:
    if heap.get_heap_array() == values:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")
    num_tests_failed += 1

print()

length = 8
values = [3, 3, 8, 6, 4, 2, 8, 1, 9]

print("====================================")
print("PART 4")
print("Initializing with values", values)
print("====================================")


heap = MinHeap(length)

print("====================================")
print("Test Case 10")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == [None, None, None, None, None, None, None, None]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 11")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

if heap.get_heap_array() == [1, 2, 3, 3, 4, 8, 8, 6]:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 12")
print("Correct Extraction")
print("====================================")

num_tests += 1

if heap.extract_min() == 1:
    if heap.get_heap_array() == [2, 3, 3, 6, 4, 8, 8, None]:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")
    num_tests_failed += 1

print()

length = 0
values = [3, 3, 8, 6, 4, 2, 8, 1, 9]

print("====================================")
print("PART 5")
print("Initializing with values", values)
print("====================================")


heap = MinHeap(length)

print("====================================")
print("Test Case 13")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == []:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 14")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

if heap.get_heap_array() == []:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 15")
print("Correct Extraction")
print("====================================")

num_tests += 1

if heap.extract_min() == None:
    if heap.get_heap_array() == []:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")
    num_tests_failed += 1

print()

length = 100
values = [3, 3, 8, 6, 4, 2, 8, 1, 9]

print("====================================")
print("PART 6")
print("Initializing with values", values)
print("====================================")


heap = MinHeap(length)

print("====================================")
print("Test Case 16")
print("Correct Initialization")
print("====================================")

num_tests += 1

if heap.get_heap_array() == [None] * length:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    num_tests_failed += 1

print()

print("====================================")
print("Test Case 17")
print("Correct Insertion")
print("====================================")

num_tests += 1

for value in values:
    heap.insert(value)

test_array = [1, 2, 3, 3, 4, 8, 8, 6, 9]

for i in range(length - len(test_array)):
    test_array.append(None)

if heap.get_heap_array() == test_array:
    print("TEST PASSED")
    num_tests_passed += 1
else:
    print("TEST FAILED")
    print("Array Returned:")
    print(heap.get_heap_array())
    num_tests_failed += 1
    print()
    print("Correct Array:")
    print(test_array)

print()



print("====================================")
print("Test Case 18")
print("Correct Extraction")
print("====================================")

num_tests += 1

test_array = [2, 3, 3, 6, 4, 8, 8, 9, None]

for i in range(length - len(test_array)):
    test_array.append(None)

if heap.extract_min() == 1:
    if heap.get_heap_array() == test_array:
        print("TEST PASSED")
        num_tests_passed += 1
    else:
        print("TEST FAILED: Incorrect array output")
        print("Your array:")
        print(heap.get_heap_array())
        print("Correct array:")
        print(test_array)
        num_tests_failed += 1
        num_tests_failed += 1
else:
    print("TEST FAILED: Incorrect value output")

print()


print("====================================")
print("SUMMARY")
print("====================================")

print("Total Tests:", num_tests)
print("Total Tests Passed: {}/{}".format(num_tests_passed, num_tests))
print("Total Tests Failed: {}/{}".format(num_tests_failed, num_tests))


