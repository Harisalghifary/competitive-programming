# Difficulty : Easy
# Tag : Math, Simulation
def passThePillow(self, n: int, time: int) -> int:
#         pos = 1
#         reverse = False
#         timer = 0
#         while timer < time:
#             if pos==1:
#                 reverse = False
#             elif pos==n:
#                 reverse = True
        
#             if reverse:
#                 pos-=1
#             else:
#                 pos+=1
#             timer+=1
    
#         return pos
    # determine when forward or backward
    piece = time // (n-1) 

    return time % (n-1) +1 if piece%2==0 else n - time % (n-1)
