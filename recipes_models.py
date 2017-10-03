"""module for implementing recipe methods"""
user_recipes = [] # pylint: disable=invalid-name


class Recipe(object):
    """class defining create, delete and update methods"""

    def __init__(self, title=None, details=None):

        self.title = title
        self.details = details

    def create_recipe(self):
        """"intiate create function"""

        recipe = {}
        recipe["title"] = self.title
        recipe["details"] = self.details

        user_recipes.append(recipe)

    def delete_recipe(self, recipe):
        """intiate delete function"""
        for recipe in user_recipes:
            if recipe:  
                del recipe[0]

                return 




    def update_recipe(self, recipe, new_recipe):
        """intiate update function"""
        pass
