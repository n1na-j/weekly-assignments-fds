# Give Python printed texts other styles
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Import Pandas
import pandas as pd

# 1. Load movie_plots.csv
print(color.BOLD + '1. First, download the movie_plots.csv file from Canvas and open it' + color.END)

df = pd.read_csv("movie_plots.csv")
print(df)


#2. Let's inspect the data. Display the first rows and get the summary (.info)
print(color.BOLD + "2. Let's inspect the data. Display the first rows and get the summary (.info)" + color.END)

df.info()


#3. Print out the number of movies for each Origin/Ethnicity
print(color.BOLD + "3. Print out the number of movies for each Origin/Ethnicity" + color.END)
# I thought it would be nice to count the movies per origin/ethnicity
df_movies_per_origin = df.groupby("Origin/Ethnicity")["Origin/Ethnicity"].count().reset_index(name="Total_movies") 
print(df_movies_per_origin)

#4. Subsetting: select only the rows with Bollywood movies
print(color.BOLD + "4. Subsetting: select only the rows with Bollywood movies" + color.END)

df_bollywood = df.copy()
# I couldn't find genre=bollywood. Therefore I searched in the CSV where I can find "Bollywood". It was written in the plots. 
df_bollywood["Bollywood"] = df_bollywood["Plot"].str.contains("Bollywood")
df_bollywood_true = df_bollywood[df_bollywood['Bollywood'] == True]


# I thought it would be great to show only the movies which are indicated as "Bollywood" based on the plot. 
print(df_bollywood_true[['Title', 'Bollywood']])

### Alternative from class ####
subset = df[df["Origin/Ethnicity"] == "Bollywood"]
print(color.GREEN + "Alternative from class:" + color.END)
print(subset)



#5. Subsetting: select only the rows with Turkish movies released after 2000
print(color.BOLD + "5. Subsetting: select only the rows with Turkish movies released after 2000" + color.END)

# Copy the original data
df_turkish_2000 = df.copy()
# Show only movies released after 2000 
df_turkish_2000 = df_turkish_2000[df_turkish_2000['Release Year'] > 2000]
# Show only Turkish movies released after 2000
df_turkish_2000 = df_turkish_2000[df_turkish_2000['Origin/Ethnicity'] == 'Turkish']
print(df_turkish_2000[['Release Year', 'Origin/Ethnicity', 'Title']])

### Alternative from class ###
turkish = df[(df["Origin/Ethnicity"] == "Turkish") & (df["Release Year"] > 2000)]
print(color.GREEN + "Alternative from class:" + color.END)
print(turkish)


#6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot
print(color.BOLD + "6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot" + color.END)
df_new = df[['Title', 'Release Year', 'Origin/Ethnicity', 'Plot']].copy()
print(df_new)



#7. Change the column names to Title, Year, Origin, Plot
print(color.BOLD + "7. Change the column names to Title, Year, Origin, Plot" + color.END)

df_new = df_new.rename(columns={'Release Year': 'Year', 'Origin/Ethnicity': 'Origin'})
print(df_new)



#8. Create a new column "kimono" that is True if the Plot contains the word "kimono"
#and false if not (tip: find a suitable string method).
#Tip: use Pandas .astype(int) to convert the resulting Boolean in 0 or 1.
print(color.BOLD + "8. Create a new column 'kimono' that is True if the Plot contains the word 'kimono'" + color.END)

df_new['Kimono'] = df_new['Plot'].str.contains('kimono').astype(int)
print(df_new)

### Alternative from class ####
# # Make everything capital 
# df_new['Plot'] = df_new['Plot'].str.upper()

# # Make everything lower case
# df_new['Plot'] = df_new['Plot'].str.lower()



#9. Using your new column, pd.groupby() and another Pandas function, count the number of movies
#with "kimono" in the plot, for the different origins.
print(color.BOLD + "9. Using your new column, pd.groupby() and another Pandas function, count the number of movies with 'kimono' in the plot, for the different origins." + color.END)

# It doesn't work like I want to.. 
# df_kimono_movies = df_new.groupby('Origin')[df_new['Kimono'] == True].count().reset_index(name="Total movies with kimono in the plot")
df_kimono_movies = df_new.groupby('Origin')['Kimono'].count().reset_index(name="Total movies with kimono in the plot")

print(color.RED + "It doesn't work like I want to.. It's not counting 0 and 1's! (see solution from class)" +  color.END)
print(df_kimono_movies) 

### Alternative from class ####
# It's not counting 0 and 1!!
# Use .sum(). 3xA = 2 (count kimono's) instead of 3xA = 3 (how many times A occurs) and 3xB = 1 (count kimono's) instead of 3xB = 3 (how many times B occurs)
temp = df_new.groupby('Origin')['Kimono'].sum()
print(color.GREEN + "Alternative from class:" + color.END)
print(temp)


#10. Using your earlier code, create a function add_word_present() with one argument (word),
#that adds a column df[word] with a 1 if the word occurs in the plot,
#and 0 if not.
#Extra challenge: make sure that it's not counted if it's inside another word.
print(color.BOLD + "10. Using your earlier code create a function add_word_present() with one argument (word) that adds a column df[word] with a 1 if the word occurs in the plot and 0 if not. Extra challenge: make sure that its not counted if its inside another word." + color.END)


def add_word_present(word):
    

    if df_new[word] == df_new['Plot'].str.contains(word).astype(int):
        print(word, 'exists in plot')
        print(df_new)
        
    else:
       print("nope", word, 'does not exsits')
            

# add_word_present(input("Write a word: "))

### Alternative from class ####
# Dynamic variables: word
print(color.GREEN + "Alternative from class:" + color.END)

def add_word(word):
   df_new[word] = df['Plot'].str.contains(" " + word + " ").astype(int)
   print(df_new)

add_word(input("Write a word: "))

      
 
#11. Write another function compare_origins() with one argument (word), that:
#1. adds a column to your data frame (simply call your earlier function)
#2. prints the proportion of movies for different origins containing that word
print(color.BOLD + "11.  Write another function compare_origins() with one argument (word), that: adds a column to your data frame (simply call your earlier function), prints the proportion of movies for different origins containing that word" + color.END)

def compare_origins(word):
   add_word(word)
   comparison =  df_new.groupby('Origin')[word].sum()
   print("You compare", word, "with", comparison, ":")

compare_origins(input("Write another word: "))

#12. We need one more tweak: to really compare different cultures,
#we need to account for the fact that the total number of movies is not the same.
#Write another, better function that calculates a percentage rather than a count.
#If you need a hint, see line 75.
#Also sort the result so that the percentage is descending.
#Finally, make it user-friendly: print the word and what the numbers mean
print(color.BOLD + "12.   We need one more tweak: to really compare different cultures: we need to account for the fact that the total number of movies is not the same. Write another, better function that calculates a percentage rather than a count. If you need a hint, see line 75. Also sort the result so that the percentage is descending. Finally, make it user-friendly: print the word and what the numbers mean" + color.END)


### Alternative from class ####
print(color.GREEN + "Alternative from class:" + color.END)

def compare_origins2(word):
   add_word(word)
   proportion = (df_new.groupby("Origin")[word].sum() / df_new.groupby("Origin")[word].count() * 100).reset_index(name="Percentage")
   proportion["Percentage"] = round(proportion["Percentage"], 2)
   proportion["Percentage"] = proportion["Percentage"].astype(str) + "%"
   print(proportion)
compare_origins2(input("Write another word: "))


#You're done! Try out your function and paste your most interesting result
#as a comment

#
#
# Hint: note that df.groupby(["Origin"])[word].count() will get you the
# number of movies, grouped by origin.
