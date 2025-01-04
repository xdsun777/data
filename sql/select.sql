-- SELECT "_rowid_",* FROM "main"."zhibo2" WHERE "时间" REGEXP '2024-12-1[6789]' AND "时间" REGEXP '2024-12-2[01234]';
-- SELECT "_rowid_",* FROM "main"."zhibo2" WHERE "时间" REGEXP '2024-12-1[6789]' GROUP BY "Uid"
-- UNION
-- SELECT "_rowid_",* FROM "main"."zhibo2" WHERE "时间" REGEXP '2024-12-2[01234]' GROUP BY "Uid" ORDER BY "主播昵称";
-- SELECT * FROM "main"."zhibo2"  GROUP BY "Uid";
-- SELECT "_rowid_",* FROM "main"."zhibo" WHERE "时间" REGEXP '2024-12-27' GROUP BY "uid" ORDER BY "主播昵称";
-- SELECT id,创建时间 FROM "main"."zhibo"  ORDER BY "uid";

