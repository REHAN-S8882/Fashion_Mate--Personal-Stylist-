import streamlit as st
import pandas as pd

# Define the fashion data with suggestions for both Male and Female
fashion_data = {
    'Female': {
        'Indian': {
            'saree': {
                'colors': ['blue', 'red', 'gold', 'green', 'black'],
                'blouse_colors': ['red', 'gold', 'blue', 'green', 'black'],
                'lower_wear': {
                    'petticoat': ['white', 'cream', 'black']
                },
                'footwear': {
                    'heels': ['black', 'red', 'gold'],
                    'ballet flats': ['blue', 'green', 'black']
                }
            },
            'lehenga': {
                'colors': ['blue', 'red', 'green', 'gold', 'yellow'],
                'lower_wear': {
                    'lehenga': ['red', 'blue', 'green', 'gold'],
                },
                'footwear': {
                    'heels': ['red', 'black', 'gold'],
                    'flat sandals': ['blue', 'gold', 'pink']
                }
            },
            'kurti': {
                'colors': ['yellow', 'green', 'pink', 'blue', 'black'],
                'lower_wear': {
                    'salwar': ['white', 'black', 'blue'],
                    'leggings': ['blue', 'black', 'green'],
                    'jeans': ['blue', 'black', 'white']
                },
                'footwear': {
                    'flats': ['white', 'black', 'pink'],
                    'heels': ['gold', 'black', 'blue'],
                    'sneakers': ['white', 'black']
                }
            },
            'churidar': {
                'colors': ['white', 'black', 'blue', 'red', 'green'],
                'lower_wear': {
                    'churidar': ['white', 'black', 'red'],
                },
                'footwear': {
                    'flats': ['black', 'blue', 'red'],
                    'heels': ['gold', 'blue', 'red'],
                    'sandals': ['black', 'brown']
                }
            }
        },
        'Western': {
            'shirt': {
                'colors': ['white', 'blue', 'green', 'red', 'black'],
                'lower_wear': {
                    'jeans': ['blue', 'black', 'grey'],
                    'shorts': ['red', 'blue', 'black'],
                    'skirt': ['blue', 'black', 'red']
                },
                'footwear': {
                    'sneakers': ['white', 'black', 'grey'],
                    'heels': ['red', 'black', 'blue'],
                    'flats': ['black', 'white', 'pink']
                }
            },
            'dress': {
                'colors': ['red', 'black', 'blue', 'green', 'yellow'],
                'lower_wear': {
                    'dress': ['red', 'black', 'blue']
                },
                'footwear': {
                    'heels': ['black', 'red', 'blue'],
                    'sandals': ['white', 'gold', 'blue'],
                    'flats': ['green', 'black', 'red']
                }
            },
            'jumpsuit': {
                'colors': ['black', 'red', 'blue', 'green', 'yellow'],
                'lower_wear': {
                    'jumpsuit': ['black', 'blue', 'red'],
                },
                'footwear': {
                    'heels': ['black', 'gold', 'red'],
                    'flats': ['blue', 'green', 'red']
                }
            },
            'blouse': {
                'colors': ['pink', 'green', 'blue', 'yellow', 'black'],
                'lower_wear': {
                    'jeans': ['blue', 'black', 'white'],
                    'skirt': ['blue', 'red', 'black'],
                    'trousers': ['black', 'green', 'grey']
                },
                'footwear': {
                    'flats': ['black', 'blue', 'white'],
                    'heels': ['red', 'pink', 'black'],
                    'sandals': ['blue', 'green', 'yellow']
                }
            }
        }
    },
    'Male': {
        'Indian': {
            'kurta': {
                'colors': ['white', 'blue', 'green', 'yellow', 'red'],
                'lower_wear': {
                    'salwar': ['white', 'cream', 'black'],
                    'jeans': ['blue', 'black', 'white'],
                    'trousers': ['black', 'blue', 'grey']
                },
                'footwear': {
                    'mojari': ['brown', 'black'],
                    'sandals': ['brown', 'black']
                }
            },
            'sherwani': {
                'colors': ['white', 'gold', 'red', 'green'],
                'lower_wear': {
                    'salwar': ['white', 'gold', 'red'],
                },
                'footwear': {
                    'mojari': ['gold', 'black'],
                    'sandals': ['brown', 'gold']
                }
            }
        },
        'Western': {
            'shirt': {
                'colors': ['blue', 'white', 'black', 'green', 'yellow'],
                'lower_wear': {
                    'jeans': ['blue', 'black', 'grey'],
                    'trousers': ['black', 'grey', 'blue'],
                    'shorts': ['blue', 'black', 'red']
                },
                'footwear': {
                    'loafers': ['black', 'brown', 'blue'],
                    'sneakers': ['white', 'blue', 'black']
                }
            },
            't-shirt': {
                'colors': ['white', 'black', 'grey', 'blue'],
                'lower_wear': {
                    'jeans': ['blue', 'black', 'grey'],
                    'shorts': ['blue', 'green', 'black'],
                    'track pants': ['black', 'grey', 'blue']
                },
                'footwear': {
                    'sneakers': ['blue', 'white', 'black'],
                    'loafers': ['brown', 'black', 'blue']
                }
            },
            'blazer': {
                'colors': ['black', 'blue', 'grey'],
                'lower_wear': {
                    'jeans': ['blue', 'black', 'grey'],
                    'trousers': ['black', 'blue', 'grey']
                },
                'footwear': {
                    'loafers': ['black', 'brown'],
                    'boots': ['brown', 'black']
                }
            }
        }
    }
}


