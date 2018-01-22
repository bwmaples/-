import os
path = "E:\\dex2jar-2.0\\xiamibak"
def prefliter( filepath ):
    subdir = os.listdir(filepath)
    for parent in subdir:
        if "smali" in parent:
            child = os.path.join(filepath,parent)
            if os.path.isdir(child):
                print (child)
                traverse(child)
            else:
                print(child)

def traverse( filepath ):
    subdir = os.listdir(filepath)
    for parent in subdir:
        child = os.path.join(filepath,parent)
        if os.path.isdir(child):
            print (child)
            traverse(child)
        else:
            print(child)


if __name__ == '__main__':
    prefliter(path)
