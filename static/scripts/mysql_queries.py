
query = """SELECT Name FROM country;"""

q_continent_country_count = """SELECT continent,COUNT(*) FROM country GROUP BY continent;"""

q_continent_pop = """SELECT continent, CAST(SUM(Population) AS DECIMAL) as TotalPopulation FROM country GROUP BY continent order by TotalPopulation asc;"""

q_continents = """SELECT DISTINCT Continent FROM country c order by Continent ASC;"""

q_countries = """SELECT Name, Continent, Population FROM country c order by Continent, Name ASC;"""

