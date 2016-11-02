input = "a0 a1 a2 a3"
generator = " 1G 2G 3G"

'''
# Script for CLC

for i in range(4,31):
	print "\n//clc %d"%(i+1)
	finalAddition = ""
	print "Xc%d"%(i+1) + "and0 " + "P%d "%(i) + "G%d "%(i-1) + "c%dc0 "%(i+1) + "and2"
	finalAddition += "c%dc0 "%(i+1)
	counter = 0
	# for j in range(4,i+1):
	for k in range(0,i-2):
		toAdd = ""
		counter += 1
		for l in range(2+(k+1)*3,-1,-1):
			# print "i is : %d      k is : %d      l is : %d" %(i,k,l)
			# print "l end\n"
			toAdd += generator[l] 
			# print toAdd
			# print l
		# print "to add is : " + toAdd
		print "Xc%d"%(i+1) + "and%d "%(k+1) + "P[%d:%d] "%(i,i-counter) + "G%d "%(i-counter-1) + "c%dc%d "%(i+1,k+1) + "and%d"%(k+3)
		previousK = k
		finalAddition += "c%dc%d "%(i+1,k+1)
	generator += " %dG"%(i)
	# print generator
	toAddForLastAnd = ""
	for j in range(i+1,1,-1):
		toAddForLastAnd += "P%d "%(j-1) 
	print "Xc%dand%d "%(i+1,i-1) + toAddForLastAnd + "G0 c%dc%d "%(i+1,previousK+2) + "and%d"%(previousK+4)
	finalAddition += "c%dc%d "%(i+1,previousK+2)
	print "Xc%dand%d "%(i+1,i) + "P[%d:0] ALUFN0 "%(i) + "c%dc%d "%(i+1,previousK+3) + "and%d"%(previousK+5)
	finalAddition += "c%dc%d "%(i+1,previousK+3)
	print "Xc%dor G%d "%(i+1,i) + finalAddition + "C%d "%(i+1) + "or%d"%(i+2)
	# print "Xc%dsum A%d XB%d C%d S%d xor3"%(i+1,i+1,i+1,i+1,i+1)
	print "Xc%dclc Ap%d XB%d C%d G%d P%d S%d CLC"%(i+1,i+1,i+1,i+1,i+1,i+1,i+1)

# test = ""
# for i in range(0,6):
# 	test += generator[-(i+1)]
# print test

# Test Cases to check against

# Xc1and0 P0 ALUFN0 c1c0 and2
# Xc1or G0 c1c0 C1 or2

# Xc2and0 P1 G0 c2c0 and2
# Xc2and1 P1 P0 ALUFN0 c2c1 and3
# Xc2or G1 c2c0 c2c1 C2 or3

# Xc3and0 P2 G1 c3c0 and2
# Xc3and1 P2 P1 G0 c3c1 and3
# Xc3and2 P2 P1 P0 ALUFN0 c3c2 and4
# Xc3or G2 c3c0 c3c1 c3c2 C3 or4

# Xc4and0 P3 G2 c4c0 and2
# Xc4and1 P3 P2 G1 c4c1 and3
# Xc4and2 P3 P2 P1 G0 c4c2 and4
# Xc4and3 P3 P2 P1 P0 ALUFN0 c4c3 and5
# Xc4or G3 c4c0 c4c1 c4c2 c4c3 C4 or5

# Xc5and0 P4 G3 c5c0 and2
# Xc5and1 P[4:3] G2 c5c1 and3
# Xc5and2 P[4:2] G1 c5c2 and4
# Xc5and3 P[4:1] G0 c5c3 and5
# Xc5and4 P[4:0] ALUFN0 c5c4 and6
# Xc5or G4 c5c0 c5c1 c5c2 c5c3 c5c4 C5 or7

# Xc6and0 P5 G4 c6c0 and2
# Xc6and1 P5 G2 G1 c6c1 and3
# Xc6and2 P5 G3 G2 G1 c6c2 and4
# Xc6and3 P5 G4 G3 G2 G1 c6c3 and5
# Xc6and4 P5 P4 P3 P2 P1 G0 c6c4 and6
# Xc6or G5 c6c0 c6c1 c6c2 c6c3 c6c4 C6 or6

'''


'''
# Scripting for and & or gates
for i in range(5,33):

	print ".subckt nor%d a[%d:0] out"%(i-1,i-2)
	print "XnorTemp a[%d:0] temp0 nor%d"%(i-3,i-2)
	print "Xinv a%d ap%d inverter"%(i-2,i-2)
	print "Xand ap%d temp0 out and2"%(i-2)
	# print "Xinverter temp0 temp inverter"
	# print "Xnor temp a%d out nor2"%(i-2)
	print ".ends\n"

	print ".subckt and%d"%i + " a[%d:0] out"%(i-1)
	print "Xinvert a[%d:0] ap[%d:0] inverter"%(i-1,i-1)
	print "XandTemp ap[%d:0]"%(i-2) + " temp nand%d"%(i-1)
	print "Xand temp ap%d"%(i-1) + " out nor2"
	print ".ends\n"
	
	print ".subckt or%d"%i + " " + input + " a%d out"%(i-1)
	print "XorTemp " + input + " temp or%d"%(i-1)
	print "Xor temp a%d"%(i-1) + " out or2"
	print ".ends\n"
	input += " a%d"%(i-1)
'''

# for i in range(5,33):
# 	print ".subckt nand%d a[%d:0] out"%(i,i-1)
# 	print "XprevAnd a[%d:0] temp nand%d"%(i-2,i-1)
# 	print "Xinv temp temp0 inverter"
# 	print "Xnand temp0 a%d out nand2"%(i-1)
# 	print ".ends\n"

# print 5%4
# print (5%4)/3
# print 6%4
# print (6%4)/3
# print 7%4
# print (7%4)/3
# print 8%4
# print (8%4)/3
# print 9%4
# print (9%4)/3
# print 10%4
# print (10%4)/3
# print 11%4
# print (11%4)/3
# print 12%4
# print (12%4)/3

for numInput in range(5,34,4):
	print numInput
	