import os


def rename_files():
    path = r"C:\**\**\Desktop\**\Folder\prank"# we need the r (rawpack),tells pytho nto take the string as it is and not interpret it in any other way
    #In the above path, we put our path where the prank folder (with the pictures) is located.
    dirs = os.listdir( path )

    old_path = os. getcwd ()
    print("Old path: "+ old_path)
    print()

    new_path = r"C:\**\**\Desktop\**\Folder\prank"
    os.chdir(new_path)
    print("New path: "+ new_path)

    for file_name in dirs:
        #os.chdir(path)
        new_file_name = file_name.translate(str.maketrans('','','1234567890'))
        print("Old Name: "+file_name)
        print("New Name: "+new_file_name)
        print()

        os.rename(file_name, new_file_name)


rename_files()
