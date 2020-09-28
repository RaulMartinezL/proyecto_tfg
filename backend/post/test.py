from django.test import TestCase

from .models import Profile, Message

class BasicTest(TestCase):

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2


    def test_fields_profile(self):

        profile = Profile()
        profile.literature = "Esto es la biografia del perfil"
        profile.music = "Me gusta el pop y el popunk"
        profile.sport = "F1"
        profile.party = "mode on"
        profile.art = "calaveras"
        profile.save()

        record = Profile.get(pk=profile.pk)
        self.assertEqual(record, profile)



    def test_fields_message(self):

        message = Message()
        message.text = "Esto es el cuerpo del mensaje"
        message.username = "Usuario1"
        message.date = "05/05/2000"
        message.save()

        record = Message.get(pk=message.pk)
        self.assertEqual(record, message)




