def draw_maze(draw_pi,draw_epi,numdata, all_minterm,maze_pi,maze_epi,col_answer,row_answer,
              col_interchange,row_interchange):
    maze = [[ "-" for j in range(numdata+1)] for i in range(len(draw_pi)+1 +len(draw_epi))]
    # row : numdata + 1 col: len(pi)+1
    print('')
    print("---------<<  MAP >>---------")
    print("<<Check Minterm that Pi has>> ")
    
    maze[0][0] = "PI/MIN"
    for i in range(1,len(draw_pi)+1):
        maze[i][0] = "'"+ str(draw_pi[i-1]) + "'"
    for i in range(1,len(draw_epi)+1):
        maze[len(draw_pi)+i][0] = "'"+ str(draw_epi[i-1]) + "'"
    for i in range(1,numdata+1):
        maze[0][i] =  (all_minterm[i-1])
    
    for i in range(1,numdata+1):
        if maze[0][i] > 9  :
            for k in range(1,len(draw_pi)+1+len(draw_epi)):
                maze[k][i] = "- "
    
    for i in range(1,len(draw_pi)+1+len(draw_epi)):
        for k in range(0,len(draw_pi)):
            if maze[i][0] == "'"+draw_pi[k]+"'" :
                draw_list = maze_pi[k]
                for m in range(1,numdata+1):
                    if maze[0][m] in draw_list:
                        if maze[0][m] > 9 > 1 :
                            maze[i][m] = "V "
                        else:
                            maze[i][m] = "V"
        for k in range(0,len(draw_epi)):
            if maze[i][0] == "'"+draw_epi[k]+"'" :
                draw_list = maze_epi[k]
                for m in range(1,numdata+1):
                    if maze[0][m] in draw_list:
                        if maze[0][m] > 9 > 1 :
                            maze[i][m] = "V "
                        else:
                            maze[i][m] = "V"
                        
    for i in range(0,len(maze)):
        for k in range(0,len(maze[i])):
            print(maze[i][k] , end= ' ')
        print('')
        
    for i in range(1,len(draw_pi)+1+len(draw_epi)):
        for k in range(0,len(draw_epi)):
            if maze[i][0] == "'"+draw_epi[k]+"'" :
                for m in range(1, numdata+1) : 
                    if(maze[i][m] == "V" or maze[i][m] == "V "):
                        maze[0][m] = "X"
                        maze[i][0] = "  EPI "
                        
    print('')
    print("---------<<  MAP >>---------")
    print("<<Check EPI>> ")                    
    for i in range(0,len(maze)):
        for k in range(0,len(maze[i])):
            print(maze[i][k] , end= ' ')
        print('')
    
    how_max = 0
    how_max_index = 0
    if(col_interchange != 0 ) and(len(col_interchange) != 0) :
        for i in range(1,len(col_interchange)):
            how = 0
            inter_index = maze[0].index(col_interchange[i])
            for k in range(1,len(draw_pi)+1+len(draw_epi)):
                if maze[inter_index][k] == "V":
                    how += 1
            if how > how_max : 
                how_max = how
                how_max_index = i
    if(how_max_index != 0 ):
        maze[0][how_max_index] = "IC"
    
    
    if(col_answer != 0) and (len(col_answer) >1 ):
        for m in range(1, numdata+1) :
            if (maze[0][m] != "X") and(maze[0][m] not in col_answer) :
                maze[0][m] = "CD"
        print('')
        print("---------<<  MAP >>---------")
        print("<<Check CD>> ")
        for i in range(0,len(maze)):
            for k in range(0,len(maze[i])):
                print(maze[i][k] , end= ' ')
            print('')
    else:
        print('')
        print("<<Check CD>> ")
        print("CD : " + "maze doesn't modify ")
    
    row_index_0 = 0
    row_how_0 = 0
    row_index_1 = 0
    row_how_1 = 0
    if (row_interchange != 0 ) and (len(row_interchange) != 0 ):
        for i in range(0,len(row_interchange)):
            for k in range(1,len(draw_pi)+1+len(draw_epi)):
                if ( maze[k][0] == row_interchange) and(i % 2 == 0):
                    for m in range(1,numdata+1):
                        if maze[k][m] == "V":
                            row_how_0 += 1
                    row_index_0 = k
                else :
                    for m in range(1,numdata+1):
                        if maze[k][m] == "V":
                            row_how_1 += 1
                    row_index_1 = k
                    
            if (row_index_0 != 0 ) and( row_index_1 != 0 ):
                if (row_how_0 > row_how_1):
                    maze[row_index_0][0] = "IR"
                else :
                    maze[row_index_1][0] = "IR"
                row_index_0 = 0
                row_index_1 = 0
                row_how_0 = 0
                row_how_1 = 0
    
    if (row_answer != 0 ) and (len(row_answer) >1 ) :
        for i in range(1,len(draw_pi)+1+len(draw_epi)):
            for k in range(0,len(row_answer)):
                if (maze[i][0] == "'"+str(row_answer[k])+"'" ) and (k % 3 == 1 ):
                    maze[i][0] = "  RD  "
        print('')
        print("---------<<  MAP >>---------")
        print("<<Check RD>> ")
        for i in range(0,len(maze)):
            for k in range(0,len(maze[i])):
                print(maze[i][k] , end= ' ')
            print('')
        
    else : 
        print('')
        print("<<Check RD>> ")
        print("RD : " + "maze doesn't modify ")
        
    print('')
    print("ALL DONE ")
    
