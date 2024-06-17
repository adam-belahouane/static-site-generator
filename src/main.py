from textnode import TextNode
import os
import shutil

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

def main():
    text = TextNode("test", "bold", "www.test.com")
    print(copy_files_to_public())

    

main()



