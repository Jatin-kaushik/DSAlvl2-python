# class ServiceCenter:
#     ls = ["KA", "Kl", "MA", "UP", "UA", "MP"]
#     sets = set(ls)
    
#     def __init__(self, serviceid, modelname, manufacturer, distancetravelled, insured, payment=0):
#         self.serviceid = serviceid
#         self.modelname = modelname
#         self.manufacturer = manufacturer
#         self.distancetravelled = distancetravelled
#         self.insured = insured
#         self.payment = payment
#     def method1(self, arr, dict1):
#         res = []
#         for i in arr:
#             ans = self.method2(i[0], i[1], i[2], i[3],i[4], 0, dict1)
#             if len(ans) > 5:
#                 res.append(ans)
        
#         if len(res) == 0:
#             print("No car found with given criteria")
#         else:
#             for i in res:
#                 print(i)
            
#     def method2(self, serviceid, modelname, manufacturer, distancetravelled, insured, payment, dict1):
#         res = []
#         if dict1[serviceid] not in self.sets:
#             return None
#         if self.distancetravelled >5000:
#             if self.insured =="yes":
#                 self.payment = 1000
#             else:
#                 self.payment = 1750
#             res = str(self.serviceid) + " " + self.modelname + " " + manufacturer +" " + str(self.payment)
#         else:
#             return 0
    
    
    
# n = int(input())
# arr = []
# dict1 = {}
# for i in range(n):
#     sid = int(input())
#     model = input()
#     manu = input()
#     dist = int(input())
#     insured = input()
#     registration = input()
#     ls = [sid, model, manu, dist, insured]
#     dict1[sid] = registration
#     arr.append(ls)
# ob1 = ServiceCenter()
# ob1.method1(arr, dict1)

#
n = int(input())

dict1 = {}

for i  in range(n):
    sid = int(input())
    model = input().lower()
    manu = input().lower()
    dist = int(input())
    insured = input().lower()
  
    if insured == "yes":
        minpayment = 1000
    else:
        minpayment  = 1750
    
    state =  input().upper()
    if state not in dict1:
        dict1[state] = [[sid,model,manu,dist,insured,minpayment]]
    else:
         dict1[state].append([sid,model,manu,dist,insured,minpayment])
    
    
    
resarr = []
state_to_query = input().upper()
if state_to_query in dict1:
    output_states = dict1[state_to_query]
    for sid,model,manu,dist,insured,minpayment in output_states:
        if dist>5000:
            resarr.append(f"{sid} {model} {manu} {minpayment}")
    
if len(resarr) >0:
    for i in resarr:
        print(i)
else:
    print("No car found with given criteria")
    
    
    
    
     