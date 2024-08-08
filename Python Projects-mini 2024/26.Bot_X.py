import tweepy

# Replace with your Twitter API credentials
api_key = ''                  # Your Twitter API key
api_secret = ''               # Your Twitter API secret key
bearer_token = ''             # Your Twitter Bearer token
access_token = ''             # Your Twitter Access token
access_token_secret = ''      # Your Twitter Access token secret

# Initialize the tweepy client with the provided credentials
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Create a tweet with the specified text
response = client.create_tweet(text='Hola.')

# Print confirmation message
print('Tweet enviado')
