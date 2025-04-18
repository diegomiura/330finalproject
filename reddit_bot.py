import praw

# Function to post a fact to Reddit
# This function uses the PRAW library to interact with Reddit's API.
def post_fact_to_reddit(fact, creds, subreddit_name="astro330"):
    """
    Posts a fun astronomy fact to a specified subreddit on Reddit.
    Args:
        fact (str): The astronomy fact to post.
        creds (dict): A dictionary containing Reddit API credentials.
        subreddit_name (str): The name of the subreddit to post to.
    Returns:
        submission: The Reddit submission object.
    """
    # Check if the required credentials are provided
    if not all(key in creds for key in ["client_id", "client_secret", "username", "password", "user_agent"]):
        raise ValueError("Missing Reddit API credentials.")
    # Initialize the Reddit instance with the provided credentials
    reddit = praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        username=creds["username"],
        password=creds["password"],
        user_agent=creds["user_agent"]
    )

    # Check if the subreddit exists
    try:
        subreddit = reddit.subreddit(subreddit_name)
        if not subreddit:
            raise ValueError(f"Subreddit '{subreddit_name}' does not exist.")
    except Exception as e:
        raise ValueError(f"Error accessing subreddit '{subreddit_name}': {e}")
    
    # Post the fact to the subreddit
    submission = subreddit.submit(title="🌠 Astronomy Fun Fact", selftext=fact)
    
    # Print the submission URL for reference
    print(f"Posted to Reddit: {submission.url}")

    # Return the submission object
    return submission
