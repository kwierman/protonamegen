import click
import logging
from protonamegen import gen_name


@click.command()
def gen_proto_name():
  print gen_name()


@click.command()
def init_proto_name():
  logging.basicConfig(level=logging.DEBUG)
  logger = logging.getLogger()
  print """ Please download the relevant packages.
  """
  import nltk
  nltk.download()
