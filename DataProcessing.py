
fields = {0 : "Age", 1 : "Sex", 2 : "Chest pain type", 3 : "Resting bp", 4 : "Cholesteral", 5 : "Fasting blood sugar", 6 : "Resting ecg", 7 : "Max Heart rate", 8 : "Angina", 9 : "Oldpeak", 10 : "Slope", 11 : "Colored Vessels", 12 : "Thal", 13 : "H/S"}

def discretize(i, n):
    '''
    Discretize input data for the attributes: age, cholesteral, heart rate, oldpeak and colored vessels
    '''
	if n == 0:
		age = float(i)
		if age < 45:
			return "mid"
		elif age >= 45 and age <= 65:
			return "eold"	#early old-age
		else:
			return "old"

	elif n == 4:
		#cholesteral
		ch = float(i)
		if ch <= 200:
			return "norm"	#normal
		elif ch > 200 and ch <= 240:
			return "bhigh"	#borderline high
		else:
			return "high" #high

	elif n == 7:
		#heart rate
		hr = float(i)
		if hr < 60:
			return "abn"
		elif hr >= 60 and hr < 100:
			return "norm"
		else:
			return "high"
	
	elif n == 9:
		#oldpeak
		op = float(i)
		if op < 1.5:
			return "low"
		elif op >= 1.5 and op < 2.55:
			return "risk"
		elif op >= 2.55:
			return "high"
	
	elif n == 11:
        #colored vessels
		ca = float(i)
		if ca <= 1:
			return "low"
		elif ca > 1 and ca <= 2:
			return "med"
		else: 
			return "high"

	else:	
		return i

def sign(i, n):
    '''
    Discretize all attributes and return level numbers - 1, 2, 3
    '''
	if n == 0:
		#age
		age = float(i)
		if age < 45:
			return 1
		elif age >= 45 and age <= 65:
			return 2	#early old-age
		else:
			return 3

	elif n == 1:
		#sex
		if i == "male":
			return 1
		return 0

	elif n == 2:
		#chest pain type
		if i == "angina":
			return 1
		elif i == "abnang":
			return 2
		elif i == "notang":
			return 3
		return 4
		
	elif n == 3:
		#resting blood pressure
		i = float(i)
		if i <= 120:
			return 1
		elif i > 120 and i < 140:
			return 2
		return 3

	elif n == 4:
		#cholesteral
		ch = float(i)
		if ch <= 200:
			return 1	#normal
		elif ch > 200 and ch <= 240:
			return 2	#borderline high
		return 3 #high

	elif n == 5:
		#fasting blood sugar
		if i == "true":
			return 1
		return 0

	elif n == 6:
		#resting ecg
		if i == "norm":		
			return 1
		elif i == "abn":
			return 2
		return 3

	elif n == 7:
		#heart rate
		hr = float(i)
		if hr < 60:
			return 2
		elif hr >= 60 and hr < 100:
			return 1
		else:
			return 3

	elif n == 8:
		#exercise induced angina
		if i == "true":
			return 1
		return 0

	elif n == 9:
		#oldpeak
		op = float(i)
		if op < 1.5:
			return 1
		elif op >= 1.5 and op < 2.55:
			return 2
		elif op >= 2.55:
			return 3

	elif n == 10:
		#slope
		if i == "up":
			return 1
		elif i == "flat":	
			return 2
		return 3

	elif n == 11:
		#colored vessels
		ca = float(i)
		if ca <= 1:
			return 1
		elif ca > 1 and ca <= 2:
			return 2
		else: 
			return 3

	elif n == 12:
		#thal
		if i == "norm":
			return 3
		elif i == "fixed":
			return 6
		return 7

	elif n == 13:
		#healthy or sick
		if i == "H":
			return 0
		return 1

def process(fname,oname):
    f = open(fname, "r")
    out = open(oname, "w")
	data = []
	x = 0
	for line in f:	
		l = line.split()
		y = 0
		innerList = []
		for i in l[0:14]:
			if i == "?":
				value = -9
			else:	
				value = sign(i, y)	#discretize(i,y)
			innerList.append(value)
			out.write(str(value))
			out.write(" ")
			y += 1
		data.append(innerList)
		x += 1
		out.write("\n")
	return data

if __name__ == "__main__":
    fname = "data.txt"
    oname = "processedData.txt"
    process(fname, oname)
