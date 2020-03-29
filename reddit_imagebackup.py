import os
import urllib.request
from urllib.parse import urlparse
import praw


def main():
    backup_directory = "C:\\Temp\\Reddit.ImageBackup.Test"
    reddit = praw.Reddit('ImageBackup-Bot', user_agent='script:Reddit.ImageBackup:v1.0.0 (by /u/gaben38)')
    subreddit = reddit.subreddit('smuggies')
    subreddit.quaran.opt_in()
    for submission in subreddit.hot(limit=10):
        if submission.stickied:
            continue
        print(f"[+{submission.score}] {submission.title}")
        print(f"URL: {submission.url}")

        download_file(backup_directory, submission.url)


def download_file(backup_directory: str, image_url: str, filename_override: str = None):
    parsed_url = urlparse(image_url)

    filename = filename_override if filename_override is not None else os.path.basename(parsed_url.path)
    print(f"Downloading file '{filename}'...")
    urllib.request.urlretrieve(image_url, os.path.join(backup_directory, filename))
    print("Download finished.")


if __name__ == "__main__":
    main()
