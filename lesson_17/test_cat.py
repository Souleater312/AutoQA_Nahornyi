from lesson_17.cat import Cat


class TestCat:

    def setup_class(self):
        print("I`m setup class function")

    def setup_method(self):
        self.cat = Cat("Porphyriy", "persian", "fluffy", 4)

    def test_check_growing(self):
        self.cat.grow()
        assert self.cat.age == 5

    def test_check_haircat(self):
        self.cat.groom("middle")
        assert self.cat.haircut == "middle"

    def teardown_method(self):
        print("I`m teardown function")

    def teardown_class(self):
        print("I`m teardown class function")