# Function to generate combinations
def generate_combinations(upper_wear, color, blouse_color, lower_wear_options, lower_colors, footwear_options,
                          footwear_colors, gender):
    combinations = []
    for lower, lower_color in zip(lower_wear_options, lower_colors):
        for footwear, footwear_color in zip(footwear_options, footwear_colors):
            if upper_wear == 'saree' and gender == 'Female':
                combinations.append([upper_wear, color, blouse_color, lower, lower_color, footwear, footwear_color])
            else:
                combinations.append([upper_wear, color, lower, lower_color, footwear, footwear_color])
    return combinations


# Main function for user interface
def main():
    st.title('FashionMate - Your Personal Stylist')

    # Gender selection
    gender = st.selectbox('Select Gender:', ['Male', 'Female'])

    # Fashion type selection
    fashion_type = st.selectbox('Select Fashion Type:', ['Indian', 'Western'])

    # Upper wear selection
    upper_wear = st.selectbox('Select Upper Wear:', list(fashion_data[gender][fashion_type].keys()))

    # Color selection for upper wear
    upper_wear_color = st.selectbox(f'Select Color for {upper_wear}:',
                                    fashion_data[gender][fashion_type][upper_wear]['colors'])

    blouse_color = None
    if upper_wear == 'saree' and gender == 'Female':
        blouse_color = st.selectbox(f'Select Blouse Color for {upper_wear}:',
                                    fashion_data[gender][fashion_type][upper_wear]['blouse_colors'])

    # Get lower wear, colors, and footwear suggestions
    lower_wear_suggestions = list(fashion_data[gender][fashion_type][upper_wear]['lower_wear'].keys())
    lower_wear_colors = list(fashion_data[gender][fashion_type][upper_wear]['lower_wear'].values())[0]
    footwear_suggestions = list(fashion_data[gender][fashion_type][upper_wear]['footwear'].keys())
    footwear_colors = list(fashion_data[gender][fashion_type][upper_wear]['footwear'].values())[0]

    # Generate all combinations
    combinations = generate_combinations(upper_wear, upper_wear_color, blouse_color, lower_wear_suggestions,
                                         lower_wear_colors, footwear_suggestions, footwear_colors, gender)

    # Adjust the column names if blouse is present or not
    columns = ['Upper Wear', 'Upper Wear Color', 'Blouse Color', 'Lower Wear', 'Lower Wear Color', 'Footwear',
               'Footwear Color']
    if gender == 'Male' or upper_wear != 'saree':
        columns.remove('Blouse Color')

    # Create DataFrame
    df_combinations = pd.DataFrame(combinations, columns=columns)
    st.table(df_combinations)


# Run the application
if __name__ == '__main__':
    main()
