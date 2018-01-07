import click
import logging
from protonamegen import gen_name


@click.command()
@click.argument('n', nargs=1, type=click.INT, default=1)
def gen_proto_name(n):
  for i in gen_name(n):
    print(i)


@click.command()
def init_proto_name():
  logging.basicConfig(level=logging.DEBUG)
  logger = logging.getLogger()
  print (""" Please download the relevant packages.""")
  import nltk
  nltk.download()
