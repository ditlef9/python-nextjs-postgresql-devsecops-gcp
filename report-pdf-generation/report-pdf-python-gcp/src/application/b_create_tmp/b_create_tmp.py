import os


def b_create_tmp():
    """
    Creates temp directories
    :return:
    """

    # Create dirs
    if not os.path.isdir("_tmp"):
        print("b_create_tmp() · Creating dir _tmp")
        os.makedirs("_tmp", exist_ok=True)