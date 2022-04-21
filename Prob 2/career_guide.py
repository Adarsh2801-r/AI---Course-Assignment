from experta import *


careers_list = []
career_factors = []
factor_map = {}
career_d_map = {}

def preprocess():
	careers = open("C:/Users/BITS-PC/Desktop/AI - Assignments/careers.txt")
	careers_list = careers.read().split("\n")
	careers.close()

	for c in careers_list:
		print(c)
		career_f_file = open("C:/Users/BITS-PC/Desktop/AI - Assignments/Career Factors/"+ c +".txt")
		career_f_list = career_f_file.read().split("\n")
		career_factors.append(career_f_list)
		factor_map[str(career_f_list)]=c
		career_f_file.close()
		career_f_file = open("C:/Users/BITS-PC/Desktop/AI - Assignments/Career Descriptions/"+c+".txt")
		career_f_data = career_f_file.read()
		career_d_map[c] = career_f_data
		career_f_file.close()

def choose_career(*arguments):
	factors = []
	for f in arguments:
		factors.append(f)
	return factor_map[str(factors)]

def get_details(career):
	return career_d_map[career]


class Greetings(KnowledgeEngine):

	def __init__(self):
		self.factor_map = factor_map
		self.get_details = get_details
		KnowledgeEngine.__init__(self)

	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hello. This is a knowledge based Career Expert System to give career guidance")
		print("")
		print("Kindly provide details")
		print("")
		yield Fact(action = "find_career")

	@Rule(Fact(action="find_career"),NOT(Fact(cgpa=W())),salience=4)
	def factor_0(self):
		self.declare(Fact(cgpa = input("What is your CGPA? (Reply as high(>9)/medium(7 to 9)/low(<7)):")))

	@Rule(Fact(action="find_career"),NOT(Fact(pub=W())),salience=1)
	def factor_1(self):
		self.declare(Fact(pub = input("Do you have any paper publications under your name? : ")))

	@Rule(Fact(action="find_career"),NOT(Fact(crux=W())),salience=1)
	def factor_2(self):
		self.declare(Fact(crux = input("Are you member of cruX ? : ")))

	@Rule(Fact(action="find_career"),NOT(Fact(acm=W())),salience=1)
	def factor_3(self):
		self.declare(Fact(acm = input("Are you member of ACM ? : ")))

	@Rule(Fact(action="find_career"),NOT(Fact(ieee=W())),salience=1)
	def factor_4(self):
		self.declare(Fact(ieee = input("Are you member of IEEE? : ")))

	@Rule(Fact(action="find_career"),NOT(Fact(por=W())),salience=1)
	def factor_5(self):
		self.declare(Fact(por = input("Do you hold any PORs? : ")))


	@Rule(
		Fact(action="find_career"),
		Fact(cgpa="medium"),
		Fact(pub="n"),
		Fact(crux="y"),
		Fact(acm="y"),
		Fact(ieee="n"),
		Fact(por="n")
	)
	def career_0(self):
		self.declare(Fact(career = "IT"))

	@Rule(
		Fact(action="find_career"),
		Fact(cgpa="medium"),
		Fact(pub="n"),
		Fact(crux="n"),
		Fact(acm="n"),
		Fact(ieee="n"),
		Fact(por="y")
	)
	def career_1(self):
		self.declare(Fact(career = "Management"))

	@Rule(
		Fact(action="find_career"),
		Fact(cgpa="high"),
		Fact(pub="y"),
		Fact(crux="n"),
		Fact(acm="y"),
		Fact(ieee="y"),
		Fact(por="n")
	)
	def career_2(self):
		self.declare(Fact(career = "Research"))

	@Rule(Fact(action="find_career"),Fact(career = MATCH.career),salience = -998)
	def career(self,career):
		print("")
		id_career = career
		career_details = self.get_details(id_career)
		print("")
		print("Based on your record, the ideal career path for you would be : \n")
		print(id_career)
		print("A brief Description : \n")
		print(career_details+"\n")





if __name__=="__main__":
	preprocess()
	engine = Greetings()
	while 1 :
		engine.reset()
		engine.run()
		print("Would you like to continue ?\n Reply as y/n")
		if input() == "n":
			exit() 
