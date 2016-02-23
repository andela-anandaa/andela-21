class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)


    @name.setter
    def name(self, name):
        name = name.split()
        self.first_name = name[0]
        self.last_name = name[1]
    