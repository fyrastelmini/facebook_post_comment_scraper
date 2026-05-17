from main import extract_post_id_from_url, fetch_comments_for_post, save_post_data
import pandas as pd
# Extract post ID
posts =[]
url_list = pd.read_csv("url.txt", header=None)[0].tolist()
#read content of url.txt
for url in url_list:

    post_id = extract_post_id_from_url(url)
    posts.append({'POST_ID': post_id, 'URL': url})
    # Fetch comments
    comments = fetch_comments_for_post(post_id)

pd.DataFrame(posts).to_csv("posts.csv", index=False)