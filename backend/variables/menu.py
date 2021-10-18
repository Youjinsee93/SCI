menu = {
        'num': 1,
        'question_text': '왼쪽의 짧은 영상을 시청 후, 느꼈던 감정에 대하여 표현/선택해주세요. 혹시 제시된 단어가 없다면 가장 비슷한 단어를 선택후, 기타란에 자유롭게 적어주세요.',
        'question_resource': 'movie_scene/movie1.mp4',
        'question_type': 'word-select',
        'question_sign': 'movie_scene/movie2.mp4',
        'genre': '영화 장면',
        'answer_selection': [
            {
                'label': '즐거운',
                'color': '#FFF2CC',
                'sign_video': 'emotion/enjoy.mp4',
             },
            {
                'label': '기쁜',
                'color': '#FFF2CC',
                'sign_video': 'emotion/pleased.mp4',
            },
            {
                'label': '쾌활한',
                'color': '#FFF2CC',
                'sign_video': 'emotion/cheerful.mp4',
            },
            {
                'label': '욕망의',
                'color': '#FFF2CC',
                'sign_video': 'emotion/greedy.mp4',
            },
            {
                'label': '아름다운',
                'color': '#FFF2CC',
                'sign_video': 'emotion/beautiful.mp4',
            },
            {
                'label': '차분한',
                'color': '#FFF2CC',
                'sign_video': 'emotion/calm.mp4',
            },
            {
                'label': '평화로운',
                'color': '#FFF2CC',
                'sign_video': 'emotion/peaceful.mp4',
            },
            {
                'label': '강한',
                'color': '#FFF2CC',
                'sign_video': 'emotion/strong.mp4',
            },

            {
                'label': '감동한',
                'color': '#FFF2CC',
                'sign_video': 'emotion/moving.mp4',
            },
            {
                'label': '믿음직한',
                'color': '#FFF2CC',
                'sign_video': 'emotion/trusted.mp4',
            },
            {
                'label': '기대되는',
                'color': '#FFF2CC',
                'sign_video': 'emotion/anticipant.mp4',
            },

            {
                'label': '불안한',
                'color': '#F08080',
                'sign_video': 'emotion/anxiety.mp4',
            },
            {
                'label': '걱정되는',
                'color': '#F08080',
                'sign_video': 'emotion/worried.mp4',
            },
            {
                'label': '무서운',
                'color': '#F08080',
                'sign_video': 'emotion/scared.mp4',
            },
            {
                'label': '싫은',
                'color': '#F08080',
                'sign_video': 'emotion/hated.mp4',
            },
            {
                'label': '짜증나는',
                'color': '#F08080',
                'sign_video': 'emotion/annoying.mp4',
            },
            {
                'label': '화난',
                'color': '#F08080',
                'sign_video': 'emotion/angry.mp4',
            },
            {
                'label': '경계되는',
                'color': '#F08080',
                'sign_video': 'emotion/alert.mp4',
            },
            {
                'label': '반항적인',
                'color': '#F08080',
                'sign_video': 'emotion/rebel.mp4',
            },
            {
                'label': '지루한',
                'color': '#F08080',
                'sign_video': 'emotion/boring.mp4',
            },
            {
                'label': '슬픈',
                'color': '#F08080',
                'sign_video': 'emotion/sad.mp4',
            },
            {
                'label': '우울한',
                'color': '#F08080',
                'sign_video': 'emotion/depressed.mp4',
            },
            {
                'label': '혐오스러운',
                'color': '#F08080',
                'sign_video': 'emotion/disguisting.mp4',
            },
            {
                'label': '놀란',
                'color': '#F08080',
                'sign_video': 'emotion/surprised.mp4',
            },
            {
                'label': '아무런 감정이 들지 않는다',
                'color': '#B4C7E7',
                'sign_video': 'emotion/neutral.mp4',
            },
        ],
        'user_input': True
    }

menu2 = {
        'num': 3,
        'question_text': '앞에서 선택한 감정 단어에 대한 간단한 설문을 진행해주세요.',
        'question_resource': '1.Amusing/1-2.gif',
        'question_type': 'word-evaluation',
        'question_sign': '1.Amusing/1-6.mp4',
        'genre': '드라마',
        'user_input': False
    }