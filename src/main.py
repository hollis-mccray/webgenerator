from generate_page import *
import sys

def main():
    static_dir = "static"
    dest_dir = "docs"
    copy_static(static_dir, dest_dir)
    if len(sys.argv) >= 2:
        BASEPATH = sys.argv[1]
    else:
        BASEPATH = "/"
    generate_pages_recursive(dir_path_content="content",template_path="template.html", dest_dir_path=dest_dir, BASEPATH=BASEPATH)

main()