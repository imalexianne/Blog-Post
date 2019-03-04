from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for,abort
# from ..models import User,PhotoProfile
from ..models import Blogpost, Comment, User, Subscriber, Quote
from .forms import BlogpostForm, CommentForm,SubscriberForm
# from .forms import ReviewForm,UpdateProfile
from .. import db,photos
import markdown2 
from ..request import get_quotes




# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @main.route('/')
# def index():
#     '''
#     function that returns the index page
#     '''
#     quote = get_quotes()
#     blogs = Blog.query.all()
#     return render_template('index.html', blogs = blogs, quote=quote)

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    quote = get_quotes()
    # blogs = Blog.query.all()

    blogposts = Blogpost.get_blogposts(id)
    comments = Comment.get_comments()
    subscribers = Subscriber.get_subscribers(id)
    title = 'Home - Welcome to The best Blogposts Review Website Online'

    return render_template('index.html', title = title, blogposts=blogposts,comments= comments, quote=quote, subscribers=subscribers)




@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


# @login_required
# def new_review(id):

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blogpost/new', methods = ['GET','POST'])
@login_required
def new_blogpost():
    form = BlogpostForm()
    
    if form.validate_on_submit():
        # title = form.title.data
        description_path = form.description_path.data
        category = form.category.data
        posted = form.posted.data

        # Updated review instance
        new_blogpost = Blogpost(description_path=description_path, category=category,posted=posted, user_id= current_user.id)

        # save review method
        new_blogpost.save_blogpost()
        return redirect(url_for('.index',description_path = description_path ))

    # title = f'{movie.title} review'
    return render_template('new_blogpost.html', blogpost_form=form)





@main.route('/blogpost/<int:id>')
def single_blogpost(id):
    login_required
    blogpost=Blogpost.query.get(id)
    if blogpost is None:
        abort(404)
    format_blogpost = markdown2.markdown(blogpost.user_blogpost,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blogpost.html',blogpost = blogpost,format_blogpost=format_blogpost)



@main.route('/blogpost')
def diplay_blogpost():
   blogposts = Blogpost.get_blogposts()
   print(blogposts)
   return render_template("new_blogpost.html",blogposts = blogposts)


@main.route('/comment/new',methods= ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        description_all = form.description_all.data
        
        

        # Updated review instance
        new_comment = Comment(description_all=description_all,user_id=current_user.id)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.index',description_all=description_all ))

 
    return render_template('new_comment.html', comment_form=form)

@main.route('/comment',methods= ['GET','POST'])
@main.route('/comment')
def diplay_comment():
   comments = Comment.get_comments()
   print(comments)
   return render_template("comment.html",comments = comments)

@main.route('/del-comment/<id>')
@login_required
def delcomment(id):
    '''
    function to delete comments
    '''
    comment = Comment.query.filter_by(id = id).first()
    db.session.delete(comment)
    db.session.commit()
    print(comment)
    title = 'delete comments'
    return render_template('delete.html',title = title, comment = comment)

@main.route('/subscribe',methods=["GET","POST"])
def subscriber():
    form=SubscriberForm()

    if form.validate_on_submit():
        subscriber = Subscriber(name=form.name.data,email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to my blogpost","email/welcome_user",subscriber.email,subscriber=subscriber)
        flash('A confirmation by email has been sent to you by email')
        return redirect(url_for('main.index'))
        title = 'Subscribe'
    return render_template('subscription.html',form=form)


@main.route('/blogpost/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blogpost(id):
    """
    Edit a blogpost in the database
    """
    new_blogpost=False

    blogpost = Blogpost.query.get(id)
    form = BlogpostForm()

    if form.validate_on_submit():

        blogpost.blogpost = form.blogpost.data

        db.session.commit()

        print('edited comment ')


        return redirect(url_for('main.index'))

    form.blogpost.data = blogpost.blogpost


    return render_template('new_blogpost.html',
                           action = 'Edit',
                           new_blogpost = new_blogpost,
                           blogpost_form = form,
                           legend='Update Post')