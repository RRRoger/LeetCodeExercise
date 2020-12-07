SELECT FirstName,
       LastName,
       City,
       STATE
FROM Person Person
LEFT JOIN Address Address ON Address.PersonId = Person.PersonId