DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies (
MovieID int PRIMARY KEY,
Name varchar(255),
Year int,
Rating int
);

INSERT INTO Movies
VALUES
(1, "Dr. No", 1962, 95),
(2, "From Russia with Love", 1963, 97),
(3, "Goldfinger", 1964, 99),
(4, "Thunderball", 1965, 83),
(5, "You Only Live Twice", 1967, 74),
(6, "On Her Majesty's Secret Service", 1969, 80),
(7, "Diamonds Are Forever", 1971, 63),
(8, "Live and Let Die", 1973, 65),
(9, "The Man With the Golden Gun", 1974, 43),
(10, "The Spy Who Loved Me", 1977, 83),
(11, "Moonraker", 1979, 60),
(12, "For Your Eyes Only", 1981, 67),
(13, "Octopussy", 1983, 41),
(14, "A View to a Kill", 1985, 38),
(15, "The Living Daylights", 1987, 77),
(16, "Licence to Kill", 1989, 79),
(17, "GoldenEye", 1995, 80),
(18, "Tomorrow Never Dies", 1997, 57),
(19, "The World Is Not Enough", 1999, 50),
(20, "Die Another Day", 2002, 56),
(21, "Casino Royale", 2006, 94),
(22, "Quantum of Solace", 2008, 63),
(23, "Skyfall", 2012, 92),
(24, "Spectre", 2015, 63),
(25, "No Time to Die", 2021, 83);

SELECT *
FROM Movies;