def row_dominance(col_pi, row_pi, inter, col_minus_epi):
    row_answer = []
    interchange = []
    
    if(len(col_pi) == 0 or len(row_pi) == 0 ):
        row_dominance_print(row_answer)
        return 0
    
    col_copy = []
    for i in range(0,len(col_pi)):
        pra = []
        
        for k in range(0,len(col_pi[i])):
            if col_pi[i][k] in col_minus_epi:
                a = col_pi[i][k]
                pra.append(a)
        col_copy.append(pra)
    col_pi  = col_copy
    
    for i in col_pi:
        for k in col_pi:
            if (len(i) > len(k)) :
                stay_int = 0
                for m in k:
                    if m not in i:
                        stay_int = 1
                        break
                
                if stay_int == 0:
                    row_answer.append(row_pi[col_pi.index(i)])
                    row_answer.append(row_pi[col_pi.index(k)])
                    row_answer.append(-1)
            if (len(i) == len(k) and (i != k)) :
                stay_int = 2
                for m in k:
                    if m not in i:
                        stay_int = 1
                        break
                        
                if stay_int == 2:
                    row_answer.append(row_pi[col_pi.index(i)])
                    row_answer.append(row_pi[col_pi.index(k)])
                    row_answer.append(-2)
                    interchange.append(row_pi[col_pi.index(i)])
                    interchange.append(row_pi[col_pi.index(k)])
    if(inter == 1):
        return interchange
    row_dominance_print(row_answer)
    
    
    return row_answer

def row_dominance_print(row_answer):
    print("<<RD>>")
    if len(row_answer) == 0 : 
        print("RD doesn't exist")
        return 0
    for i in range(0,len(row_answer)):
        if row_answer[i] == -1 : 
            if(row_answer[i-2].count('2') != 0 ):
                row_answer[i-2] = row_answer[i-2].replace('2','-')
            if(row_answer[i-1].count('2') != 0 ):
                row_answer[i-1] = row_answer[i-1].replace('2','-')
            print("PI ("+ row_answer[i-2] + ") dominantes PI (" + row_answer[i-1] + ")")
        if row_answer[i] == 2 : 
            if(row_answer[i-2].count('2') != 0 ):
                row_answer[i-2] = row_answer[i-2].replace('2','-')
            if(row_answer[i-1].count('2') != 0 ):
                row_answer[i-1] = row_answer[i-1].replace('2','-')
            print("PI ("+ row_answer[i-2] + ") interchangeable PI (" + row_answer[i-1] + ")")
    
