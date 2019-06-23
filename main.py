def main(data: dict):
    """main

    :param data:
    :type data: dict
    """

    input_data = json.dumps(data)
    run_recognition(input_data)


if __name__ == "__main__":
    main()

