the_boys = [
    {
    "alias": "Billy Butcher",
    "real_name": "William 'Billy' Butcher",
    "powers": []
    },
    {
    "alias": "Hughie",
    "real_name": "Hughie Campbell Jr",
    "powers": []
},{
    "alias": "Starlight",
    "real_name": "Annie January",
    "powers": ["Electricity conversion", "Superhuman strength and reflexes", "Regenerative healing"]
}]

def find_real_names():
    list_of_real_names = []
    for names in the_boys:
        list_of_real_names.append(names["real_name"])
    print(list_of_real_names)

find_real_names()