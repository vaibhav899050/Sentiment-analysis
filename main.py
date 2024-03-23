import subprocess
import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from datetime import datetime

# Download NLTK data
nltk.download('vader_lexicon')

# Function to analyze sentiment
def analyze_sentiment(filepaths, encoding):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []

    for filepath in filepaths:
        with open(filepath, encoding=encoding) as file:
            content = file.read()
            scores = analyzer.polarity_scores(content)
            sentiments.append(scores)

    return sentiments


# Function to display sentiment analysis results
def display_results(sentiments, dates):
    # Extract scores
    # print(sentiments)
    positivity = [score["pos"] for score in sentiments]
    negativity = [score["neg"] for score in sentiments]
    overall = [score["pos"] - score["neg"] for score in sentiments]

    datetime_dates = [datetime.strptime(date, "%Y-%m") for date in dates]

    # Format dates with abbreviated month names
    formatted_dates = [date.strftime("%b'%y") for date in datetime_dates]
    print(formatted_dates)
    # Plotting Positivity
    pos_figure = px.line(x=formatted_dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
    pos_figure.update_traces(mode="lines+markers", line=dict(color="green", width=2), marker=dict(size=8, symbol="circle"))
    pos_figure.update_layout(title="Positivity Over Time", xaxis_title="Date", yaxis_title="Positivity Score",
                             yaxis=dict(tickvals=[i/10 for i in range(11)], showgrid=True),
                             height=500, width=800)  # Increase plot size

    # Plotting Negativity
    neg_figure = px.line(x=formatted_dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
    neg_figure.update_traces(mode="lines+markers", line=dict(color="red", width=2), marker=dict(size=8, symbol="circle"))
    neg_figure.update_layout(title="Negativity Over Time", xaxis_title="Date", yaxis_title="Negativity Score",
                             yaxis=dict(tickvals=[i/10 for i in range(11)], showgrid=True),
                             height=500, width=800)  # Increase plot size

    # Plotting Overall Sentiment
    overall_figure = px.line(x=formatted_dates, y=overall, labels={"x": "Date", "y": "Overall Sentiment"})
    overall_figure.update_traces(mode="lines+markers", line=dict(color="blue", width=2), marker=dict(size=8, symbol="circle"))
    overall_figure.update_layout(title="Overall Sentiment Over Time", xaxis_title="Date", yaxis_title="Overall Sentiment Score",
                                  yaxis=dict(tickvals=[i/10 for i in range(-10, 11, 2)], showgrid=True),
                                  height=500, width=800)  # Increase plot size

    return pos_figure, neg_figure, overall_figure

# Main function
def main():
    st.title("Larsen & Toubro\nSentiment Analysis")
    st.subheader("Sentiment Analysis for different social media platforms")

    c1, c2, c3 = st.columns(3)
    with c1:
        tb=st.button("Twitter")
    with c2:
        fb=st.button("FaceBook")
    with c3:
        mc=st.button("Money Control")
    c4, c5, c6 = st.columns(3)
    with c4:
        li = st.button("LinkedIn")
    with c5:
        ft= st.button("Financial Times")
    with c6:
        sa=st.button("Stocks Prediction")


    ss = st.subheader("OverAll Sentiment analysis")
    st.sidebar.title("Options")

    if sa:
        ss.subheader("Larsen and Toubro Stocks Prediction")
        st.image("graph_st.png")

    # Load file paths
    filepaths = sorted(glob.glob("diary/*.txt"))

    # Get dates from file names
    dates = [name.strip("diary\\").strip(".txt") for name in filepaths]
    print(dates[0])

    # Sentiment analysis
    sentiments = analyze_sentiment(filepaths, 'utf-8')

    # Display sentiment analysis results
    pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)

    # Display options in the sidebar
    realtime_checkbox = st.sidebar.checkbox("Realtime Analysis + Public Opinions")
    ns = st.sidebar.checkbox("News Analysis")
    if ns:
        ss.header("Latest News Analysis")
        filepaths1 = "nc.txt"
        analyzer1 = SentimentIntensityAnalyzer()
        sentiments1 = []
        pos = 0
        neg = 0
        over = 0
        with open(filepaths1, encoding='utf-8') as file:
            content1 = file.read()
            scores1 = analyzer1.polarity_scores(content1)
            pos = scores1["pos"]
            neg = scores1["neg"]
            over = pos - neg
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

        postweets = []
        negtweets = []
        with open(filepaths1, encoding='utf-8') as file:
            cont = file.read()
            finaltweeets = cont.split('\n')
            for tweets in finaltweeets:
                newsc = analyzer1.polarity_scores(tweets)
                if newsc["neg"]<0.05:
                    postweets.append(tweets)
                else:
                    negtweets.append(tweets)

        col1, col2 = st.columns(2)
        count = 1
        with col1:
            st.header("Positive News")
            for tweet in postweets:
                tweet = tweet.replace("\n", " ")
                st.write(str(count) + ". " + tweet)
                count += 1

        # Display negative tweets
        count = 1
        with col2:

            st.header("Negative News")
            for tweet in negtweets:
                tweet = tweet.replace("\n", " ")
                st.write(str(count) + ". " + tweet)
                count += 1

    if realtime_checkbox:
        st.subheader("Realtime Analysis Results")
        st.markdown("Click on the FETCH DATA button for realtime sentiment analysis")
        fetch_button = st.button("Fetch Data")


        if fetch_button:
            # Run Python file for fetching realtime data
            st.subheader("Fetching and translating data for realtime analysis.......")
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
    display_negativity = st.sidebar.checkbox("Negativity", value=True)
    display_overall = st.sidebar.checkbox("Overall Sentiment", value=True)
    display_comb = st.sidebar.checkbox("Positive+Negative", value=True)

    def dis(pos, neg, ov):
        if display_mode:
            st.plotly_chart(pos_figure)
        if display_negativity:
            st.plotly_chart(neg_figure)
        if display_overall:
            st.plotly_chart(overall_figure)

    if tb:
        ss.subheader("Analysis of Twitter data of last one Year")
        filepaths = sorted(glob.glob("diary/*.txt"))

        # Get dates from file names
        dates = [name.strip("diary\\").strip(".txt") for name in filepaths]
        print(dates[0])

        # Sentiment analysis
        sentiments = analyze_sentiment(filepaths, 'utf-8')

        # Display sentiment analysis results
        pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)
        dis(pos_figure, neg_figure, overall_figure)
    if mc:
        ss.subheader("Analysis of Money Control of last 5 Years")
        filepaths = sorted(glob.glob("diary_link/*.txt"))

        # Get dates from file names
        dates = [name.strip("diary_link\\").strip(".txt") for name in filepaths]
        print(dates[0])

        # Sentiment analysis
        sentiments = analyze_sentiment(filepaths, 'windows-1252')

        # Display sentiment analysis results
        pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)
        dis(pos_figure, neg_figure, overall_figure)

    if ft:
        ss.subheader("Analysis of Financial Times of last 5 Years")
        filepaths = sorted(glob.glob("diary_et/*.txt"))

        # Get dates from file names
        dates = [name.strip("diary_et\\").strip(".txt") for name in filepaths]
        print(dates[0])

        # Sentiment analysis
        sentiments = analyze_sentiment(filepaths, 'windows-1252')

        # Display sentiment analysis results
        pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)
        dis(pos_figure, neg_figure, overall_figure)

    if fb:
        ss.subheader("Analysis of FaceBook of last 4 Years")
        filepaths = sorted(glob.glob("diary_facebook/*.txt"))

        # Get dates from file names
        dates = [name.strip("diary_facebook\\").strip(".txt") for name in filepaths]
        print(dates[0])

        # Sentiment analysis
        sentiments = analyze_sentiment(filepaths, 'windows-1252')

        # Display sentiment analysis results
        pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)
        dis(pos_figure, neg_figure, overall_figure)

    if li:
        ss.subheader("Analysis of LinkedIn of last 4 Years")
        filepaths = sorted(glob.glob("diary_money/*.txt"))

        # Get dates from file names
        dates = [name.strip("diary_money\\").strip(".txt") for name in filepaths]
        print(dates[0])

        # Sentiment analysis
        sentiments = analyze_sentiment(filepaths, 'windows-1252')

        # Display sentiment analysis results
        pos_figure, neg_figure, overall_figure = display_results(sentiments, dates)
        dis(pos_figure, neg_figure, overall_figure)
    if display_mode:
        st.plotly_chart(pos_figure)
    if display_negativity:
        st.plotly_chart(neg_figure)
    if display_overall:
        st.plotly_chart(overall_figure)

    # Display selected chart(s)



if __name__ == "__main__":
    main()
