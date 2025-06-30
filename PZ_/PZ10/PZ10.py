#Туристические агентства предлагают следующие туры. Вояж - Мексика,Канада,Израиль,Италия,США; 
#РейнаТур - Англия,Япония,Канада,ЮАР; Радуга - США,Испания,Швеция,Австралия.
#Определить в каких турагентсвах можно приобрести туры в Канаду, а в каких в США

voyage = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reina_tour = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}

tour_agent = {
    "Вояж": voyage,
    "РейнаТур": reina_tour,
    "Радуга": raduga}

def find_agent(country):
    agent_country = []
    for agent, tours in tour_agent.items():
        if country in tours:
            agent_country.append(agent)
    return agent_country

agent_canada = find_agent("Канада")
agent_usa = find_agent("США")

print("Агентства, предлагающие туры в Канаду:", agent_canada)
print("Агентства, предлагающие туры в США:", agent_usa)