from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample blog data
posts = {
    1: {
        "title": "First Blog Post",
        "date": "2025-01-11",
        "content": "This is the full content of the first blog post. Welcome to my blog!"
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

@app.route('/admin')
def admin_dashboard():
    return render_template('admin.html', posts=posts)

@app.route('/admin/create', methods=['POST'])
def create_post():
    new_id = max(posts.keys()) + 1 if posts else 1
    posts[new_id] = {
        "title": request.form['title'],
        "date": request.form['date'],
        "content": request.form['content']
    }
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if request.method == 'POST':
        posts[post_id]['title'] = request.form['title']
        posts[post_id]['date'] = request.form['date']
        posts[post_id]['content'] = request.form['content']
        return redirect(url_for('admin_dashboard'))
    return render_template('edit_post.html', post=posts[post_id], post_id=post_id)

@app.route('/admin/delete/<int:post_id>')
def delete_post(post_id):
    posts.pop(post_id, None)
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
