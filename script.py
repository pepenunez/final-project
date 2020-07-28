import pandas as pd
import numpy as np

# Functions from supermarkets-modelling

def get_products(ingredients:list):
    
            # ...
    supermarkets_lists = {
            'aldinorth': [],
            'aldisouth': [],
            'edeka': []
            #'kaufan': pd.read_pickle('data/products-clean/edeka-products-clean.pkl')
            #'rewe': pd.read_pickle('data/products-clean/edeka-products-clean.pkl')
            #'lidl':
        }
    
    for market in supermarkets:

        for ing in ingredients:
        
            # Empty dictionary where we will store the matching products
            matches = []   
        
            # For each product, iterate through each supermarket and generate a list
            for product in supermarkets[market]['Name']:
                ratio = fuzz.ratio(product.lower(), ing.lower())

                if ratio > 50:
                    matches.append((product, ratio))
                    matches = sorted(matches, key=lambda x: x[1], reverse=True)
                
            # If matches list is not empty
            if matches:
                supermarkets_lists[market].append(matches[0][0])
                        
    return supermarkets_lists

def get_list_products_price(ingredients:list):
    
    # Create a dictionary with the supermarkets and a list with the products
    supermarkets_p = {
        'aldinorth': get_products(ingredients)['aldinorth'],
        'aldisouth': get_products(ingredients)['aldisouth'],
        'edeka': get_products(ingredients)['edeka']
        # ...
    }
    
    # New empty df
    result = pd.DataFrame(columns=['Supermarket', 'Ingredient', 'Price', 'Coverage'])

    # Iterate and populate a df with the final result
    for market in supermarkets_p:
        
        # Iterate per each product in each supermarket
        s = supermarkets[market] # Dictionary which contains the detailed info of all products per supermarket
        
        for ing in supermarkets_p[market]:    
            try:
                price = s[s['Name'] == ing]['Price'].values[0]
                df2 = {'Supermarket': market, 'Ingredient': ing, 'Price': price, 'Coverage': 1}
                result = result.append(df2, ignore_index=True)
            except:
                result = result.append({'Supermarket': market, 'Ingredient': ing, 'Price': np.nan, 'Coverage': 0}, ignore_index=True)
    
    # 'result' contains detailed information about product and price per each supermarket
    
    # Change to numeric
    result['Price'] = pd.to_numeric(result['Price'], errors='coerce')
    result['Coverage'] = pd.to_numeric(result['Coverage'], errors='coerce') * 100
    
    return result

# We want to see:
#    1. Where we will be able to find all the products
#    2. Where can we buy them at the best price

def get_supermarket_choice(ingredients:list):
    
    result = get_list_products_price(ingredients) 
    
    # Group by 'Supermarket'
    results = result.groupby('Supermarket').agg({'Price':'sum', 'Coverage': 'mean'}).reset_index()
    results = results.sort_values('Price').reset_index(drop=True)
    
    return results

def get_shopping_list(ingredients:list):
    
    result = get_list_products_price(ingredients) 
    results = get_supermarket_choice(ingredients)
    
    # Ask the user where they would like to do the grocery shopping
    user_input = input('Where would you like to go shopping?\n')
    
    return result[result['Supermarket'] == user_input]