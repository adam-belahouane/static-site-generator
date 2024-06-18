from textnode import TextNode
import os
import shutil
import stat
from markdowntohtml import markdown_to_html_node

def copy_if_file(static_path,public_path,li):
        for item in li:
            path_to_copy = static_path + "/" + item
            where_im_copying_too = public_path
            if os.path.isfile(path_to_copy):
                shutil.copy(path_to_copy, where_im_copying_too)
            if os.path.isdir(path_to_copy):
                new_public_path = where_im_copying_too + "/" + item
                os.mkdir(new_public_path)
                copy_if_file(path_to_copy, new_public_path, os.listdir(path_to_copy))

def copy_files_to_public():
    shutil.rmtree("/home/adam_belahouane/workspace/github.com/adam-belahouane/static-site-generator/public")
    static_path = "/home/adam_belahouane/workspace/github.com/adam-belahouane/static-site-generator/static"
    public_path = "/home/adam_belahouane/workspace/github.com/adam-belahouane/static-site-generator/public"
    if not os.path.exists(public_path):
        os.mkdir(public_path)

    if os.path.exists(static_path):
        contents_of_dir = os.listdir(static_path)
        copy_if_file(static_path, public_path, contents_of_dir)

    return "we did it"

def extract_title(markdown):
    with open(markdown) as f:
        read_data = f.read()
        if read_data.startswith("#"):
            title = read_data.split("\n")[0]
            title = title.strip("# ")
        f.close()
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as fp:
        from_path_data = fp.read()
        fp.close()
    with open(template_path) as tp:
        template_path_data = tp.read()
        tp.close()
    contents_data = markdown_to_html_node(from_path_data).to_html()
    title_data = extract_title(from_path)
    # print(contents_data, title_data)
    template_path_data = template_path_data.replace("{{ Title }}", title_data)
    template_path_data = template_path_data.replace("{{ Content }}", contents_data)
    with open("./public/index.html", "w") as index_html:
        index_html.write(template_path_data)
        index_html.close()

def main():
    copy_files_to_public()
    generate_page("./content/index.md", "./template.html", "./public")
    

main()



