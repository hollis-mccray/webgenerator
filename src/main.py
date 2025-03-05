from generate_page import *

def main():
    copy_static()
    generate_page("content/index.md", template_path="template.html", dest_path="public/index.html")
    generate_pages_recursive(dir_path_content="content",template_path="template.html", dest_dir_path="public")

main()