def column_dominance(col_minus_epi,col_pi):
    
    answer = []    
    col_stay = []
    interchange= []
    for i in col_minus_epi:
        pra = []
        for k in range(0,len(col_pi)):
            if i in col_pi[k]:
                pra.append(k)
        answer.append(pra)
        
    for i in range(0,len(answer)):
        for k in range(0,len(answer)):
            pra = []
            if len(answer[i]) > len(answer[k]):
                stay_int  = 0
                for m in range(0,len(answer[k])):
                    if answer[k][m] not in answer[i]:
                        stay_int = 1
                        break
                if (stay_int == 0 ):
                    pra.append(k)
                    pra.append(i)
                    pra.append(-1)
            if len(answer[i]) == len(answer[k]):
                if(i == k ):
                    continue
                stay_int  = 2
                for m in range(0,len(answer[k])):
                    if answer[k][m] not in answer[i]:
                        stay_int = 1
                        break
                if (stay_int == 2 ):
                    pra.append(k)
                    pra.append(i)
                    pra.append(-2)
                    interchange.append(pra)
            col_stay.append(pra)
    last = []
    for i in range(0,len(col_stay)):
        if (len(col_stay[i]) != 0):
            last.extend(col_stay[i])
    last = col_dominance_print(last, col_minus_epi)
    return last,interchange
        
def col_dominance_print(last, col_minus_epi):
    print("<<CD>>")
    answer = []
    if (len(last) == 0 ):
        print("CD doesn't exist")
        return answer
    for i in range(0,len(last)):
        if last[i] == -1 :
            col_is_dominated = last[i-2]
            col_dominates = last[i-1]
            print("minterm "+str(col_minus_epi[col_dominates]) +
                  " dominates minterm " + str(col_minus_epi[col_is_dominated]))
            answer.append(col_minus_epi[col_is_dominated])
        if last[i] == -2 :
            col_is_dominated = last[i-2]
            col_dominates = last[i-1]
            print("minterm "+str(col_minus_epi[col_dominates]) +
                  " interchangeable minterm " + str(col_minus_epi[col_is_dominated]))
    return answer
        

def pi_to_min(col_pi):
    answer = []
    for q in col_pi:
        pra = []
        pra.append(q)
        for i in range(0,q.count('2')):
            pra1 = []
            for k in range(0,len(pra)):
                pra1.append(pra[k].replace('2','1',1))
                pra1.append(pra[k].replace('2','0',1))
            pra = []
            pra.extend(pra1)
        answer.append(pra)
    for i in range(0,len(answer)):
        for k in range(0,len(answer[i])):
            answer[i][k] = '0b'+answer[i][k]
            answer[i][k] = int(answer[i][k],2)
    return answer

def col_minus_min(col_epi, real_minterm):
    answer = real_minterm
    for i in range(0,len(col_epi)):
        for k in range(0,len(col_epi[i])):
            if col_epi[i][k] in answer:
                answer.remove(col_epi[i][k])
    return answer

def inttobin(variable, numdata,data):
    for i in range(len(data)) :
        data[i] = bin(data[i])
        if len(data[i]) != variable + 2:
            data[i] = data[i][0:2] + (variable+2-len(data[i]))*"0" + data[i][2:]
    return data

def reuse_premerge(variable,numdata,data):
    pi,nonpi = premerge(variable,numdata,data)
    while (len(nonpi) > 1) :
        pi2,nonpi = premerge(variable,numdata,nonpi)
        pi += pi2
    
    if len(nonpi) == 1:
        pi += nonpi
    pi.sort()
    return pi

