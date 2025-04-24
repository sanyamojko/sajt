from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Створення екземпляру Flask
app = Flask(__name__)

# Налаштування SQLite бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'  # База даних SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Модель коментаря
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(50), nullable=False)  # Сторінка, до якої відноситься коментар
    topic = db.Column(db.String(100), nullable=False)  # Тема коментаря
    content = db.Column(db.Text, nullable=False)  # Зміст коментаря

    def __repr__(self):
        return f"Comment('{self.topic}', '{self.page}')"


# Створення таблиць, якщо вони не існують
with app.app_context():
    db.create_all()


# Роут для головної сторінки
@app.route('/')
def index():
    return render_template('index.html')


# Роут для сторінки st1
@app.route('/st1', methods=['GET', 'POST'])
def st1():
    if request.method == 'POST':
        topic = request.form['topic']
        content = request.form['content']
        new_comment = Comment(page='st1', topic=topic, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('st1'))

    comments = Comment.query.filter_by(page='st1').all()
    return render_template('st1.html', comments=comments)


# Роут для сторінки st2
@app.route('/st2', methods=['GET', 'POST'])
def st2():
    if request.method == 'POST':
        topic = request.form['topic']
        content = request.form['content']
        new_comment = Comment(page='st2', topic=topic, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('st2'))

    comments = Comment.query.filter_by(page='st2').all()
    return render_template('st2.html', comments=comments)


# Роут для сторінки st3
@app.route('/st3', methods=['GET', 'POST'])
def st3():
    if request.method == 'POST':
        topic = request.form['topic']
        content = request.form['content']
        new_comment = Comment(page='st3', topic=topic, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('st3'))

    comments = Comment.query.filter_by(page='st3').all()
    return render_template('st3.html', comments=comments)


# Роут для редагування коментаря
@app.route('/edit_comment/<int:id>', methods=['GET', 'POST'])
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    if request.method == 'POST':
        comment.topic = request.form['topic']
        comment.content = request.form['content']
        db.session.commit()
        return redirect(url_for(comment.page))

    return render_template('edit_comment.html', comment=comment)


# Роут для видалення коментаря
@app.route('/delete_comment/<int:id>', methods=['GET', 'POST'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for(comment.page))


if __name__ == '__main__':
    app.run(debug=True)
