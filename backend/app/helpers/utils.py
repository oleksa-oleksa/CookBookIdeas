def scale_ingredients(ingredients, scale_factor):
    """
    Scale the ingredient amounts by the given scale factor.
    If an ingredient's amount is null, it will be excluded from scaling.

    :param ingredients: List of ingredient dictionaries
    :param scale_factor: Integer representing how many servings to scale
    :return: List of scaled ingredient dictionaries
    """
    scaled_ingredients = []

    for ingredient in ingredients:
        scaled_ingredient = ingredient.copy()  # Create a copy to modify

        if ingredient["amount"] is not None:  # Only scale if amount is not null
            scaled_ingredient["amount"] *= scale_factor

        scaled_ingredients.append(scaled_ingredient)

    return scaled_ingredients
