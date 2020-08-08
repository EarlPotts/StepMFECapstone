from .top_results import top_results
class business:
    def __init__(self, description, name):
        self.description = description
        self.name = name

    def __str__(self):
        return self.name

class Test:
    def test1(self):
        assert top_results([],["tag"]) == []

    def test2(self):
        results = top_results([business("tag yellow", "walmart"), business("tag red yellow", "target"), business("tag", "kroger")], ["tag", "red", "yellow"])

        for result in results:
            print (result[0])
        assert top_results([business("tag yellow", "name"), business("tag red yellow", "name"), business("tag", "name")], ["tag", "red", "yellow"]) == []

