test = {   'name': 'q1_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> top_social_apps_by_content_rating.shape[0] == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> top_social_apps_by_content_rating.shape[1] == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> top_social_apps_by_content_rating.columns[0] == 'Num_Top_Social_Apps'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> top_social_apps_by_content_rating.get('Num_Top_Social_Apps').sum() == 224\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> top_social_apps_by_content_rating.get('Num_Top_Social_Apps').iloc[0] == 92\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
