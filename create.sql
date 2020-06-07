CREATE TABLE "bot_info" (
	"group_jid"	TEXT,
	"peer_jid"	TEXT,
	"user_name"	TEXT,
	"screen_name"	TEXT,
	"days"	REAL,
	"pfp"	TEXT,
	"msg_sent"	TEXT,
	"first_msg"	TEXT,
	"removed_eve"	int,
	"no_of_msg"	int
);
CREATE TABLE "group_info" (
	"group_jid"	TEXT NOT NULL,
	"join_time"	REAL,
	"wiki_status"	TEXT,
	"verification_status"	TEXT,
	"owner"	TEXT,
	"admins"	TEXT,
	"verification_time"	INT DEFAULT 180,
	"welcome_message"	TEXT
, verification_days INT DEFAULT 20);
CREATE TABLE "user_info" (
	"group_jid"	TEXT NOT NULL,
	"peer_jid"	TEXT NOT NULL,
	"given_name"	TEXT
);

