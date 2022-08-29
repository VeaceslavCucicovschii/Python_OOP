
class Humanity:
  people = 8_000_000_000
  planet = "Terra"

  def dailyBirth():
    return 400_000
  
  def dailyDeth():
    return 40_000

# print(Humanity.dailyBirth())

initial_number_of_people = Humanity.people
print("People in 2022: ", Humanity.people)

for day in range(365):
  Humanity.people += Humanity.dailyBirth()
  Humanity.people -= Humanity.dailyDeth()
  

print("People growth from 2022 to 2023: ", Humanity.people - initial_number_of_people)

print("Planet humanity befor 2050: ", Humanity.planet)

fourth_planet = input("Introduce fourth planet name: ")
fifth_planet = input("Introduce fifth planet name: ")

Humanity.planet = [Humanity.planet, "Moon", "Mars", fourth_planet, fifth_planet]


print("Planet humanity starting 2050: ", Humanity.planet)