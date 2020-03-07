---
layout: post
title: Add to the website!
---
### Basic rundown of how to modify this website

## Step-by-step process for making a post:
1. Add .md file into the _posts folder
2. Include the following in the header:
```javascript
---
layout: post
title: [YOUR TITLE]
---
```
3. Name file accordingly: YEAR-MONTH-DAY-TITLE.md (no spaces!!)
4. Use github markdown. See link [here](https://raw.githubusercontent.com/barryclark/www.jekyllnow.com/gh-pages/_posts/2014-6-19-Markdown-Style-Guide.md)

## Local Development
This is to see your website react to your changes in realtime without having to git push.
Make sure you have Ruby installed. If not, follow this [tutorial](https://stackify.com/install-ruby-on-windows-everything-you-need-to-get-going/) (for Windows)

1. Install Jekyll and plug-ins in one fell swoop. `gem install github-pages` This mirrors the plug-ins used by GitHub Pages on your local machine including Jekyll, Sass, etc.
2. Clone down your fork `git clone https://github.com/yourusername/yourusername.github.io.git`
3. Serve the site and watch for markup/sass changes `jekyll serve`
4. View your website at http://127.0.0.1:4000/
5. Commit any changes and push everything to the master branch of your GitHub user repository. GitHub Pages will then rebuild and serve your website.
