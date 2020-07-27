import os

import click
import sys

sys.path.append(r'D:\\Documents\weather')
from weather.table_creator.local_files.local_files import LocalFiles


@click.group()
def cli():
    pass


@cli.command("stats")
@click.argument("lat")
@click.argument("lng")
@click.argument("start")
@click.argument("end")
def stats_cli(lat, lng, start, end):
    ob1 = LocalFiles()
    ob1.get_values(lat, lng, start, end)
    ob1.transformation()
    ob1.create_name()
    ob1.record()
    click.echo(f"Файл {ob1.name_file} записан по адресу {os.getcwd()}")
if __name__ == '__main__':
    cli()


