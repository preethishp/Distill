from flask import Flask, render_template
import tweepy
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search/<query>')
def search_twitter(query):
    auth = tweepy.OAuthHandler('cbCXqKyjSMbuRbJohFhqFV4XN', 'PjrfzMCgf0q3208KY9rSXqn2kRNCNbTt2zncv3gl5ZPFMa7Vq9')
    auth.set_access_token('277271827-TsTALivgB7EBwg1ujzqmyyRcKs8r1ggbgXO3fe5I', 'uIzjxMRAeZ6eOFGvedp8POtaR8rGLGs6yziefI6qIabhv')
    api = tweepy.API(auth)
    max_tweets = 10
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    return searched_tweets.__str__()


if __name__ == '__main__':
    app.run()
