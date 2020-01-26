fav_dishes={"biryani":['monday'],"karahi":['tuesday'],"bbq":['wednesday'],"sabzi":['thursday'],"pulao":['friday'],"dal fry":['saturday'],"mutton karahi":['sunday']}

dishes_in_week={"aloo paratha":['monday'],"biryani":['tuesday'],"bhindi":['wednesday'],"dal fry":['thursday'],"beef pulao":['friday'],"qourma":['saturday'],"mutton karahi":['sunday']}

no_of_dish=len(dishes_in_week.keys() & fav_dishes.keys())
x=(dishes_in_week.keys() & fav_dishes.keys())
print("no of dish which your fav dishes:{}".format(no_of_dish))
print("{}".format(fav_dishes))
print("{}".format(dishes_in_week))
print("{}".format(x))