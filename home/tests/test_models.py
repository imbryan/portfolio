from django.test import TestCase

from datetime import datetime

from home.models import BlogPost


class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(
            date_published=datetime.now(),
            post_title="Post",
            post_body="<div>Post text</div>",
        )
        BlogPost.objects.create(
            date_published=datetime.now(),
            post_title="Post with 51 words", 
            post_body="<div>" + ("word " * 51).strip() + "</div>",
        )
        BlogPost.objects.create(
            date_published=datetime.now(),
            post_title="Post with preview",
            post_body="<div>Post text</div>",
            preview_text="Preview text",
        )

    def test_default_preview(self):
        post = BlogPost.objects.get(post_title="Post")
        self.assertEqual(post.preview_text, "Post text")
        self.assertNotIn("<div>", post.preview_text)

    def test_default_preview_51_words(self):
        post = BlogPost.objects.get(post_title="Post with 51 words")
        self.assertEqual(len(post.preview_text.split()), 50)
        self.assertEqual(post.preview_text[-1], "…")
        self.assertNotIn("<div>", post.preview_text)

    def test_given_preview(self):
        post = BlogPost.objects.get(post_title="Post with preview")
        self.assertEqual(post.preview_text, "Preview text")
