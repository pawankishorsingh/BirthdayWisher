import os, random
import datetime
import SendMail
import Config

class BirthdayWisher:
	def __init__(self, name, email, today):
		self.name = name
		self.email = email
		self.today = today
		imagePath = None

	def choseRandomImage(self):
		imageName = random.choice(os.listdir(Config.imageDirectory))
		self.imagePath = os.path.join(Config.imageDirectory, imageName)

	def composeAndSendEmail(self):
		recipient = self.email
		sub = "Happy Birthday - " + self.name
		html_header = Config.html_header % (self.name)
		html_body = Config.html_body % (self.today)
		html_footer = Config.html_footer % (Config.sender.split()[0])
		SendMail.send_mail(Config.server, Config.sender, recipient, sub, html_header, html_body, html_footer, self.imagePath, files=[], cc=Config.cc, bcc=[])
		print("Mail sent successfully to %s" % (recipient))


class RecordParser:
	def __init__(self):
		birthdayFlag = False
		today = None

	def calulateTodaysDate(self):
		# today will be an str object with value like '27-06'
		self.today = datetime.date.today().strftime('%d-%b').lstrip('0')
		print("today: ", self.today)

	def deleteLog(self):
		if os.path.isfile('birthday_persons.log'):
			os.remove('birthday_persons.log')

	def printFoundMessage(self, name):
		print("Wow !!! It's %s's birthday today..." % name)

	def updateLog(self, name):
		fh = open('birthday_persons.log', 'a')
		fh.write(name.strip() + ",")
		fh.close()

	def parseRecordsAndSendWishes(self):
		with open("Records.csv") as f:
			records_list = f.readlines()
			for record in records_list:
				(dob, name, email) = record.split(",")
				if dob == self.today:
					print("dob:", dob)
					self.birthdayFlag = True
					self.printFoundMessage(name)
					self.updateLog(name)
					birthdayWisher = BirthdayWisher(name, email, self.today)
					birthdayWisher.choseRandomImage()
					birthdayWisher.composeAndSendEmail()

	def printMessageIfNoMail(self):
		if self.birthdayFlag == False:
			print("Sadly !!! There are no birthdays listed for today i.e. %s..." % self.today)

if __name__ == '__main__':
	recordParser = RecordParser()
	recordParser.calulateTodaysDate()
	recordParser.deleteLog()
	recordParser.parseRecordsAndSendWishes()
