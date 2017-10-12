from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from model_mommy import mommy
from django.conf import settings

# Get custom user model
User = get_user_model()


class EditPasswordTestCase(TestCase):
    """
    Test to edit password from user.
    """

    def setUp(self):
        """
        This method will run before any test case.
        """

        self.client = Client()
        self.url = reverse('accounts:update-password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('test1234')
        self.user.save()

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.user.delete()

    def test_update_password_ok(self):
        """

        """

        data = {
            'old_password': 'test1234',
            'new_password1': 'test12345678',
            'new_password2': 'test12345678'
        }

        self.client.login(username=self.user.username, password='test1234')
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('test12345678'))

    def test_redirect_to_login(self):
        """
        Test to redirect to login page when user try to access the edit
        password without be logged.
        """

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        login_url = reverse('accounts:login')
        redirects_url = '{0}?next={1}'.format(login_url, self.url)
        self.assertRedirects(response, redirects_url)

    def test_update_old_password_fail(self):
        """
        Test to get an error when user pass incorrect old password.
        """

        data = {
            'old_password': 'incorrect',
            'new_password1': 'test12345678',
            'new_password2': 'test12345678'
        }

        self.client.login(username=self.user.username, password='test1234')
        response = self.client.post(self.url, data)
        self.assertFormError(
            response, 'form', 'old_password',
            _('Your old password was entered incorrectly. Please enter it again.')
        )
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('test1234'))

    def test_update_new_password_fail(self):
        """
        Test to get an error whe user pass incorrect new password confirmation
        """

        data = {
            'old_password': 'test1234',
            'new_password1': 'test12345678',
            'new_password2': 'test12345'
        }

        self.client.login(username=self.user.username, password='test1234')
        response = self.client.post(self.url, data)
        self.assertFormError(
            response, 'form', 'new_password2',
            _("The two password fields didn't match.")
        )
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('test1234'))
