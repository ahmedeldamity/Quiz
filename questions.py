import json

def Topic(user, topicName):

	with open("Question.json", "r") as File:
		jsonData = json.load(File)

	quId = questionStopped(user, topicName)

	for topic in jsonData["topics"]:
		if topic["topic_name"] == topicName:

			for question in topic["questions"]:
				if question["id"] >= quId:

					print(question["question_statement"])

					for option in question["options"]:
						print(option)

					ans = int(input("Enter Your Answer (1/2/3/4): "))

					if ans == question["answer"]:
						print("Right answer")
						user.score += question["point"]

					else:
						print("Wrong answer")

					print(f"Your score: {user.score}", end="\n\n")
					saveNewQuestionId(user, topicName, question["id"] + 1, user.score)

def saveNewQuestionId(user, topicName, newId, newScore):

	with open("UserData.json", "r") as File:
		jsonData = json.load(File)

	for person in jsonData:
		x = 0
		for key, value in person.items():
			if key == "userName" and value == user.userName:
				x = 1

			if x == 1 and key == "questionTopics":

				for key2, value2 in value.items():
					if key2 == topicName:
						person[key][key2] = newId

			if x == 1 and key == "score":
				person[key] = newScore

	with open("UserData.json", "w") as File:
		json.dump(jsonData, File, indent=4)


def questionStopped(user, topicName):

	with open("UserData.json", "r") as File:
		jsonData = json.load(File)

	questionId = 1

	for person in jsonData:
		x = 0
		for key, value in person.items():

			if key == "userName" and value == user.userName:
				x = 1
			if x == 1 and key == "questionTopics":

				for _key, _value in value.items():
					if _key == topicName:
						questionId = _value

	return questionId