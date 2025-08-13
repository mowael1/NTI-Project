from google_play_scraper import reviews, Sort
import pandas as pd

# Replace with your app's package name
app_id = "com.talabat"

def main(country , lang):
    result, _ = reviews(
        app_id,
        lang=lang,        # Language of reviews
        country=country,     # Country
        sort=Sort.NEWEST, # Sort by newest reviews
        count=100000      # Number of reviews to fetch
    )

    review_list = []

    for r in result:
        
        review_list.append({"user" : r['userName'],
                        "rating": r['score'],
                        "review": r["content"]
                        })

    df = pd.DataFrame(review_list)
    
    return df


egypt_data = main("eg" , "ar")
egypt_data.to_csv(r'C:\Users\mw865\Desktop\python\egypt_data.csv' , index=False , encoding='utf-8-sig')