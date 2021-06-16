create table users
(
   	username varchar(100) not null,
	userId int not null,
	Email    varchar(256) not null,
	Password varchar(20)  not null,
	PRIMARY KEY(userId,Email)
);


INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('amit gabay',1, 'amit@gmail.com', 'a123');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('ido gabay',2,'ido@gmail.com', 'b123');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('omer gabay',3, 'omer@gmail.com', 'c234');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('lior ribak',4, 'lior@walla.com', 't567');
INSERT INTO schema_users.users (username, userId, Email, Password) VALUES ('ariel amit',5, 'ariel@gmail.com', 'u678');

select * from users;