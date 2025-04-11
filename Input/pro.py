import os 


def exceptionHandling(folder_path):
    try:
        files = os.listdir(folder_path)
        return files,None
    except FileNotFoundError:
       return None,"{folder_path} this one doest not eixst"
    except PermissionError:
        return None, "{folder_path} for this folder you do not have the permission"
    


def main():

    folder_paths = input("Mention the folder name seperated by commas").split(",")
    print(folder_path)
    for folder_path in folder_paths:
        files,error_message = exceptionHandling(folder_path)
        if files : 
            print("files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print("Error in {folder_path}: error_message")

        
if __name__ == "__main__":
    main()
    

