class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)
        #need to add last directory to FileSystem
        #/dir1/dir2 ->dir2 needs to be added
        #first go to dir1 then add dir2
        #/dir1/dir2/dir3
        # got to diretory dir2 and add dir3
        #every time -> go to second last directory and add last
        #directorys seperated with "/"
        #if not Directory instance -> ValueError
        path_names = path[1:].split("/")
        add_path_name = path_names[-1]
        path_to_new_path = path_names[:-1]

        
        # if len(path_to_new_path) == 0:
            # first_directory = Directory(add_path_name)
            # self.root.add_node(first_directory)
            # return
        #find second last
        second_last_node = self._find_bottom_node(path_to_new_path)
        

        #validate that its a directory
        if not isinstance(second_last_node, Directory):
            raise ValueError

        #create new direcoty and add id to the filesystem
        add_new_directory = Directory(add_path_name)
        second_last_node.add_node(add_new_directory)


    def create_file(self, path, contents):
        #go to the directory at the bottom
        #follow path until the end (function: find_bottom_node)
        #create a file (Class File)
        FileSystem._validate_path(path)
        path_names = path[1:].split("/")
        file_name = path_names[-1]
        path_to_new_file = path_names[:-1]


        desired_directory = self._find_bottom_node(path_to_new_file)

        #Validate that the path end is acutally a Direcotry (Class)
        if not isinstance(desired_directory, Directory):
            raise ValueError
        
        created_file = File(file_name)
        created_file.write_contents(contents)

        desired_directory.add_node(created_file)
        


    def read_file(self, path):
        FileSystem._validate_path(path)
        path_names = path[1:].split("/")
        file_name = path_names[-1]
        path_to_file = path_names[:-1]
        desired_directory = self._find_bottom_node(path_to_file)

        #Validate that the path end is acutally a Direcotry (Class)
        if not isinstance(desired_directory, Directory):
            raise ValueError

        if file_name not in desired_directory.children:
            raise ValueError
         
        return desired_directory.children[file_name].contents

    def delete_directory_or_file(self, path):
        #/dir1/dir2/dir3
        #delete dir3
        #validate

        FileSystem._validate_path(path)
        desired_path = path[1:].split("/")
        delete_path_name = desired_path[-1]
        path_to_new_path = desired_path[:-1]

        #find second last node
        second_last_node = self._find_bottom_node(path_to_new_path)
        
        #Validate that the path end is acutally a Direcotry (Class)
        if not isinstance(second_last_node, Directory):
            raise ValueError

        #check if file exists
        if not delete_path_name in second_last_node.children:
            raise ValueError


        del second_last_node.children[delete_path_name]


    def size(self):
        #i build me a helper function because i heard of recursion sometime and i wanted to try it
        #it worked somehow :)
        size = _get_size(self.root)
        print("Self.root:", self.root)
        return size



    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    


    def _find_bottom_node(self, node_names):
        #example:
        #["dir1", "dir2", "dir3"]
        #go to dir1 --> look inside dir1 for dir2 (dir1.children)
        #go to dir2 and look for dir3 inside dir2
        #return dir3
        node = self.root
        for name in node_names:
            #search for directorys to go to
            #repeat the process until the end
            #dir1->dir2->dir3....
            if name not in node.children:
               raise ValueError("not in node.children")     

            #forgot to check if its a directory:
            if not isinstance(node, Directory):
                raise ValueError("Not dir type")
            
            node = node.children[name]
            #print(type(node))

        #return the node that is sotred in "node" at the end because this is the bottom node
        return node


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

#size = 0
#helper function to get size
def _get_size(node):
        size = 0
        if isinstance(node, File):
            size += len(node)
        names = node.children
        
        print(names)
        for name in names:
            if isinstance(node.children[name], File):
                size += len(node.children[name])
            elif isinstance(node.children[name], Directory):
                size += _get_size(node.children[name])
            
        return size

#debug
fs = FileSystem()
# fs.create_directory("/dir1")
# fs.create_directory("/dir1/dir3")
#fs.create_file("/tim.txt", "Tim is great!")
#fs.create_directory("/dir1")
#fs.create_directory("/dir1/dir2")
#fs.create_directory("/dir1/dir2/dir3")
#fs.create_file("/dir1/dir2/file1.txt", "1")
#fs.create_file("/dir1/dir2/dir3/file2.txt", "1")
#print(fs.size())# 2)


#fs.delete_directory_or_file("/dir1") #ValueError -> correct
fs.create_directory("/dir1")
fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
print(fs.size()) 
##fs.delete_directory_or_file("/dir2") #ValueError -> correct
#fs.delete_directory_or_file("/dir1")
#print(fs.size()) #0

