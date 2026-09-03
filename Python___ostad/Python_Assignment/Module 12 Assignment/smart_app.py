"""
Module 12 Assignment - Smart Text Analyzer & Live Data App

"""

import urllib.request
import json

def main():
    # Step 2: Program Introduction
    
    
    print("Welcome to Smart Text Analyzer & Live Data App")
    print("==================================================\n")

  
  
    # Step 3: String Analyzer Section
    # ----------------------------------------------------
    
    
    print("--- 1. STRING ANALYZER ---")
    sentence = input("Enter a sentence: ").strip()

    # Step 7: Error handling for empty input
    if not sentence:
        print("Warning: Empty input provided for sentence analysis.")
    else:
        # Character & Word 
        
        char_count = len(sentence)
        words = sentence.split()
        word_count = len(words)

        # Palindrome Check 
        
        cleaned_str = "".join(sentence.split()).lower()
        is_palindrome = cleaned_str == cleaned_str[::-1]

        print(f"Total Characters : {char_count}")
        print(f"Total Words      : {word_count}")
        print(f"Is Palindrome?   : {'Yes' if is_palindrome else 'No'}\n")

    
    
    # Step 4: Sorting Logic Section & Step 5: Algorithm Challenge
    # ----------------------------------------------------
    
    
    print("--- 2. SORTING & ALGORITHM CHALLENGE ---")
    raw_numbers = input("Enter numbers separated by commas (e.g. 10, 5, 8, 20): ").strip()

    if not raw_numbers:
        print("Warning: No numbers provided.")
    else:
        try:
            # Converting string input into a list of floats
            
            
            num_list = [float(x.strip()) for x in raw_numbers.split(",") if x.strip()]

            if not num_list:
                print("No valid numbers found.")
            else:
                # Step 4: Sorting
                
                
                asc_sorted = sorted(num_list)
                desc_sorted = sorted(num_list, reverse=True)

                print(f"Ascending Order  : {asc_sorted}")
                print(f"Descending Order : {desc_sorted}")

                # Step 5: Algorithm Thinking Challenge (without min() or max())
                
                
                largest = num_list[0]
                smallest = num_list[0]

                for num in num_list:
                    if num > largest:
                        largest = num
                    if num < smallest:
                        smallest = num

                print(f"Largest Number   : {largest} (Found using manual loop)")
                print(f"Smallest Number  : {smallest} (Found using manual loop)\n")

        except ValueError:
            print("Error: Invalid number format! Please enter valid comma-separated numbers.\n")



    # Step 6: API Integration (Mini App)
    # ----------------------------------------------------
    
    
    print("--- 3. LIVE DATA API INTEGRATION ---")
    print("Fetching live Bitcoin price (via free CoinGecko API)...")
    
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            btc_usd = data["bitcoin"]["usd"]
            print(f"Current Bitcoin Price: ${btc_usd:,.2f} USD\n")
            
    except Exception as e:
        print(f"Could not fetch API data. Reason: {e}\n")

    


if __name__ == "__main__":
    main()