# Generated by Django 4.1.7 on 2023-03-27 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0017_newsitem_drupal_node_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsitem",
            name="news_topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="news_items",
                to="news.newstopic",
            ),
        ),
        migrations.AlterField(
            model_name="newsitem",
            name="news_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="news_items",
                to="news.newstype",
            ),
        ),
        migrations.AlterField(
            model_name="newsitem",
            name="teaser",
            field=models.TextField(
                blank=True,
                help_text="Briefly summarize the news item for display in news lists",
                max_length=100,
                null=True,
            ),
        ),
    ]