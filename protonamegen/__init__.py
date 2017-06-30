import nltk
import random

__nouns__      = None
__adjectives__ = None


def __initialize__():
  global __nouns__
  global __adjectives__
  wn = nltk.wordnet.wordnet
  __nouns__ = []
  __adjectives__ = []
  for synset in wn.all_synsets('n'):
    word = synset.name().split('.n').split('.s')[0]
    if not "_" in word or '-' in word:
      __nouns__.append(word)
  for synset in wn.all_synsets('a'):
    word = synset.name().split('.a')[0]
    if not "_" in word or '-' in word:
      __adjectives__.append(word)


def gen_noun():
  global __nouns__
  if __nouns__ is None:
    __initialize__()
  return random.choice(__nouns__)


def gen_adjective():
  global __adjectives__
  if __adjectives__ is None:
    __initialize__()
  return random.choice(__adjectives__)


def gen_name():
  return gen_adjective() + "_" + gen_noun()