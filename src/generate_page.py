from markdown_to_html import markdown_to_html_node
from pathlib import Path
import os, shutil

def copy_static(static_dir, dest_dir):

    src_path = os.path.join(os.curdir, static_dir)
    dest_path = os.path.join(os.curdir, dest_dir)

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    os.mkdir(dest_path)

    subcopy(src_path,dest_path)

def subcopy(source, destination):
    src_list = os.listdir(source)
    for item in src_list:
        item_path = os.path.join(source,item)
        if os.path.isfile(item_path):
            shutil.copy(item_path,destination)
        else:
            old_dir = os.path.join(source, item)
            new_dir = os.path.join(destination, item)
            os.mkdir(new_dir)
            subcopy(old_dir, new_dir)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            sections = line.split(" ", 1)
            title = sections[1].strip()
            return title

    raise Exception("title not found")

def generate_page(from_path, template_path, dest_path, BASEPATH):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(os.path.join(os.curdir,from_path)) as source_file:
        source = source_file.read()

    with open(os.path.join(os.curdir,template_path)) as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown=source).to_html()
    title = extract_title(markdown=source)
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)
    html = html.replace('href="/', f'href="{BASEPATH}')
    html = html.replace('src="/', f'src="{BASEPATH}')

    with open(os.path.join(os.curdir,dest_path), "w") as output:
        output.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, BASEPATH):
    src_list = os.listdir(dir_path_content)
    for item in src_list:
        item_path = os.path.join(dir_path_content,item)
        print(item_path)
        if os.path.isfile(item_path):
            if Path(item_path).suffix == ".md":
                new_path = os.path.join(dest_dir_path,item)
                new_path = new_path.replace(".md", ".html")
                generate_page(item_path, template_path,new_path, BASEPATH=BASEPATH)
        else:
            old_dir = os.path.join(dir_path_content, item)
            new_dir = os.path.join(dest_dir_path, item)
            os.mkdir(new_dir)
            generate_pages_recursive(old_dir, template_path, new_dir, BASEPATH=BASEPATH)