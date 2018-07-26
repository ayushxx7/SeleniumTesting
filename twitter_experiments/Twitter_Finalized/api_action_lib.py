import tweepy
import pandas as pd
import time
from file_path import user_keys_excel,user_tweets_excel
user_keys_dataframe = pd.read_excel(user_keys_excel)

def api_dict_creation(user_keys_dataframe):
    '''
    args: user_keys_dataframe
    Api Dictionary creation from excel file
    return : api_dict
    '''
    api_dict = {}
    for username in user_keys_dataframe.username:
        row = user_keys_dataframe[user_keys_dataframe.username == username]
        consumer_key = row.consumer_key.tolist()[0]
        consumer_secret = row.consumer_secret.tolist()[0]
        access_token = row.access_token.tolist()[0]
        access_token_secret = row.access_token_secret.tolist()[0]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api_dict[username] = api
    return api_dict
#print(api_dict)
api_dict = api_dict_creation(user_keys_dataframe) ## NEEDS IMPROVEMENT

def follow_each_other(user_keys_dataframe, api_dict):
    '''
    args : user_keys_dataframe, api_dict
    Follows the account by picking up the all the username from the dictionary except the current username
    Return : None
    '''
    for current_username in api_dict.keys():
        ## POSSIBLE TO USE api_dict here as well?
        # for other_username in api_dict.keys():
        # if other_username != current_username
        for other_username in user_keys_dataframe[user_keys_dataframe.username != current_username]['username']:
            try:
                api_dict[current_username].create_friendship(api_dict[other_username].me().screen_name)
                print(current_username, " follows ", other_username)
            except:
                print(current_username, " already follows ", other_username)

def create_tweet_file(user_keys_dataframe): #### use when tweet file empty
    '''
    args : api_dict,
    read api excel, copy user column and write to new tweet excel file
    use this tweet file, write tweets in new column called tweets,
    Return : None
    '''
    # writer = pd.ExcelWriter("excel_files/user_tweets.xlsx") < DISABLING THIS
    df = pd.DataFrame()
    for username in user_keys_dataframe.username:
        df["username"] = user_keys_dataframe.username
        df['tweet'] = ""
        df.to_excel("excel_files/user_tweets.xlsx")
    print(df)
    # df.to_excel(user_tweets_excel) # < MADE THIS WORK

user_tweets = pd.read_excel(user_tweets_excel)

def tweet_to_dictionary():
    return {i:j for i, j in zip(user_tweets.username, user_tweets.tweet)}

# tweet_dict = tweet_to_dictionary()
# for i in tweet_dict.keys():
#     print(i)
#     print(tweet_dict[i])
#update status
def update_status_from_excel():
    '''
args : api_dict,
Opens the excel file, picks up the tweets and tweets for the current username
Return : None

# read_login_credentials()
    '''
    tweet_dict = tweet_to_dictionary()
    for user in tweet_dict.keys():
        print("User",user,'tweeting from excel')
        # try:
        tweet_text = "dude come on:" + tweet_dict[user]
        print(tweet_text)
        tweet = api_dict[user].update_status(tweet_text)
        print(tweet.text)
        # except:
        #     print("STATUS IS DUPLICATE ERROR")


    # for current_username in df.username:
    #     print(current_username)
    #     try:
    #         tweet = api_dict[current_username].update_status("A different format to update my username:",df[df.username == current_username]['tweet'])
    #     except:
    #         print("STATUS IS DUPLICATE ERROR")
    #     print(tweet.text)

#update status & #retweet
def tweet_retweet(tweet_text = 'I am a sample tweet', wait_interval = 0):
    '''
    Args: tweet_text
    This function tweets a particular tweet from multiple accounts
    Then it retweet that tweet from other accounts.
    Returns: None
    '''
    for current_username in api_dict.keys():
        print(current_username)
        tweet = api_dict[current_username].update_status(tweet_text)
        print(tweet.text)
        '''
        for other_username in api_dict.keys():
            if(other_username != current_username):
        '''
        for other_username in user_keys_dataframe[user_keys_dataframe.username != current_username]['username']:
            try:
                api_dict[other_username].retweet(tweet.id)
                # api_dict[other_username].create_favorite(tweet.id)
                print(other_username, " Retweets ", current_username , "Tweet text:", tweet.text)
                if wait_interval != 0:
                    print(f"Waiting for {wait_interval} seconds")
                    time.sleep(wait_interval)
            except Exception as e:
                print('ERROR:',e,'from id',other_username,'on retweeting',tweet.text)

