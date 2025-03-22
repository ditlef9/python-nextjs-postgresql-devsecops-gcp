import os

def a_delete_old():
    """
    Delete old files in the _tmp directory
    :return: None
    """
    # Delete all old files
    for dirpath, _, filenames in os.walk("_tmp"):
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            # Get relative path to maintain directory structure in destination
            print(f"a_delete_old · Deleting {src_file}")
            try:
                os.remove(src_file)  # Actually delete the file
                print(f"a_delete_old · Deleting {src_file} [Ok] ")
            except Exception as e:
                print(f"a_delete_old · Deleting {src_file} [Error: {e}]")

