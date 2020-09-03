import pandas as pd
import numpy as np

def example():
    return 'Success'

# Functions from supermarkets-modelling

# Functions from allrecipes-modeling:

def get_translation(ingredients:list):
    clean_list = []
    # ...
    for ingredient in ingredients:
        matches = []
        for ing in unique_ingredients:
            ratio = fuzz.ratio(ing.lower(), ingredient.lower())
            if ratio > 50:
                matches.append((ing, ratio))
                matches = sorted(matches, key=lambda x: x[1], reverse=True)
        if matches:
            clean_list.append(matches[0][0])
        else: 
            clean_list.append(np.nan)
    return clean_list

def get_top10_recommendations(ingredients:list):
    ingredients = get_translation(ingredients)
    input_arr = np.array(ingredients)
    
    # Create empty DataFrame
    model = pd.DataFrame(columns=('Ingredient Position', 'Distance'))
    
    # Generate the model
    knn = model_knn.kneighbors(ingredient_features.loc[input_arr].values, n_neighbors=10)
    
    for i, ing in enumerate(ingredients):
        
        # Zip the ingredients position with the distance to the input 'ingredient'
        z = zip(knn[1][i].tolist(), knn[0][i].tolist())
        
        # Format it as a list
        z_list = [(x, y) for x, y in z]
    
        # Create the DataFrame
        temp = pd.DataFrame(z_list, columns=('Ingredient Position', 'Distance'))
        
        # Drop the rows of the ingredients that are already in our list
        temp = temp.drop(temp[temp['Distance'] <= 0.001].index)

        # Concat the new list of (Position, Distance) with the final df
        model = pd.concat([model, temp])
        
    # Group by ingredient position and sort by distance
    model = model.groupby('Ingredient Position').agg({'Distance': 'mean'})
    model = model.sort_values(by='Distance', ascending=True).reset_index()
    
    # Print output header
    print(f'If you are buying {ingredients} you may also want to buy:')
    print(f'---------------------------------------------------------\n')
    
    for x in range(0, 10):
        # Print a list with the top 10 recommendations
        print(f'{x + 1}.{ingredient_features.iloc[model["Ingredient Position"][x]].name}')
    return model.head(10)