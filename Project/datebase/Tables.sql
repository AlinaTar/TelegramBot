CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS changes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    name_surname TEXT NOT NULL,
    data TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS checks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT NOT NULL,
    photo_id TEXT NOT NULL,
    data TEXT NOT NULL
);