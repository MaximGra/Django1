# Generated by Django 4.0.5 on 2022-07-03 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_title_remove_article_themes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'articles and themes',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название тематики')),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
                'db_table': 'Themes',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AlterModelTable(
            name='article',
            table='Articles',
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AddField(
            model_name='articlescope',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.theme'),
        ),
        migrations.AddField(
            model_name='article',
            name='themes',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.theme'),
        ),
    ]