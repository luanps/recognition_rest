from recognition import Recognition

def main(data: dict):
    """main

    :param data:
    :type data: dict
    """
    rec = Recognition(data)
    rec.convert_base64_to_img()


if __name__ == "__main__":
    main(data)

