#wap to find profit and profit % when bought 10 quantities 
# pens at Rs.27 and sold them for Rs.43


cp,sp,qty= 27,43,10
profit = (sp-cp)*qty
print ("profit: ",profit)
profit_percent = profit/(cp*qty)*100
print(f"profit_percent: {profit_percent:.2f}")
