# Covid and Dictionaries
covid_positive_cases = {
    'Cyprus': [25, 1000, 2000],
    'France': [100000, 123000, 240000],
    'UK': [120000, 260000, 280000]}

print("1.  Search by country\n2.  Search by time stamp\n3.  View all\n-------")


def indexing(lst, word):
    for index in range(len(lst)):
        if word == lst[index] or word == lst[index].lower():
            return index


userinput = int(input("Input your choice: "))
if userinput == 1:
    countryname = input("Enter country name: ")

    print(list(covid_positive_cases.keys())[indexing(list(covid_positive_cases.keys()), str(countryname))],
          ": ",
          list(covid_positive_cases.values())[indexing(list(covid_positive_cases.keys()), str(countryname))][0],
          ",",
          list(covid_positive_cases.values())[indexing(list(covid_positive_cases.keys()), str(countryname))][1],
          ",",
          list(covid_positive_cases.values())[indexing(list(covid_positive_cases.keys()), str(countryname))][2])
if userinput == 2:
    stamp = eval(input("Enter the Stamp number : "))
    for i in range(len(list(covid_positive_cases.keys()))):
        print(list(covid_positive_cases.keys())[i], ":", list(covid_positive_cases.values())[i][stamp - 1],
              "; ", end="")
if userinput == 3:
    for i in range(len(list(covid_positive_cases.keys()))):
        print(list(covid_positive_cases.keys())[i], " : ",
              list(covid_positive_cases.values())[i][0], ", ",
              list(covid_positive_cases.values())[i][1], ", ",
              list(covid_positive_cases.values())[i][2],
              " ", end="")



