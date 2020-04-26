import time

# find GHJK in different digits where GH % JK == 0
start = time.time()
listGHJK = []
for number in range(1023,9877):
    if len(set(list(map(int,str(number)))))<4: continue            
    gh = number // 100
    jk = number % 100
    if jk > 9 and gh % jk == 0:
        # print(gh,jk)
        listGHJK.append(number)
                    
print(f"Found {len(listGHJK)} combinations of GH/JK in {'%.3f'%((time.time()-start)*1000)} ms: \n{listGHJK}") # print with Python 3 parameter mode

# find ABCDEFGHJK in different digits where AB * CD + EF - GH / JK = 2020
start = time.time()
combination = solution = 0
target = 2020
for abcdef in range(102345,987655):
    d6 = list(map(int,str(abcdef))) # convert number to a list of digits
    if len(d6) != len(set(d6)): continue # duplicate digit in abcdef
    for ghjk in listGHJK:
        d4 = list(map(int,str(ghjk))) # convert number to a list of digits
        if len(set(d4) & set(d6))>0: continue # abcdef duplicates digit with ghjk
        combination += 1
        ab = abcdef // 10000
        cd = abcdef // 100 % 100
        ef = abcdef % 100
        gh = ghjk // 100
        jk = ghjk % 100
        if ab*cd+ef-gh/jk == target:
            solution += 1
            print("No.%d: %02dx%02d+%02d-%02d/%02d=%d" % (solution,ab,cd,ef,gh,jk,target)) # traditional string format 1
    
print("Found {} solutions in {} combinations with {} s.".format(solution,combination,format(time.time()-start,'.3f'))) # traditional string format 2
   