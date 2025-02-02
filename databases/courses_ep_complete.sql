DROP TABLE IF EXISTS courses_ep_complete;
CREATE TABLE IF NOT EXISTS courses_ep_complete (
    userID VARCHAR(150),
    courseSlug VARCHAR(150),
    epSlug VARCHAR(150),
    createdAt TIMESTAMP
);