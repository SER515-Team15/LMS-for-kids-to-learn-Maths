CREATE TABLE Quiz (
	Quiz_ID INT AUTO_INCREMENT, 
	Name varchar(50) NOT NULL,
	Email varchar(50) NOT NULL,
	Description varchar(100),
	PRIMARY KEY (Quiz_ID),
	FOREIGN KEY (Email) REFERENCES Users(Email)
);

CREATE TABLE Questions (
	Question_ID INT AUTO_INCREMENT,
	Question varchar(1000),
	Quiz_ID INT,
	PRIMARY KEY (Question_ID),
	FOREIGN KEY (Quiz_ID) REFERENCES Quiz(Quiz_ID)
);

CREATE TABLE Choices (
	Choice_ID INT AUTO_INCREMENT,
	Choice varchar(100) NOT NULL,
	IfAnswer varchar(1) NOT NULL,
	Quiz_ID INT,
	Question_ID INT,
	PRIMARY KEY (Choice_ID),
	FOREIGN KEY (Quiz_ID) REFERENCES Quiz(Quiz_ID),
	FOREIGN KEY (Question_ID) REFERENCES Questions(Question_ID)
);

CREATE TABLE Grades (
	Quiz_ID INT NOT NULL,
	Email varchar(50) NOT NULL,
	Score varchar(3) NOT NULL,
	FOREIGN KEY (Quiz_ID) REFERENCES Quiz(Quiz_ID),
	FOREIGN KEY (Email) REFERENCES Users(Email)
);