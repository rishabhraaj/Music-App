import random
# ******************* FOR GENERATING NUMERIC OTP *******************
def randomnumber():
    num=random.randrange(1000,9999)
    return num

# ******************* FOR GENERATING ALPHA NUMBERIC OTP ****************
# def randomalphanum():
#     charvalue="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     s=""
#     for i in range(1,5):
#         index=random.randrange(0,36)
#         s=s+charvalue[index]
#     retur     n s