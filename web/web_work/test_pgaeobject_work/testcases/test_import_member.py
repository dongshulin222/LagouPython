from web.web_work.test_pgaeobject_work.pages.main_page import MainPage


class TestImportMember:
    def setup(self):
        self.main = MainPage()
        self.phone = '13701667140'

    def test_import_member(self):
        assert self.phone in self.main.goto_import_member().import_member().get_member()
