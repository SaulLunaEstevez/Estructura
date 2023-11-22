BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Camiones" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"totalAlmacenaje"	INTEGER,
	"placas"	TEXT,
	"marca"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
