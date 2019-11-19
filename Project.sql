CREATE TABLE Quiz (
	Name varchar(500),
	Instructor varchar(100) NOT NULL,
	Quiz_Level varchar(50) NOT NULL,
	Description varchar(100),
	PRIMARY KEY (Name)
);

CREATE TABLE Questions (
	ID INT AUTO_INCREMENT,
	Question varchar(1000),
	Quiz_Name varchar(500),
	PRIMARY KEY (ID),
	FOREIGN KEY (Quiz_Name) REFERENCES Quiz(Name)
);

CREATE TABLE Choices (
	ID INT AUTO_INCREMENT,
	Choice varchar(100) NOT NULL,
	IfAnswer varchar(1) NOT NULL,
	Quiz_Name varchar(500),
	Question_ID INT,
	PRIMARY KEY (ID),
	FOREIGN KEY (Quiz_Name) REFERENCES Quiz(Name),
	FOREIGN KEY (Question_ID) REFERENCES Questions(ID)
);

CREATE TABLE Grades (
	Quiz_Name varchar(500),
	Email varchar(50) NOT NULL,
	Score varchar(3) NOT NULL,
	Instructor varchar(50) NOT NULL,
	FOREIGN KEY (Quiz_Name) REFERENCES Quiz(Name),
	FOREIGN KEY (Email) REFERENCES Users(Email)
);