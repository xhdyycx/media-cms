from app.modules.cover.poster_gen_grid import gen_poster_workflow
from app.modules.cover.poster_gen_styles import gen_poster_workflow2, gen_poster_workflow3

def gen_poster_workflow_select(name, style):
    if style == 'style-1':
        return gen_poster_workflow(name)
    if style == 'style-2':
        return gen_poster_workflow2(name)
    if style == 'style-3':
        return gen_poster_workflow3(name)

if __name__ == '__main__':
    gen_poster_workflow('Anime')

