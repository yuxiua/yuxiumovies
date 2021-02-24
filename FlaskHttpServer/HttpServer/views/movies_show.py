from flask import render_template,Blueprint,request
import os
import sys

currentpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#注意：调用这个路径是以调用他的py文件的文件夹
movie_path = os.path.join(currentpath,'static\movies')

movie = Blueprint('movies_show', __name__)#添加什么就在html中的url_for些什么，比如：movies_show.movieList

@movie.route('/movieList',methods=["GET", "POST"])
def movieList():
	if request.method == "GET":
		movies = []
		for file_name in os.listdir(movie_path):
			if file_name.split('.')[1] in ['mp4','avi']:
				movies_dic = {}
				movies_dic['file'] = file_name
				movies_dic['title'] = file_name.split('.')[0]
				movies.append(movies_dic)
			else:
				os.remove(f'{movie_path}\{file_name}')
		return render_template('movies.html', movies=movies)

