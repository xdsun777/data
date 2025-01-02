CREATE TABLE "zhibo2" (
	"id"	INTEGER NOT NULL UNIQUE,
	"主播昵称"	TEXT,
	"时间"	TEXT,
	"用户昵称"	TEXT,
	"动作"	TEXT,
	"内容"	TEXT,
	"Uid"	TEXT NOT NULL,
	"抖音号"	TEXT,
	"性别"	TEXT,
	"地区"	TEXT,
	"简介"	TEXT,
	"等级"	INTEGER,
	"粉丝"	INTEGER,
	"关注"	INTEGER,
	"精准"	INTEGER,
	"Secid"	TEXT,
	"qurl"	TEXT,
	"私密"	BLOB,
	"蓝V"	TEXT,
	"作品链接"	TEXT,
	"创建时间"	INTEGER,
	"省份"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "zhibo" (
	"id"	INTEGER NOT NULL UNIQUE,
	"编号"	TEXT,
	"用户昵称"	TEXT,
	"勋章等级"	TEXT,
	"动作"	TEXT,
	"抖音号"	TEXT,
	"sec_uid"	TEXT,
	"uid"	TEXT,
	"简介"	TEXT,
	"粉丝"	TEXT,
	"关注"	TEXT,
	"性别"	TEXT,
	"地区"	TEXT,
	"精准"	TEXT,
	"时间"	TEXT,
	"省份"	TEXT,
	"创建时间"	TEXT,
	"主播昵称"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);


CREATE TABLE "fensi" (
	"id"	INTEGER NOT NULL UNIQUE,
	"昵称"	INTEGER,
	"UID"	INTEGER,
	"简介"	TEXT,
	"sec_uid"	TEXT,
	"抖音号"	TEXT,
	"精准"	TEXT,
	"蓝v认证"	TEXT,
	"粉丝数"	TEXT,
	"创建时间"	TEXT,
	"from"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);