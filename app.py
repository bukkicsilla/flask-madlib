from flask import Flask, request, render_template
from random import choice
import stories

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10

story1 = stories.Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

story2 = stories.Story(
    ["adjective", "noun", "verb", "adverb", "adjective", "noun"], """Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree.
He {verb} {adverb} through the large tunnel that led to its {adjective} {noun}."""
)
story3 = stories.Story(
    ["noun", "verb", "adverb", "adjective"], """I love my {noun}. It {verb} {adverb}. I find it {adjective}."""
    )
madlib_stories = [story1, story2, story3]
#story = choice(madlib_stories)
#print(story.template)
#print("LENGTH", len(story.prompts))

@app.route("/")
def select_story():
    return render_template("select.html", length=len(madlib_stories))

@app.route("/home")
def home():
    #print("ARGS FROM SELECT", request.args)
    index = int(request.args["id"])
    story = madlib_stories[index]
    print("STORY", story.template)
    return render_template("home.html", prompts=story.prompts, length=len(story.prompts), story_id=index)

@app.route("/story")
def show_story():
    print(request.args)
    index = int(request.args["story_id"])
    story = madlib_stories[index]
    d = {}
    for i in range(len(story.prompts)):
        #print("INDEX", i)
        d[story.prompts[i]] = request.args[str(i)]
    madlib_story = story.generate(d)
    return render_template("story.html", madlib=madlib_story)
    #return render_template("story.html", madlib="MADLIB")

