import markdown
import os

f = open('templates/index_template.html', 'r')
index_template = f.read().split('SPLIT')
f.close

f = open('templates/post_template.html', 'r')
post_template = f.read().split('SPLIT')
f.close

index_page = index_template[0]

posts = dict()

for filename in os.scandir('src'):
    f = open(filename.path, 'r')
    content = f.read()
    title = content.splitlines()[0][1:].strip() # get title
    post = markdown.markdown(content)
    f.close()

    last_mod = os.stat(filename.path).st_mtime
    posts[last_mod] = (filename.path[4:-2], title, post)

index = list(posts.keys())
index.sort()

for i in index:
    # add to index page
    index_page += "\n <p> <a href = \"posts/" + posts[i][0] + "html\"> " + posts[i][1] + " </a> </p>"

    post = post_template[0] + posts[i][1] + post_template[1] + posts[i][2] + post_template[2]
    with open('posts/' + posts[i][0] + 'html', 'w') as f:
        f.write(post)

index_page += "\n" + index_template[1]
with open('index.html', 'w') as f:
    f.write(index_page)




