import csv

from categories.models import Category, Genre, Title, TitleGenre
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import Comment, Review

User = get_user_model()


class Command(BaseCommand):
    help = 'load data from csv files'

    def handle_1(self, *args, **options):
        with open('static\\data\\users.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                username = row['username']
                email = row['email']
                role = row['role']
                bio = row['bio']
                first_name = row['first_name']
                last_name = row['last_name']
                users = User(
                    id=id,
                    username=username,
                    email=email,
                    role=role,
                    bio=bio,
                    first_name=first_name,
                    last_name=last_name,
                )
                users.save()

    def handle_2(self, *args, **options):
        with open('static\\data\\review.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                title_id = row['title_id']
                text = row['text']
                author = row['author']
                score = row['score']
                pub_date = row['pub_date']
                reviews = Review(
                    id=id,
                    title_id=title_id,
                    text=text,
                    author=author,
                    score=score,
                    pub_date=pub_date,
                )
                reviews.save()

    def handle_3(self, *args, **options):
        with open('static\\data\\comments.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                review_id = row['review_id']
                text = row['text']
                author = row['author']
                pub_date = row['pub_date']
                comments = Comment(
                    id=id,
                    review_id=review_id,
                    text=text,
                    author=author,
                    pub_date=pub_date,
                )
                comments.save()

    def handle_4(self, *args, **options):
        with open('static\\data\\titles.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                year = row['year']
                category = row['category']
                titles = Title(
                    id=id,
                    name=name,
                    year=year,
                    category=category,
                )
                titles.save()

    def handle_5(self, *args, **options):
        with open('static\\data\\category.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                slug = row['slug']
                categories = Category(
                    id=id,
                    name=name,
                    slug=slug,
                )
                categories.save()

    def handle_6(self, *args, **options):
        with open('static\\data\\genre.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                slug = row['slug']
                genres = Genre(
                    id=id,
                    name=name,
                    slug=slug,
                )
                genres.save()

    def handle_7(self, *args, **options):
        with open('static\\data\\genre_title.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                title_id = row['title_id']
                genre_id = row['genre_id']
                genre_titles = TitleGenre(
                    id=id,
                    title_id=title_id,
                    genre_id=genre_id,
                )
                genre_titles.save()
