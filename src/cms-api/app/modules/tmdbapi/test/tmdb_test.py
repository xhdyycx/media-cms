from app.modules.tmdbapi import TMDb, Movie, Search
if __name__ == '__main__':
    tmdb = TMDb()
    tmdb._base = 'https://tmdb.aliang.link'
    tmdb.api_key = '623cf1f96f2d0dabcb0895e020381f9e'
    tmdb.language = 'zh-CN'
    movie = Movie()
    search = Search()
    popular = search.movies(term = '肖申克的救赎', page = 1)
    print(popular)
    for p in popular:
        print(p.id)
        print(p.title)
        print(p.overview)
        print(f'''https://tmdb.aliang.link/t/p/original{p.poster_path}''')

