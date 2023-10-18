tamarin-prover --derivcheck-timeout=0 --output=proofs.spthy \
  --prove=TLSKeyShareRecursion \
  --prove=TLSKeyLeakRecursion \
  --prove=WrongCAKeyUseImpliesCompromise \
  --prove=CanObtainRootKey \
  --prove=VerifiedAuthorityOrigin \
  --prove=AuthenticEmblem \
  --prove=CanDisupte \
  --prove=CAAccountability \
  --prove=AuthorityAccountability \
  --prove=PPAccountability \
  --prove=RootKeyUse \
  adem.spthy
