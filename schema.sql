drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);
 drop table if exists subject;

 create table subject(
 	id integer primary key autoincrement,
 	name text not null);

 drop table if exists messages;

 create table messages(
 	id integer primary key autoincrement,
 	subid integer not null,
 	userid integer not null,
 	message text,
 	FOREIGN KEY(subid) REFERENCES subject(id),
 	FOREIGN KEY(userid) REFERENCES users(id)
 	);