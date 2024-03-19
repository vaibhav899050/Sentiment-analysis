import subprocess
import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download NLTK data
nltk.download('vader_lexicon')

# Function to analyze sentiment
def analyze_sentiment(filepaths):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []

    for filepath in filepaths:
        with open(filepath) as file:
            content = file.read()
            scores = analyzer.polarity_scores(content)
            sentiments.append(scores)

    return sentiments

# Function to display sentiment analysis results
def display_results(sentiments, dates):
    # Extract scores
    positivity = [score["pos"] for score in sentiments]
    negativity = [score["neg"] for score in sentiments]
    overall = [score["pos"] - score["neg"] for score in sentiments]

    # Plotting Positivity
    pos_figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
    pos_figure.update_traces(mode="lines+markers", line=dict(color="green", width=2), marker=dict(size=8, symbol="circle"))
    pos_figure.update_layout(title="Positivity Over Time", xaxis_title="Date", yaxis_title="Positivity Score",
                             yaxis=dict(tickvals=[i/10 for i in range(11)], showgrid=True),
                             height=500, width=800)  # Increase plot size

    # Plotting Negativity
    neg_figure = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
    neg_figure.update_traces(mode="lines+markers", line=dict(color="red", width=2), marker=dict(size=8, symbol="circle"))
    neg_figure.update_layout(title="Negativity Over Time", xaxis_title="Date", yaxis_title="Negativity Score",
                             yaxis=dict(tickvals=[i/10 for i in range(11)], showgrid=True),
                             height=500, width=800)  # Increase plot size

    # Plotting Overall Sentiment
    overall_figure = px.line(x=dates, y=overall, labels={"x": "Date", "y": "Overall Sentiment"})
    overall_figure.update_traces(mode="lines+markers", line=dict(color="blue", width=2), marker=dict(size=8, symbol="circle"))
    overall_figure.update_layout(title="Overall Sentiment Over Time", xaxis_title="Date", yaxis_title="Overall Sentiment Score",
                                  yaxis=dict(tickvals=[i/10 for i in range(-10, 11, 2)], showgrid=True),
                                  height=500, width=800)  # Increase plot size

    return pos_figure, neg_figure, overall_figure

# Main function
def main():
    st.title("Larsen & Tourbo - Sentiment Analysis")
    st.sidebar.title("Options")

    # Load file paths
    filepaths = sorted(glob.glob("diary/*.txt"))

    # Get dates from file names
    dates = [name.strip("diary\\").strip(".txt") for name in filepaths]

    # Sentiment analysis
    sentiments = analyze_sentiment(filepaths)

    # Display sentiment analysis results
    pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)

    # Display options in the sidebar
    realtime_checkbox = st.sidebar.checkbox("Realtime Analysis")
    if realtime_checkbox:
        fetch_button = st.sidebar.button("Fetch Data")

        if fetch_button:
            # Run Python file for fetching realtime data
            subprocess.run(["python", "runc.py"])
            st.markdown("---")
            st.subheader("Realtime Analysis Results")
            st.markdown("Realtime analysis results will be displayed here.")
            filepaths1 = "selenium-twitter-scraper-master/diary/new.txt"
            analyzer1 = SentimentIntensityAnalyzer()
            sentiments1 = []
            pos = 0
            neg = 0
            over = 0
            with open(filepaths1) as file:
                content1 = file.read()
                scores1 = analyzer1.polarity_scores(content1)
                pos = scores1["pos"]
                neg = scores1["neg"]
                over = pos-neg
            print(neg)
            realtime_fig = px.bar(x=["Positivity", "Negativity", "Overall Sentiment"],
                                  y=[pos,
                                     neg,
                                     over],
                                  labels={"x": "Sentiment", "y": "Average Score"},
                                  color=["Positivity", "Negativity", "Overall Sentiment"],
                                  color_discrete_map={"Positivity": "green", "Negativity": "red",
                                                      "Overall Sentiment": "blue"})
            st.plotly_chart(realtime_fig)
            st.subheader("Latest Public Opinions")
            postweets = []
            negtweets = []
            with open(filepaths1) as file:
                cont = file.read()
                finaltweeets = cont.split('@#$%\n')
                for tweets in finaltweeets:
                    newsc = analyzer1.polarity_scores(tweets)
                    if newsc["pos"]>newsc["neg"]:
                        postweets.append(tweets)
                    else:
                        negtweets.append(tweets)


            col1, col2 = st.columns(2)
            count = 1
            with col1:
                st.header("Positive Public Opinions")
                for tweet in postweets:
                    tweet = tweet.replace("\n", " ")
                    st.write(str(count)+". "+tweet)
                    count+=1

            # Display negative tweets
            count = 1
            with col2:

                st.header("Negative Public Opinions")
                for tweet in negtweets:
                    tweet = tweet.replace("\n", " ")
                    st.write(str(count)+". "+tweet)
                    count+=1




    # Display selected chart(s)
    display_mode = st.sidebar.checkbox("Positivity", value=True)
    display_negativity = st.sidebar.checkbox("Negativity", value=False)
    display_overall = st.sidebar.checkbox("Overall Sentiment", value=False)

    # Display selected chart(s)
    if display_mode:
        st.plotly_chart(pos_figure)
    if display_negativity:
        st.plotly_chart(neg_figure)
    if display_overall:
        st.plotly_chart(overall_figure)

if __name__ == "__main__":
    main()
