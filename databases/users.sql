DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    userID VARCHAR(150),
    platformName VARCHAR(150),
    platformID VARCHAR(150),
    createdAt TIMESTAMP,
    lastSeenAt TIMESTAMP
);