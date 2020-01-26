best_dishes={"biryani","BBQ","Mutton Karahi","Kheer","Roasted Chicken"}
print("my fav dishes are: ",best_dishes)
for p in range(len(best_dishes)):
    a=best_dishes.pop()
    print(a)
print("after pop the all items in best_dishes:",best_dishes)