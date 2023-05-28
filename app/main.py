import utils
import read_csv
import charts

#dualidad ejecutado main como modulo o como script

def run():
    data = read_csv.read_csv("data.csv")
    #Para que no se vea tan mal el grafico se filtra por continente
    data = list(filter(lambda item:item["Continent"] == "South America",data))
    
    countries = list(map(lambda x:x["Country/Territory"], data))
    percentages = list(map(lambda x:x["World Population Percentage"], data))
    charts.generate_pie_chart(countries,percentages)

    country = input("Digite el pais => ")

    result = utils.population_by_country(data,country)

    if len(result) > 0:
        country = result[0]
        #Keys son los labels
        #value es value
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels,values)

#Este if nos dice que si se ejecuta desde la terminal tambien corra el archivo osea correr como script
if __name__ == "__main__" :
    run()