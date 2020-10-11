import pandas as pd
import time 

tag = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/tags.csv')
rating = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/ratings.csv')
movie = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/movies.csv')
link = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/links.csv')
genome_score = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/genome-scores.csv')
genome_tag = pd.read_csv('C:/Users/lenovo/Desktop/培训作业/第一周/python/ml-25m/genome-tags.csv')

#用户数
users_tag = set(tag.userId)
users_rating = set(rating.userId)
users = users_tag|users_rating
print('一共有%s不同的用户' %(len(users)))

#电影数
movie_set = set(movie.movieId)
print('一共有%s不同的电影' %(len(movie_set)))

#电影种类
tag_set = set(genome_tag.tagId)
print('一共有%s不同的电影种类' %(len(tag_set)))

#外部链接
movie_link = set(link.movieId)
movie_unlink = movie_set - movie_link
print('一共有%s电影没有外部链接' %(len(movie_unlink)))
