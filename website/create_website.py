import glob
from string import Template
import os
from subprocess import call
import re
import markdown2


html_path     ='./html/'  # insert the path to the directory of interest
deploy_path   ='../'
template_path ='./template/'
bibtext_path  ='./bibtex/'
images_path   ='./images/'
bibtex_path   ='./bibtex/'
blog_path     ='./blog/'
papers_path   = bibtex_path + "/papers/"

#clean up and make directory
call(["rm", "-rf", deploy_path ])
call(["mkdir", deploy_path ])
#clean up lame files
# find . -type f -name "*~" | xargs rm

# copy images to deploy
call(["cp", "-r", images_path, deploy_path ])
# copy paper 

call(["cp", "-r", papers_path, deploy_path ])

# run bibtex
print "Running bibtex..."
call(["bibtex2html", "-d", "-r", "--nodoc", bibtex_path + "allpapers.bib"])

all_papers_file = open('allpapers.html', 'r')
all_papers_file_text = all_papers_file.read()
all_papers_file_text = all_papers_file_text.replace('&lt;', '<')
all_papers_file_text = all_papers_file_text.replace('&gt;', '>')

all_papers_file_text = re.sub("<p>.*", "", all_papers_file_text)
all_papers_file_text = re.sub(".*bibtex2html.*", "", all_papers_file_text)

# I don't really know where this is coming from !
all_papers_file_text = all_papers_file_text.replace('with the following command:', '')
all_papers_file.close()
call(["rm", "-r", 'allpapers.html' ])

all_papers_deploy_file = open(template_path + 'allpapers.html', 'w')
all_papers_deploy_file.write(all_papers_file_text)
all_papers_deploy_file.close();

call(["mv", "-f", "./allpapers_bib.html", deploy_path])




# Loop through HTML path

html_string_files = glob.glob(html_path+"*.html") + glob.glob(html_path+"*.css")

for html_string in html_string_files:
    print "Processing file " + html_string
    html_file = open(html_string, 'r')
    html_file_text = html_file.read()
    # Loop through Template path
    for template_string in glob.glob(template_path + "*.html"):
        template_file = open(template_string, 'r')
        template_file_text = template_file.read()
        template_file_key  = "$" + os.path.split(template_string)[-1]
        print "Applying template " + template_file_key
        html_file_text = html_file_text.replace(template_file_key, template_file_text)
    
    deploy_html_string = deploy_path + os.path.split(html_string)[1]
    #print deploy_html_string
    deploy_html_file = open(deploy_html_string, 'w')
    deploy_html_file.write(html_file_text)
    deploy_html_file.close()
    
    #all_text = f.read()
    #print all_text
    #print os.path.splitext(name)[0]
    

# Blog stuff
################################################################################
blog_name_pp = "blog-requires-pp.html"
blo_file = open(deploy_path+blog_name_pp, 'r')
html_content = blo_file.read()
blo_file.close()
blog_content = ""
blog_files = glob.glob(blog_path+"*.md")

blog_files.sort()
blog_files = blog_files[::-1]

for blog_string in blog_files:
    blog_file = open(blog_string, 'r')
    blog_file_text = blog_file.read()
    blog_file_text =  blog_file_text.replace("$date", os.path.split(blog_string)[1][:-3])
    converted = markdown2.markdown(blog_file_text)
    blog_content+=converted
html_content = html_content.replace("$blog", blog_content)
deploy_blog_file = open(deploy_path+"blog.html", 'w')
deploy_blog_file.write(html_content)
deploy_blog_file.close()

call(["rm", "-r", deploy_path + blog_name_pp ])


################################################################################


#Links stuff
links_name_pp = "links-requires-pp.html"

links_file_pp = open(deploy_path + links_name_pp , 'r')
links_file_md = open(html_path + "links.md",'r')

links_content = links_file_pp.read()
links_md_content = links_file_md.read()
#print links_md_content
converted = markdown2.markdown(links_md_content)

links_content = links_content.replace("$links", converted)

deploy_links_file = open(deploy_path+"links.html", 'w')
deploy_links_file.write(links_content)
deploy_links_file.close()


call(["rm", "-r", deploy_path + links_name_pp ])

   
