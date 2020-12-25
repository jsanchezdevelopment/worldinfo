
query = """SELECT Name FROM country;"""

query2 = """SELECT continent,COUNT(*) FROM country GROUP BY continent;"""

query3 = """SELECT continent, CAST(SUM(Population) AS DECIMAL) as TotalPopulation FROM country GROUP BY continent order by TotalPopulation asc;"""