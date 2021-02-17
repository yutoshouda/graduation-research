from flask import Flask

@app.route("/")
def hello():

    tmp0 = "sakurai"
    #tmp1 = 10000

    return render_template('3page.html',kyouin = tmp0)
    #return render_template ('3page.html',kakuritu = tmp1)

