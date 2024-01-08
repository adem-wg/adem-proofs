#!/usr/bin/env python3

from sys import argv, stdin, exit
import re

def splitter(line):
  splitted = line.split(':')
  return (splitted[0], splitted[1].strip())

lines = list(map(splitter, stdin.readlines()))
if not lines:
  exit(0)

def subToken(token, line):
  (num, goal) = line
  if isinstance(token, str):
    return num if token in goal else None
  else:
    return num if token.search(goal) is not None else None

def matchAgainstList(priorityList, lines):
  for token in priorityList:
    try:
      return next(filter(bool, map(lambda line: subToken(token, line), lines)))
    except StopIteration:
      pass

match = None
if argv[1] in ['CanObtainRootKey', 'CanReceiveEmblem']:
  match = matchAgainstList([
    'VerifyAuthorityEndorsements',
    '!CA',
    '!Log',
    '!TLSKey',
    '!DomainOwner',
    'VerifyEndorsements',
    'RootDomains',
    'VerifyAuthoritySetup',
    'RootKeyResponse',
    'St_',
    '!KU( ~',
    'sign',
    'tlsClientMsg',
    'tlsServerMsg',
  ], lines)
elif argv[1] == 'AuthenticEmblem':
  match = matchAgainstList([
    re.compile(r'!Ltk\( .*, ~'),
    re.compile(r'!TLSKey\(.+, ~(assetKey|rootKey)'),
    '!KU( ~rootKey',
    '!KU( ~assetKey',
    'RootDomains',
    'VerifyEndorsements',
    '!KU( sign(<\'emblem\'',
    '!KU( sign(<\'end_int\'',
    re.compile(r'VerifyAuthoritySetup\( ~id(\.\d+)?, ~sess(\.\d+)?, [\$\d\w\.]+, pk\(~'),
    re.compile(r'!KU\( sign\(<\'end_ext\', .+ ~[\w\.\d]+\) \) @ #[\w\.\d]+$'),
    re.compile(r'RootKeyResponse\( ~sess(\.\d+)?, oi'),
  ], lines)
elif argv[1] == 'CAAccountability':
  match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~skCA'),
    '!KU( ~skCA',
    '!KU( sign(',
    'SignatureStore',
    'LogInclusion',
    '!TLSKey',
  ], lines)
elif argv[1] == 'AuthorityAccountability':
  match = matchAgainstList([
    '!KU( sign(<\'end_ext\'',
    re.compile(r'!Ltk\( .+, ~'),
    '!KU( ~rootKey',
  ], lines)
elif argv[1] == 'PPAccountability':
  match = matchAgainstList([
    '!KU( sign(<\'end_int\'',
    '!KU( ~rootKey',
  ], lines)
elif argv[1] == 'RootKeyUse':
  match = matchAgainstList(['RootKeyResponse'], lines)
elif argv[1] == 'RootKeyUse':
  match = matchAgainstList([
    'UsedRootKey',
    'RootKeyVerified',
  ], lines)

if match is not None:
  print(match)
