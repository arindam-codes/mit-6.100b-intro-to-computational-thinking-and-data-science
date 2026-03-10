# since the problem contains only 5 variables so total cases to search is 
# 2^5 32 cases so we can apply brute force method safely



def best_score():
    
    best_scores = 0
    best_choice = None
    F = 1

    ps1 = 6
    ps2 = 7
    ps3 = 8
    ps4 = 9
    ps5 = 10
        
    for a in [0, 10]:
        for b in [0, 10]:
            for c in [0, 10]:
                for d in [0, 10]:
                    for e in [0, 10]:
                        
                        score = ((60 - (a+b+c+d+e))*F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5)
                
                        if score > best_scores and a + b + c + d + e >= 20:
                            best_scores = score
                            best_choice = (a, b, c, d, e)
        
    return best_choice, best_scores

var, score = best_score()
print(var, score)
