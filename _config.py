######################################################################
# This is the main Blogofile configuration file.
# www.Blogofile.com
#
# This file has the following ordered sections:
#  * Basic Settings
#  * Intermediate Settings
#  * Advanced Settings
#
#  You really only _need_ to change the Basic Settings.
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site_url         = "http://jmjeong.com"

#### Blog Settings ####

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog_enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog_path = ""

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog_name        = "Jaemok"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog_description = u"jmjeong, Jaemok Jeong"

## blog_timezone -- the timezone that you normally write your blog posts from
blog_timezone    = "ROK"

## blog_posts_per_page -- Blog posts per page
blog_posts_per_page = 5

# Automatic Permalink
# (If permalink is not defined in post article, it's generated
#  automatically based on the following format:)
# Available string replacements:
# :year, :month, :day -> post's date
# :title              -> post's title
# :uuid               -> sha hash based on title
# :filename           -> article's filename without suffix
blog_auto_permalink_enabled = True
# This is relative to site_url
blog_auto_permalink         = "/blog/:filename"

######################################################################
# Intermediate Settings
######################################################################
#### Disqus.com comment integration ####
disqus_enabled = True
disqus_name    = "jmjeong"

#### Emacs Integration ####
emacs_orgmode_enabled = True
# emacs binary (orgmode must be installed)
emacs_binary    = "/Applications/Emacs.app/Contents/MacOS/Emacs"               # emacs 22 or 23 is recommended
emacs_preload_elisp = "_emacs/setup.el"          # preloaded elisp file
emacs_orgmode_preamble = r"#+OPTIONS: H:3 num:nil toc:nil \n:nil"   # added in preamble

#### Blog post syntax highlighting ####
syntax_highlight_enabled = True
# You can change the style to any builtin Pygments style
# or, make your own: http://pygments.org/docs/styles
syntax_highlight_style   = "murphy"

#### Custom blog index ####
# If you want to create your own index page at your blog root
# turn this on. Otherwise blogofile assumes you want the
# first X posts displayed instead
blog_custom_index = False

#### Post excerpts ####
# If you want to generate excerpts of your posts in addition to the
# full post content turn this feature on
post_excerpt_enabled     = True
post_excerpt_word_length = 50
#Also, if you don't like the way the post excerpt is generated
#You can define a new function
#below called post_excerpt(content, num_words)

#### Blog pagination directory ####
# blogofile places extra pages of your blog in
# a secondary directory like the following:
# http://www.yourblog.com/blog_root/page/4
# You can rename the "page" part here:
blog_pagination_dir = "page"

#### Blog category directory ####
# blogofile places extra pages of your or categories in
# a secondary directory like the following:
# http://www.yourblog.com/blog_root/category/your-topic/4
# You can rename the "category" part here:
blog_category_dir = "category"

#### Site css directory ####
# Where to write css files generated by blogofile
# (eg, Syntax highlighter writes out a pygments.css file)
# This is relative to site_url
site_css_dir = "/css"

#### Post encoding ####
blog_post_encoding = "utf-8"

#### Post sort order ####
# If this value is 'date', blog articles are sorted by creation time.
# If this value is 'updated', blog articles are sorted by modification time.
blog_post_sort_order = "updated"    

######################################################################
# Advanced Settings
######################################################################
# These are the default ignore patterns for excluding files and dirs
# from the _site directory
# These can be strings or compiled patterns.
# Strings are assumed to be case insensitive.
ignore_patterns = [
    r".*([\/]|[\\])_.*",   #All files that start with an underscore
    r".*([\/]|[\\])#.*",   #Emacs temporary files
    r".*~$]",       #Emacs temporary files
    r".*([\/]|[\\])\.git", #Git VCS dir
    r".*([\/]|[\\])\.hg",  #Mercurial VCS dir
    r".*([\/]|[\\])\.bzr", #Bazaar VCS dir
    r".*([\/]|[\\])\.svn", #Subversion VCS dir
    r".*([\/]|[\\])CVS"    #CVS dir
    ]

