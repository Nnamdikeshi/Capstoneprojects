# Gather user sentence
user_put = input("Type a sentence: ")

# Using the .title() function we capitilize each word
user_put = user_put.title()

# Print to check if it worked
print ("Here's each word capitilized: ", user_put)

# Using the .split() function we join our string
user_put = ''.join(user_put.split())

# Print to check if it worked
print ("Here's your sentence joined: ", user_put)

# Lowercase the first letter in the string
user_put = user_put[0].lower() + user_put[1:]

#Print to see if it worked
print ("Here's the sentence with the first letter lowercase: ", user_put)