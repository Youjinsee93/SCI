from backend.variables.menu import menu
from backend.variables.menu import menu2

def copy_menu(num, resource, genre):
    menu_copy = menu.copy()
    menu_copy['num'] = num
    menu_copy['genre'] = genre
    menu_copy['question_resource'] = resource

    return menu_copy

def copy_menu2(num, resource, genre):
    menu2_copy = menu2.copy()
    menu2_copy['num'] = num
    menu2_copy['genre'] = genre
    menu2_copy['question_resource'] = resource

    return menu2_copy


problems = [copy_menu(1,'movie_scene/movie1.mp4', '영화 장면'),
            copy_menu2(2,'movie_scene/movie1.mp4', '영화 장면'),
            copy_menu(3,'movie_scene/movie2.mp4', '영화 장면'),
            copy_menu2(4,'movie_scene/movie2.mp4', '영화 장면'),
            copy_menu(5,'movie_scene/movie3.mp4', '영화 장면'),
            copy_menu2(6,'movie_scene/movie3.mp4', '영화 장면'),
            copy_menu(7,'movie_scene/movie4.mp4', '영화 장면'),
            copy_menu2(8,'movie_scene/movie4.mp4', '영화 장면'),
            copy_menu(9,'movie_scene/movie5.mp4', '영화 장면'),
            copy_menu2(10,'movie_scene/movie5.mp4', '영화 장면'),
            copy_menu(11, 'movie_scene/movie6.mp4', '영화 장면'),
            copy_menu2(12, 'movie_scene/movie6.mp4', '영화 장면'),
            copy_menu(13, 'movie_scene/movie7.mp4', '영화 장면'),
            copy_menu2(14, 'movie_scene/movie7.mp4', '영화 장면'),
            copy_menu(15, 'movie_scene/movie8.mp4', '영화 장면'),
            copy_menu2(16, 'movie_scene/movie8.mp4', '영화 장면'),
            copy_menu(17, 'movie_scene/movie9.mp4', '영화 장면'),
            copy_menu2(18, 'movie_scene/movie9.mp4', '영화 장면'),
            copy_menu(19, 'movie_scene/movie10.mp4', '영화 장면'),
            copy_menu2(20, 'movie_scene/movie10.mp4', '영화 장면'),
            ]

