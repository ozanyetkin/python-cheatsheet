

# Run the test harness provided for precision clock
#TEST 1
if str(PrecisionClock(23,32)) == "23:32:00":
    print("Test 1 PASSED")
else:
    print("Test 1 FAILED")

#TEST 2
tmp = PrecisionClock(23,30,23)
[tmp.tick() for i in range(10)]
if str(tmp) == "23:30:33":
    print("Test 2 PASSED")
else:
    print("Test 2 FAILED")

#TEST 3
tmp = PrecisionClock(23,32)
tmp.tick()
if str(tmp) == "23:32:01":
    print("Test 3 PASSED")
else:
    print("Test 3 FAILED")

#TEST 4
tmp = PrecisionClock(0,59,59)
tmp.tick()
if str(tmp) == "01:00:00":
    print("Test 4 PASSED")
else:
    print("Test 4 FAILED")

#TEST 5
tmp = PrecisionClock(12,59,59)
tmp.tick()
if str(tmp) == "13:00:00":
    print("Test 5 PASSED")
else:
    print("Test 5 FAILED")
    
#TEST 6
if PrecisionClock(15,2.0,"32") == PrecisionClock(15,"2",32):
    print("Test 6 PASSED")
else:
    print("Test 6 FAILED")

#TEST 7
if PrecisionClock(15,3,"32") != PrecisionClock(15,2,32):
    print("Test 7 PASSED")
else:
    print("Test 7 FAILED")
    
#TEST 8
if PrecisionClock(22,23,0) != PrecisionClock(22,23,1):
    print("Test 8 PASSED")
else:
    print("Test 8 FAILED")

#TEST 9
if Clock(15,2) == PrecisionClock(15,"2",32):
    print("Test 9 PASSED")
else:
    print("Test 9 FAILED")

#TEST 10
if PrecisionClock(18,24,32) == Clock(18,24):
    print("Test 10 PASSED")
else:
    print("Test 10 FAILED")

#TEST 11
if Clock(18,56) != PrecisionClock(18,53,32):
    print("Test 11 PASSED")
else:
    print("Test 11 FAILED")
    
#TEST 12
if PrecisionClock(22,44,13) != Clock(23,44):
    print("Test 12 PASSED")
else:
    print("Test 12 FAILED")

#TEST 13
try:
    tmp = PrecisionClock(-1,23,1)
    print("Test 13 FAILED")
except ValueError:
    print("Test 13 PASSED")
except:
    print("Test 13 FAILED")
    
#TEST 14
try:
    tmp = PrecisionClock(12,-23,1)
    print("Test 14 FAILED")
except ValueError:
    print("Test 14 PASSED")
except:
    print("Test 14 FAILED")
    
#TEST 15
try:
    tmp = PrecisionClock(12,23,-1)
    print("Test 15 FAILED")
except ValueError:
    print("Test 15 PASSED")
except:
    print("Test 15 FAILED")
    
#TEST 16
try:
    tmp = PrecisionClock("dsaf",23,1)
    print("Test 16 FAILED")
except ValueError:
    print("Test 16 PASSED")
except:
    print("Test 16 FAILED")
  
#TEST 17
try:
    tmp = PrecisionClock(12,"riidid",1)
    print("Test 17 FAILED")
except ValueError:
    print("Test 17 PASSED")
except:
    print("Test 17 FAILED")
    
#TEST 18
try:
    tmp = PrecisionClock(12,23,"sdcs")
    print("Test 18 FAILED")
except ValueError:
    print("Test 18 PASSED")
except:
    print("Test 18 FAILED")
    
#TEST 19
try:
    tmp = PrecisionClock(12,23,75)
    print("Test 19 FAILED")
except ValueError:
    print("Test 19 PASSED")
except:
    print("Test 19 FAILED")
    
#TEST 20
try:
    tmp = PrecisionClock(12,62,34)
    print("Test 20 FAILED")
except ValueError:
    print("Test 20 PASSED")
except:
    print("Test 20 FAILED")
    
#TEST 21
try:
    tmp = PrecisionClock(26,23,5)
    print("Test 21 FAILED")
except ValueError:
    print("Test 21 PASSED")
except:
    print("Test 21 FAILED")