import logging
import datetime
import pytz
import re
import os
from BeautifulSoup import *
logger = logging.getLogger("blogofile.config")

org_exported_src_dir = "_tmp"
html_dest_dir = "_posts"

yaml_template = """---
title: %s
date : %s
updated: %s
categories: %s  
---
"""

### Pre/Post build hooks:
def pre_build():
    #Do whatever you want before the _site is built
    """For the org exported file in _tmp directory, add yaml header and
       move it to _post directory"""
    posts = []
    if not os.path.isdir(org_exported_src_dir):
        logger.error("There is no __tmp directory")
        return
    post_file_names = [f for f in os.listdir(org_exported_src_dir) \
                           if f.endswith(".html") and not f.startswith("_")]
    for post_fn in post_file_names:
        post_path = os.path.join(org_exported_src_dir,post_fn)
        logger.info("pre_build : process %s" % post_path)
        
        src = open(post_path,"r").read().decode(blog_post_encoding)
        updated = os.path.getmtime(post_path)   # time of most recent content modification
        content = process_file(src, updated)
        f = open(os.path.join(html_dest_dir, post_fn), "w")
        f.write(content.encode(blog_post_encoding))
        f.close()

def get_string(parent):
    l = []
    for tag in parent:
        if isinstance(tag, NavigableString):
            l.append(tag.string)
        else:
            l.extend(get_string(tag))
    return "".join(l)

def process_file(src, updated):
    soup = BeautifulSoup(src)

    # the first h2 section will be used for title, category, and date
    metaline = soup.find('div', {'id': 'outline-container-1'}).h2

    # extract title
    title = re.sub('&nbsp;', '', metaline.contents[0]).strip()

    # extract category
    categories = ", ".join(get_string(metaline('span', {'class':'tag'})).split('&nbsp;'))

    # extract date
    dateStr = metaline('span', {'class':'timestamp'})[0].string # 2009-08-22 Sat 15:22
    # date_format = "%Y/%m/%d %H:%M:%S"
    date = datetime.datetime.strptime(dateStr, "%Y-%m-%d %a %H:%M")
    date = date.replace(tzinfo=pytz.timezone(blog_timezone))
    dateStr = date.strftime("%Y/%m/%d %H:%M:00")

    # updated time
    updated = datetime.datetime.fromtimestamp(updated)
    updated = updated.replace(tzinfo=pytz.timezone(blog_timezone))
    updatedStr = updated.strftime("%Y/%m/%d %H:%M:00")

    # delete first h2 section (which is title and category)
    metaline.extract()

    # 2009/09/25 14:39:23n
    yamlHeader = yaml_template % (title, dateStr, updatedStr, categories)

    # Print soup.body
    tocStr = soup.find('div',  {'id': 'table-of-contents'})
    contentStr = soup.find('div', {'id': 'outline-container-1'})
    footnoteStr = soup.find('div', {'id': 'footnotes'})
    
    if tocStr != None:
        contentStr = str(tocStr) + str(contentStr)

    # if footnoteStr exists, add it to contentStr
    # if footnoteStr != None:
    #     contentStr += str(footnoteStr)

    content = yamlHeader + str(contentStr).decode(blog_post_encoding)
    if footnoteStr != None:
        content += "\n" + str(footnoteStr).decode(blog_post_encoding)
        
    return content
    
def post_build():
    #Do whatever you want after the _site is built
    pass

def post_excerpt(content, num_words=50):
    #Default post excerpting function
    #Can be overridden in _config.py by
    #defining post_excerpt(content,num_words)
    """Retrieve excerpt from article"""

    s = BeautifulSoup(content)

    excerpt = ''.join([str(e).decode('utf-8') for e in s.findAll('p', limit=2)])
    excerpt += "<i>Read more...</i>"
    return excerpt
