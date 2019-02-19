veg = {"Cucumber": "Add to sandwich",
       "Cabbage": "Make Soup of it",
       "Carrot": "Healthy good for your eyes"}

fruit = {"Orange": "Citrus fruit",
         "Aple": "Keeps a doctor away",
         "Pear": "Green coloured fruit"}

# want to add fruit to veg dictionary
print(veg)
# veg.update(fruit)
print("=" * 50)
print(veg)
print(veg.update(fruit))  # this return none as explained before doesnt create any new object

# below is copy method
# lets say you dont want to update the existing but want to join both dictionaries
# copy method is best to use in that case as it lets you do that and you will have both in one dictionary.


print("=" * 50)
nice_n_nasty = fruit.copy()
nice_n_nasty.update(veg)
print(nice_n_nasty)