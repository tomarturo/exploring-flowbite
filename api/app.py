from flask import Flask, render_template

app = Flask(__name__)

worknav = [
	{"name": "Overview",
	"path": "/", 
	"icon": "OV"},
	{"name": "Solutions Marketing", 
	"path": "solutions",
	"icon": "SM"},
	{"name": "Brand Kit",
	"path": "brand-kit",
	"icon": "BK"},
	{"name": "S'mores", 
	"path": "s'mores", 
	"icon": "DS"},
	{"name": "Field Reports", 
	"path": "field-reports", 
	"icon": "FR"},
]

personalnav = [
	{"name": "The Tom Blog",
	"path": "tom-blog",
	"icon": "TTB"},
	{"name": "PooPal",
	"path": "poo-pal",
	"icon": "PP"},
	{"name": "HeyTK",
	"path": "hey-tk",
	"icon": "HTK"},
	{"name": "Next Steps",
	"path": "next-steps",
	"icon": "NS"},
]

miscnav = [
	{"name": "About",
	"path": "about",
	"icon": "AB"},
	{"name": "Contact",
	"path": "contact",
	"icon": "CT"}
]

projectheader = {
    " ": {
        "title": "Welcome, Earthling",
        "company": "Tom Kurzeka",
		"year": "2023"
    },
    "solutions": {
        "title": "Solutions Marketing",
        "tag": ["b2b", "a/b testing", "strategy"],
        "company": "VistaPrint",
        "companyURL": "www.vistaprint.com",
		"year": "2023"
    },
}

context = {
	"worknav": worknav,
	"personalnav": personalnav,
	"miscnav": miscnav,
}

@app.route("/")
def index():
	selected_project = projectheader.get(" ")
	context["selected_project"] = selected_project
	return render_template("index.html", **context)

@app.route("/solutions")
def solutions():
	selected_project = projectheader.get("solutions")
	context["selected_project"] = selected_project
	return render_template("solutions.html", **context)

# if __name__ == '__main__':
# 	app.run(debug=True)
