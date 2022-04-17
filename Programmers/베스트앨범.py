# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    answer = []
    musics = [(i,x) for i, x in enumerate(zip(genres, plays))]
    music_dict = {}
    genre_dict = {}
    for music in musics:
        music_dict.update({music[1][0] : []})
        genre_dict.update({music[1][0] : 0})
    for music_num, pref in musics:
        music_dict[pref[0]].append((music_num,pref[1]))
        genre_dict[pref[0]] += pref[1]
    for k, v in music_dict.items():
        temp = sorted(v,key=lambda x : x[1], reverse=True)
        music_dict.update( {k :  temp})
    sorted_genres = sorted(genre_dict.items(),key=lambda x: x[1],reverse=True)
    for genre in sorted_genres:
        for i, _ in music_dict[genre[0]][:2]:
            answer.append(i)
    return answer