

my_dict = {'pres':'Sara', 'sec':'Ann', 'treas':'Mary'}


def in_dict(key, value):
    if key and value in my_dict:
        return True
    else:
        return False


if __name__ == '__main__':
    in_dict('VP', 'Jan')