def premerge(variable, numdata, data):
    pi = []
    nonpi = []
    realpi = []
    for i in range(0,len(data)):
        for k in range(0,len(data)):
            if (i != k) and (data[i].count("1") - data[k].count("1") == 1):
                a = merge(data[i],data[k])
                if a != -1 :
                    if a not in nonpi:
                        nonpi.append(a)
                    if data[i] not in pi:
                        pi.append(data[i])
                    if data[k] not in pi:
                        pi.append(data[k])
    
    for i in data :
        if i not in pi :
            realpi.append(i)
    return realpi,nonpi

def merge(st1,st2):
    count = 0
    st3 = "0b"
    for i in range(2,len(st1)):
        if st1[i] != st2[i] :
            count += 1
            if (st1[i] == "2") or (st2[i] == "2"):
                return -1
            else:
                st3 += "2"
        else:
            st3 += st1[i]
    if count != 1 :
        return -1
    else:
        return st3


def output(variable,pi):
    for i in range(len(pi)):

        pi[i]=pi[i].replace("2","-",variable)
    return pi

def epi(variable,numdata,data,pi):
    data = data
    pi_epi = pi
    pi2 = []
    for i in range(0,len(data)):
        data[i] = data[i][2:]
    data = data + data
    for j in range(0,len(pi_epi)):
        pi_epi[j] = pi_epi[j][2:]
        pi3 = epicut(pi_epi[j])
        pi2.append(pi3)
        for q in range(0,len(pi3)):
            if pi3[q] in data:
                data.remove(pi3[q])
    epi_index = []
    for i in data :
        for k in range(0,len(pi2)):
            if (i in pi2[k])and (k not in epi_index):
                epi_index.append(k)
    epi = []
    for i in epi_index :
        epi.append(pi_epi[i])
    return epi

def epicut(pi):
    a = []
    a+=aaa(pi)
    if "2" not in pi :
        a.append(pi)
    else:
        for i in range(1,pi.count("2")):
            for k in range(0,len(a)):
                a += aaa(a[k])
    answer = []
    for i in a:
        answer.append(i)
        if "2" in i:
            answer.remove(i)
    return answer

def aaa(st1):
    a= []
    for i in range(0,len(st1)):
        if st1[i] == "2":
            a.append(st1[0:i]+"0"+st1[i+1:])
            a.append(st1[0:i]+"1"+st1[i+1:])
            return a
        
def solution(minterm):
    all_minterm = minterm[2:]
    real_minterm = minterm[2:]
    variable = minterm[0]
    numdata = minterm[1]
    data = minterm[2:]
    data = inttobin(variable,numdata,data)
    pi = reuse_premerge(variable,numdata,data)
    answer = []
    epi_list = epi(variable,numdata,data,pi)
    # column dominance--------------
    row_pi = []
    col_pi = []
    col_epi = []
    for i in pi :
        col_pi.append(i)
        row_pi.append(i)
    for i in epi_list:
        col_pi.remove(i)
        row_pi.remove(i)
    for i in epi_list:
        col_epi.append(i)
    
    col_pi = pi_to_min(col_pi) #pi -> minterm
    col_epi = pi_to_min(col_epi)
    maze_pi = col_pi
    maze_epi = col_epi
    col_minus_epi = col_minus_min(col_epi,real_minterm)
    col_answer,col_interchange = column_dominance(col_minus_epi,col_pi)
    # ------------------------------
    #row dominance------------------
    row_answer = row_dominance(col_pi,row_pi,0 , col_minus_epi)
    row_interchange = row_dominance(col_pi,row_pi,1, col_minus_epi)
    #-------------------------------
    
    epi_list = output(variable,epi_list)
    pi = output(variable,pi)
    draw_pi = pi
    draw_epi = epi_list
    
    for i in draw_epi :
        if i in pi : 
            draw_pi.remove(i)
    
    draw_maze(draw_pi,draw_epi,numdata,all_minterm,maze_pi,maze_epi,col_answer,row_answer,
              col_interchange,row_interchange)
    answer.extend(pi)
    answer.append("EPI")
    answer.extend(epi_list)
    
    print("")
    print("")
    print(answer)
    print("")
    print("")
