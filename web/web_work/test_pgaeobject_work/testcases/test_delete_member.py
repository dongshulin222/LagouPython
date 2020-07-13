from web.web_work.test_pgaeobject_work.pages.contact_page import ContactPage
from web.web_work.test_pgaeobject_work.pages.main_page import MainPage


class TestDeleteMember:
    def setup(self):
        self.main = MainPage()
        self.contact = ContactPage()

    def test_delete_member(self):
        self.phone = '13701667140'
        self.main.goto_delete_member().delete_member(self.phone)
        assert self.phone not in self.contact.get_member()
