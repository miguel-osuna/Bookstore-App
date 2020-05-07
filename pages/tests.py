from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """The page exists and returns a HTTP 200 status code."""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """The proper template is being used by the view."""
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        """Checks if the homepage view has the correct html."""
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):
        """Checks if the homepage contains does not containt the incorrect html."""
        self.assertNotContains(self.response, "Hi, I should not be on the page")

    def test_homepage_view(self):
        """Checks if it's the same view."""
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


# Create your tests here.
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        """The page exists and returns a HTTP 200 status code."""
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        """The proper template is being used by the view."""
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        """Checks if the aboutpage view has the correct html."""
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        """Checks if the aboutpage contains does not containt the incorrect html."""
        self.assertNotContains(self.response, "Hi, I should not be on the page")

    def test_aboutpage_view(self):
        """Checks if it's the same view."""
        view = resolve("about/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