def tweet_like(tweet_text = 'I am a sample tweet', wait_interval = 0):
    '''
    Args: tweet_text
    This function tweets a particular tweet from multiple accounts
    Then it retweet that tweet from other accounts.
    Returns: None
    '''
    for current_username in api_dict.keys():
        print(current_username)
        tweet = api_dict[current_username].update_status(tweet_text)
        print(tweet.text)
        '''
        for other_username in api_dict.keys():
            if(other_username != current_username):
        '''
        for other_username in user_keys_dataframe[user_keys_dataframe.username != current_username]['username']:
            try:
                # api_dict[other_username].retweet(tweet.id)
                api_dict[other_username].create_favorite(tweet.id)
                print(other_username, " Retweets ", current_username , "Tweet text:", tweet.text)
                if wait_interval != 0:
                    print(f"Waiting for {wait_interval} seconds")
                    time.sleep(wait_interval)
            except Exception as e:
                print('ERROR:',e,'from id',other_username,'on retweeting',tweet.text)


# def un_tweet_retweet(tweet_text = 'I am a sample tweet'):
#     '''
#     Args: tweet_text
#     This function tweets a particular tweet from multiple accounts
#     Then it retweet that tweet from other accounts.
#     Returns: None
#     '''
# # probably will use destroy_status

#     for current_username in api_dict.keys():
#         print(current_username)
#         # tweet = api_dict[current_username].update_status(tweet_text)
#         # print(tweet.text)
#         for other_username in user_keys_dataframe[user_keys_dataframe.username != current_username]['username']:
#             try:
#                 # api_dict[other_username].unretweet(tweet.id)
#                 print(other_username, " Retweets ", current_username , "Tweet text:", tweet.text)
#             except Exception as e:
#                 print('ERROR:',e,'from id',other_username,'on retweeting',tweet.text)

# create_tweet_file()
# update_status_from_excel()
def update_same_status(tweet_text, wait_interval = 0):
    for current_username in api_dict.keys():
        tweet = api_dict[current_username].update_status(tweet_text)
        print(f"{current_username}'s status is updated")
        if wait_interval != 0 and current_username != list(api_dict.keys())[-1]:
            print(f"Waiting for {wait_interval} seconds")
            time.sleep(wait_interval)
def destroy_top_status():
    for current_username in api_dict.keys():
        print(current_username)
        for tweet in tweepy.Cursor(api_dict[current_username].user_timeline).items(1):
            print(tweet.text)
            api_dict[current_username].destroy_status(tweet.id)

def like_top_status():
    for current_username in api_dict.keys():
        print(current_username)
        for tweet in tweepy.Cursor(api_dict[current_username].user_timeline).items(1):
            print(tweet.text)
            api_dict[current_username].create_favorite(tweet.id)
def retweet_top_status():
    for current_username in api_dict.keys():
        print(current_username)
        for tweet in tweepy.Cursor(api_dict[current_username].user_timeline).items(1):
            print(tweet.text)
            api_dict[current_username].retweet(tweet.id)


# follow_each_other(user_keys_dataframe, api_dict)
tweet_retweet("What exactly is #DigitalBikaner ? Can someone please explain to me?",1)
# print(tweet_id_dict)
# update_status_from_excel()
# create_tweet_file(user_keys_dataframe)
# update_same_status("'Live for an ideal and that one ideal alone. Let it be so great, so strong, that there may be nothing else left in the mind; no place for anything else, no time for anything else.' -Swami Vivekananda", 2)
# destroy_top_status()
# like_top_status()
# retweet_top_status()
