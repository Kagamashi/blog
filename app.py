from flask import Flask, render_template

app = Flask(__name__)

# Sample blog data
posts = {
    1: {
        "title": "First Blog Post",
        "date": "January 11, 2025",
        "content": "This is the full content of the first blog post. Welcome to my blog!"
    },
    2: {
        "title": "Second Blog Post",
        "date": "January 12, 2025",
        "content": "This is the second blog post. More content coming soon!"
    }
}

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id, {
        "title": "Post Not Found",
        "date": "N/A",
        "content": "The requested blog post does not exist."
    })
    return render_template('post.html', post_title=post["title"], post_date=post["date"], post_content=post["content"])

if __name__ == '__main__':
    app.run(debug=True)
