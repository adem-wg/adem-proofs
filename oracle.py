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
elif argv[1] == 'VerifiedAuthorityOrigin':
  match = matchAgainstList([
    'VerifyEndorsements',
  ], lines)
elif argv[1] == 'AuthenticEmblem':
  match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~(ltk|rootKey)'),
    '!KU( ~rootKey',
    '!KU( ~ltk',
    'RootDomains',
    'VerifyEndorsements',
    '!KU( sign(<\'emblem\'',
    '!KU( sign(<\'end_int\'',
    re.compile('VerifyAuthoritySetup\( ~id(\.\d+)?, ~sess(\.\d+)?, [\$\d\w\.]+, pk\(~'),
    re.compile('!KU\( sign\(<\'end_ext\', .+ ~[\w\.\d]+\) \) @ #[\w\.\d]+$'),
    re.compile('RootKeyResponse\( ~sess(\.\d+)?, oi'),
  ], lines)
elif argv[1] == 'CAAccountability':
  match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~skCA'),
    '!KU( ~skCA',
    '!KU( sign(',
    'SignatureStore',
    '!TLSKey',
  ], lines)
elif argv[1] == 'LogAccountability':
  match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~(ltk|rootKey|skLog|skCA)'),
    re.compile('!KU\( ~(ltk|rootKey|skLog|skCA)'),
    'DomainOwner',
    'RootDomains',
    re.compile('^[\(\s]*∀'),
    re.compile(r'!KU\( sign\(<\'sct\',.+sha256\(rk_false\)'),
    re.compile(r'!KU\( sign\(<\'cert\',.+sha256\(rk_false\)'),
    '!TLSKey( $P',
  ], lines)
elif argv[1] == 'AuthorityAccountability':
  match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~rootKey'),
    '!KU( ~rootKey',
    'RootDomains',
    re.compile(r'!TLSKey\(.+,\s*\$OI,'),
    '!KU( sign(<\'end_ext\'',
    'VerifyAuthoritySetup',
  ], lines)
elif argv[1] == 'PPAccountability':
    match = matchAgainstList([
    re.compile(r'!TLSKey\(.+, ~rootKey'),
    '!KU( ~rootKey',
    'RootDomains',
    'VerifyEndorsements',
    re.compile(r'!TLSKey\(.+,\s*\$OI,'),
    '!KU( sign(<\'end_int\'',
  ], lines)
elif argv[1] == 'RootKeyUse':
  match = matchAgainstList(['RootKeyResponse'], lines)
elif argv[1] == 'CertBindingIsImpliedAuthority':
  match = matchAgainstList([
    re.compile(r'VerifyAuthoritySetup\(.+,\s*\$OI,'),
    'RootKeyResponse',
  ], lines)
elif argv[1] == 'CertBindingIsImpliedPP':
  match = matchAgainstList([
    'RootDomains',
    'VerifyEndorsements',
    'RootKeyResponse',
  ], lines)

if match is not None:
  print(match)
